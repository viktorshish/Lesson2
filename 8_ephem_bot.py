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
import logging
import datetime
import settings
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def greet_user(update, context):
    logger.info('Вызван /Start')
    update.message.reply_text('Здравствуй, пользователь! Введите команду: /planet [Название планеты на английском языке]')

def planet_in_the_constellation(update, context):
    planet = update.message.text.split()[1].lower()
    if planet == 'mercury':
        mercury = ephem.Mercury(datetime.datetime.now())
        constellation = ephem.constellation(mercury)
    elif planet == 'venus':
        venus = ephem.Venus(datetime.datetime.now())
        constellation = ephem.constellation(venus)
    elif planet == 'jupiter':
        jupiter = ephem.Jupiter(datetime.datetime.now())
        constellation = ephem.constellation(jupiter)
    elif planet == 'saturn':
        saturn = ephem.Saturn(datetime.datetime.now())
        constellation = ephem.constellation(saturn)
    elif planet == 'uranus':
        uranus = ephem.Uranus(datetime.datetime.now())
        constellation = ephem.constellation(uranus)
    elif planet == 'neptune':
        neptune = ephem.Neptune(datetime.datetime.now())
        constellation = ephem.constellation(neptune)


    else:
        print('Ничего не выбрано')

    print(f'На текущее время: {datetime.datetime.now()} - планета {planet.capitalize()} находдится в созведии {constellation}')

    # print('Ничего не выбрано')
# def talk_to_me(update, context):
#     text = update.message.text.split()[1]
#     if text =='mars':
#         mars = ephem.Mars(datetime.today())
#         constellation = ephem.constellation(mars)
#     else:
#         logger.info(f'Ничего не выбрано')
#         update.message.reply_text('Ничего не выбрано')
#     logger.info(f'Выбрана планета: {text}')
#     update.message.reply_text(f'Выбрана планета: {text} - Находится в созвездии {constellation}')

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
