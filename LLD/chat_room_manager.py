class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Message:
    def __init__(self, sender_id, content):
        self.sender_id = sender_id
        self.content = content

class ChatRoom:
    def __init__(self, room_id, room_name):
        self.room_id = room_id
        self.room_name = room_name
        self.members = {}
        self.messages = []
    

    def join():
        pass

    def leave():
        pass

    def send_message():
        pass

class ChatRoomManager:

    def __init__(self):
        self.rooms = {}

    def create_chat_room(self, room_id, room_name):

        if room_id in self.rooms:
            raise ValueError("Room Already Exists")

        room = ChatRoom(room_id=room_id, room_name=room_name)
        self.rooms[room_id] = room
        return room

    def delete_chat_room():
        pass

    def get_room():
        pass