from mongoengine import Document, IntField, StringField, DateTimeField, ReferenceField
from .channel import Channel
from datetime import datetime

class Message(Document):
    message_id = IntField(required=True)
    chat_id = IntField(required=True)
    from_user = IntField()
    date = DateTimeField()
    text = StringField()
    caption = StringField()
    content_type = StringField()
    file_id = StringField()
    source_channel = ReferenceField(Channel)
    destination_channel = ReferenceField(Channel)
    forwarded_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'indexes': [
            'message_id',
            'chat_id',
            'source_channel',
            'destination_channel',
            'forwarded_at'
        ]
    }

    def __str__(self):
        return f"Message {self.message_id} from {self.source_channel} to {self.destination_channel}"

