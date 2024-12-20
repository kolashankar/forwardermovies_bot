import json
from models.user import User
from models.forwarding_task import ForwardingTask

class BackupService:
    @staticmethod
    def create_backup(user_id):
        user = User.query.get(user_id)
        if not user:
            return None

        backup_data = {
            'user': {
                'telegram_id': user.telegram_id,
                'username': user.username,
                'is_premium': user.is_premium
            },
            'forwarding_tasks': []
        }

        for task in user.forwarding_tasks:
            task_data = {
                'source_channel': task.source_channel,
                'destination_channel': task.destination_channel,
                'is_active': task.is_active,
                'filter_keywords': task.filter_keywords,
                'replace_keywords': task.replace_keywords,
                'begin_text': task.begin_text,
                'end_text': task.end_text
            }
            backup_data['forwarding_tasks'].append(task_data)

        return json.dumps(backup_data, indent=2)

    @staticmethod
    def restore_backup(backup_data):
        data = json.loads(backup_data)
        user = User.query.filter_by(telegram_id=data['user']['telegram_id']).first()
        
        if not user:
            user = User(
                telegram_id=data['user']['telegram_id'],
                username=data['user']['username'],
                is_premium=data['user']['is_premium']
            )
        else:
            user.username = data['user']['username']
            user.is_premium = data['user']['is_premium']

        for task_data in data['forwarding_tasks']:
            task = ForwardingTask(
                user=user,
                source_channel=task_data['source_channel'],
                destination_channel=task_data['destination_channel'],
                is_active=task_data['is_active'],
                filter_keywords=task_data['filter_keywords'],
                replace_keywords=task_data['replace_keywords'],
                begin_text=task_data['begin_text'],
                end_text=task_data['end_text']
            )
            user.forwarding_tasks.append(task)

        return user

