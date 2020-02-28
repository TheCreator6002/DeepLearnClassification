import telebot
import os
from NN import answer_bot
from skimage import io
from Foto_verifications import euclidean_distance, descriptor_finding
import time

# Identification bot
tele_bot = telebot.TeleBot('1086910877:AAHs0x480zUDPmY7ooi9YlYJi0VbiC12rao')


# Start reaction
@tele_bot.message_handler(commands=['start'])
def start_message(message):
    tele_bot.send_message(message.chat.id, 'Я родился! /start')

@tele_bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Кошки и собаки':
        tele_bot.send_message(message.chat.id, 'Пришлите фото животного')
        @tele_bot.message_handler(content_types=['photo'])
        def handle_docs_photo(message):
            try:
                file_info = tele_bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = tele_bot.download_file(file_info.file_path)

                with open((file_info.file_id), 'wb') as new_file:
                    new_file.write(downloaded_file)
                tele_bot.reply_to(message, "Фото получил, обрабатываю...")
                thisFile = file_info.file_id
                time.sleep(5)
                base = "1"
                os.rename(thisFile, base + ".jpg")
                file = '1.jpg'
                answer = answer_bot(file)
                if answer == 0:
                    tele_bot.send_message(message.chat.id, 'Собака')
                    os.remove('1.jpg')
                elif answer == 1:
                    tele_bot.send_message(message.chat.id, 'Кошка')
                    os.remove('1.jpg')

            except Exception as e:
                tele_bot.reply_to(message, e)
                os.remove('1.jpg')

    elif message.text == 'Верификация':
        tele_bot.send_message(message.chat.id, 'Пришлите фото')
        @tele_bot.message_handler(content_types=['photo'])
        def handle_docs_photo(message):
            try:

                file_info = tele_bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = tele_bot.download_file(file_info.file_path)

                with open((file_info.file_id), 'wb') as new_file:
                    new_file.write(downloaded_file)
                tele_bot.reply_to(message, "Фото получил, обрабатываю...")
                file1 = ''
                check_Identificator = os.path.exists('1.jpg')
                if check_Identificator == False:
                    thisFile = file_info.file_id
                    time.sleep(5)
                    base = "1"
                    os.rename(thisFile, base + ".jpg")
                    file1 = '1.jpg'
                    tele_bot.send_message(message.chat.id, 'Пришлите второе фото...')
                else:
                    thisFile = file_info.file_id
                    time.sleep(5)
                    base = "2"
                    os.rename(thisFile, base + ".jpg")
                    file2 = '2.jpg'
                    img1 = io.imread('1.jpg')
                    img2 = io.imread('2.jpg')

                    answer = euclidean_distance(descriptor_finding, img1, img2 )
                    print(answer)
                    if answer < 0.6:
                        tele_bot.send_message(message.chat.id, 'На фото один человек')
                        os.remove('1.jpg')
                        os.remove('2.jpg')
                    else:
                        tele_bot.send_message(message.chat.id, 'На фото разные люди')
                        os.remove('1.jpg')
                        os.remove('2.jpg')
            except Exception as e:
                tele_bot.reply_to(message, e)
                os.remove('1.jpg')
                os.remove('2.jpg')


@tele_bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '?':
        tele_bot.send_message(message.chat.id, '!')


tele_bot.polling()


