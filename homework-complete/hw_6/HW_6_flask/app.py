from datetime import datetime
import pytz
from flask import Flask


app = Flask(__name__)


@app.route('/')
def time_now():
    current_time = datetime.now(pytz.timezone('Europe/Rome'))
    time = current_time.strftime('%Y-%m-%d %H:%M:%S:')
    return f'Time in Rome now is {time}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
