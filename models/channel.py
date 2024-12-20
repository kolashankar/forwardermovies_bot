from mongoengine import Document, StringField, IntField, BooleanField, DateTimeField
from datetime import datetime

class Channel(Document):
    channel_id = IntField(required=True, unique=True)
    title = StringField(max_length=255)
    username = StringField(max_length=255)
    type = StringField(choices=['source', 'destination'], required=True)
    added_by = IntField(required=True)  # User ID who added the channel
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    last_forwarded = DateTimeField()

    meta = {
        'indexes': [
            'channel_id',
            'type',
            'added_by',
            'is_active'
        ]
    }

    def __str__(self):
        return f"{self.title} ({self.channel_id})"

