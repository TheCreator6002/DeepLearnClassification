import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# API key
token = '69d973cd2cfbe4b7aac0fb84e1b500a2bd10b5520a86d79a751277f2a2c1dc022f0f82f5b654466d8b91b'

# Authorization bot
vk = vk_api.VkApi(token=token)
group_id ='581854678'


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})


# Message check
longpoll = VkBotLongPoll(vk, group_id)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text

            if request == "hi":
                write_msg(event.user_id, "hi")



