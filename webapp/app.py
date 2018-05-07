from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import logging
from big_data_kafka import LikesCountsConsumer
logging.basicConfig(level=logging.DEBUG)
from threading import Thread
import json
import eventlet
from flask_cors import CORS
eventlet.monkey_patch()
app = Flask(__name__)
app.debug=True
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode='eventlet', ping_timeout=30, logger=True, engineio_logger=True)
thread=None
@app.route('/')
def index():
    # global thread
    # if thread is None:
    #     thread = Thread(target=background)
    #     thread.start()
    socketio.emit('started',json.loads("[10,12]"), namespace='/')
    return render_template('index.html')
@socketio.on('start_event')
def start_app(data):
    logging.info(data)
    emit('started',json.loads("[10,12]"), namespace='/')
    eventlet.spawn(background)


def background():
    logging.info('Starting background')
    consumer = LikesCountsConsumer.LikesCountsConsumer()
    consumer.start(socketio)


if __name__ == '__main__':
    socketio.run(app)
