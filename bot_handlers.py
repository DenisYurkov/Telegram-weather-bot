from bot import *  # Import bot object and owm
from messages import *  # Import everything from the message file

# We send bot greetings
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, HELP_MESSAGE)


# Analyzing user input and displaying weather conditions
@bot.message_handler(content_types=['text'])
def send_input(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]

        answer = "Enter your message " + message.text.title() + " Enter your message " + w.get_detailed_status() + "!" + "\n"
        answer += "Enter your message " + message.text + " Enter your message " + str(temp) + "°" + " !" + "\n\n"

        if temp < 10:
            answer += ANSWER_TEMP_10
        elif temp < 20:
            answer += ANSWER_TEMP_20
        else:
            answer += ANSWER_ELSE

        bot.send_message(message.chat.id, answer)

    # The exception helps to fix the error, now the program does not stop from user error
    except pyowm.exceptions.api_response_error.NotFoundError:
        bot.reply_to(message, MESSAGE_ERROR)


# The bot works without stopping
if __name__ == "__main__":        
    bot.polling(none_stop=True)
