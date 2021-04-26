class NoSuchCart(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id
