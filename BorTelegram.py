import vk_api
import telebot
import types


vk_session = vk_api.VkApi('+994553247948', '1597568962asdF')
vk_session.auth()

vk = vk_session.get_api()




bot = telebot.TeleBot('1396849011:AAGNLhxmdnMgtCQSwxsZVCRL9avv2Vw2PgE') # токен я вставил

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, 'Привет вот список команд:\nКто создал бота-/developer\nСоздать пост на стене вк у разработчика-/post')
    
      
@bot.message_handler(commands=['developer'])
def send_auth(message):
    bot.send_message(message.chat.id,'Этот парень: https://vk.com/idaslanmem')

@bot.message_handler(commands=['post'])
def send_auth(message):
    bot.send_message(message.chat.id,'Напиши любой текст для поста')

@bot.message_handler(content_types=['text'])
def start(message):
    print(vk.wall.post(message=message.text))
    bot.send_message(message.chat.id, "Пост с текстом "+message.text+" создан успешно :) Аслан будет рад \nПост создан тут https://vk.com/idaslanmem")



bot.polling()