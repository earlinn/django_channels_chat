
import json

from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # проверяем, аутентифицирован ли пользователь
        if not self.scope["user"].is_authenticated:  # проверять авторизацию или аутентификацию?
            raise DenyConnection("User is not authenticated")

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # присоединяемся к группе
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_id = text_data_json["message_id"]
        reply_to = text_data_json.get("reply_to")  # ID сообщения, на которое отвечаем
        username = self.scope["user"].username

        # отправляем сообщение в группу
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "message_id": message_id,
                "reply_to": reply_to,
                "username": username,
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        message_id = event["message_id"]
        reply_to = event["reply_to"]
        username = event["username"]

        # отправляем сообщение обратно клиенту
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "message_id": message_id,
                    "reply_to": reply_to,
                    "username": username,
                }
            )
        )
