from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from key import TOKEN


def main():
    # updater - класс, который ловит обновления из телеграма
    # по сути, фронтенд для бота
    updater = Updater(
        token=TOKEN,
        use_context=True  # для обратной совместимости с версиями 12 и ниже
    )
    # диспетчер распределяет сообщения по обработчикам
    dispatcher = updater.dispatcher

    # создаем обработчик, который ловит все сообщения
    echo_handler = MessageHandler(Filters.all, do_echo)
    hello_handler = MessageHandler(Filters.text('Привет, привет'), say_hello)

    # регистрируем обработчики. ПОРЯДОК ВАЖЕН!
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    print('Бот успешно запустился')  # Отладочная печать
    updater.idle()


def do_echo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    text = update.message.text
    update.message.reply_text(text=f'Твой id: {chat_id}\n'
                                   f'Ты написал: {text}\n')


def say_hello(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    update.message.reply_text(text=f'Привет, {name}!\n'
                                   f'Приятно познакомиться с живым человеком.\n'
                                   f'Я - бот!')


if __name__ == '__main__':
    main()
