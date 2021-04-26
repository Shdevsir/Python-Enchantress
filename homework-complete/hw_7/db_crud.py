import psycopg2


class BaseConnection:
    def __enter__(self):
        self.conn = psycopg2.connect(
            database='shdevsir',
            user='shdevsir',
            password='pass',
            host='localhost'
        )
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_td):
        self.conn.commit()
        self.conn.close()


class CRUDu:
    @staticmethod
    def create_user(user_info: dict):
        with BaseConnection() as cursor:
            cursor.execute("""
            INSERT INTO  users(name, email, registration_time)
            VALUES
            (%(name)s, %(email)s, %(registration_time)s)""", user_info)

    @staticmethod
    def last_user_id():
        with BaseConnection() as cursor:
            cursor.execute("""
            SELECT id FROM users ORDER BY id DESC LIMIT 1
            """)
            _id = cursor.fetchone()
            return _id

    @staticmethod
    def read_user(_id: int):
        with BaseConnection() as cursor:
            cursor.execute("""
            SELECT name, email, registration_time FROM users WHERE id = %s
            """, (_id,))
            results = cursor.fetchone()
            return results

    @staticmethod
    def update_user(new_info: dict, _id: int):
        with BaseConnection() as cursor:
            cursor.execute(f"""
            UPDATE users SET name=%(name)s, email=%(email)s,
            registration_time=%(registration_time)s
            WHERE id = {_id}""", new_info)

    @staticmethod
    def delete_user(_id: int):
        with BaseConnection() as cursor:
            cursor.execute("""DELETE FROM users
            WHERE id = %s""", (_id,))


class CRUDc:
    @staticmethod
    def create_cart(cart: dict):
        with BaseConnection() as cursor:
            cursor.execute("""INSERT INTO cart(creation_time, user_id)
            VALUES(%(creation_time)s, %(user_id)s)""", cart)
            cursor.executemany("""
            INSERT INTO cart_details (cart_id, price, product)
            VALUES (%(cart_id)s, %(price)s, %(product)s)
            """, cart["cart_details"])

    @staticmethod
    def update_cart(cart: dict):
        with BaseConnection() as cursor:
            cursor.execute("""UPDATE cart SET creation_time=(%(creation_time)s)
            WHERE user_id = %(user_id)s""", cart)
            cursor.executemany("""UPDATE cart_details SET price = %(price)s,
            product = %(product)s
            WHERE cart_id = %(cart_id)s""", cart["cart_details"], )

    @staticmethod
    def read_cart(_id: int):
        with BaseConnection() as cursor:
            cursor.execute("""SELECT * FROM cart_details
            WHERE cart_id = %s""", (_id,))
            results = cursor.fetchall()
        return results

    @staticmethod
    def delete_cart(_id: int):
        with BaseConnection() as cursor:
            cursor.execute("""DELETE FROM cart_details
            WHERE cart_id = %s""", (_id,))
