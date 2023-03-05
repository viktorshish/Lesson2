"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from datetime import datetime
import logging
import settings
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# format='%(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def greet_user(update, context):
    logger.info('Вызван /Start')
    update.message.reply_text('Здравствуй, пользователь! Введите команду: /planet и название планеты английскими буквами. Пример: /planet mars')

def planet_in_the_constellation(update, context):
    planet_user = update.message.text.split()[1].capitalize()
    logger.info(f'Выбрана планета: {planet_user}')
    list_planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluton']
    if planet_user in list_planets:
        planet = getattr(ephem, planet_user)(datetime.now())
        constellation = ephem.constellation(planet)
        date_now = datetime.now().strftime('%Y-%m-%d')
        update.message.reply_text(f'На текщий день: {date_now} - планета {planet_user} находдится в созведии {constellation}')
        logger.info(f'Расчет произведен и отправлен пользователю  - {planet} - {constellation}')
    else:
        update.message.reply_text('Такой планеты не существует, введите команду правильно')
        logger.info('Расчет не произведен, ошибочно задана планета')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_in_the_constellation))
    dp.add_handler(MessageHandler(Filters.text, planet_in_the_constellation))


    logger.info('Бот запущен')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
