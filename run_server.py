import flask
from telebot import types
from config import *
from bot_handlers import bot, owm
import os

server = flask.Flask(__name__)


@server.route('/' + TOKEN_TELEGRAM, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(
        flask.request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/' + TOKEN_PYOWM, methods=['POST'])
def get_message_pyowm():
    owm.process_new_updates([types.Update.de_json(
        flask.request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN_TELEGRAM))
    return "Hello from Heroku!", 200


@server.route('/', methods=["GET"])
def index_pyowm():
    owm.remove_webhook()
    owm.set_webhook(url="http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={}".format(TOKEN_PYOWM))
    return "Hello PYOWM!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
