from django.core.management.base import BaseCommand
from telegram import Bot, Update  # pip install python-telegram-bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from telegram.utils.request import Request
from django.conf import settings
from youtube_dl import DownloadError

from tgBot.models import Profile, Message
from tgBot.download_vid import download_video

def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner

@log_errors
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
                     'name': update.message.from_user.username,
                 }
    )

    update.message.reply_text(
        text='Привет! Пришли мне ссылку на видео, которое хочешь скачать',
    )


@log_errors
def users_url(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
                     'name': update.message.from_user.username,
                 }
    )
    Message(
        profile=p,
    ).save()

    try:
        update.message.reply_text(
            text='Начинаю загрузку',
        )
        download_video(text)
        update.message.reply_text(
            text=download_video(text),
        )

    except DownloadError:
        update.message.reply_text(
            text='Не могу распознать ссылку',
        )


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        # 1 -- подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0
        )
        bot = Bot(
        request = request,
        token = settings.TOKEN
        )
        print(bot.getMe()) #python manage.py bot

        # 2 -- обработчики
        updater = Updater(
            bot=bot,
            use_context=True,
        )


        message_start = CommandHandler('start', start)
        updater.dispatcher.add_handler(message_start)


        message_url = MessageHandler(Filters.text, users_url)
        updater.dispatcher.add_handler(message_url)


        # 3 -- запустить бесконечную обработку входящих сообщений
        updater.start_polling()
        updater.idle()



