import telebot
from telebot import apihelper
import time

TOKEN= "8967536754:AAH4RAWeTQ3NAuqmdHT2x6fIk7iKCsy7oS8"

# ТВОЙ SOCKS5 ПРОКСИ ИЗ НАСТРОЕК
apihelper.proxy = {'http': 'socks5://192.168.16.79:10808'}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-калорийщик.")

print("Bot started...")
bot.polling()

# Бесконечный цикл: если упал — перезапускается
while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print(f"Ошибка: {e}")
        print("Перезапуск через 5 секунд...")
        time.sleep(5)