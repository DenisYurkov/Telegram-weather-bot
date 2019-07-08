import telebot
import pyowm
import config  # we connect config to take tokens

# We get Telegram token
bot = telebot.TeleBot(config.TOKEN_TELEGRAM)
print(bot.get_me())

# We get OpenWeatherMap token
owm = pyowm.OWM(config.TOKEN_PYOWM, language='ru')
