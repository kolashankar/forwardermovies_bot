from telegram.ext import CommandHandler, CallbackQueryHandler
from .command_handlers import handle_command
from .callback_handlers import handle_callback_query

class CommandRegistry:
    def __init__(self):
        self.handlers = []

    def register_commands(self):
        self.handlers.extend([
            CommandHandler(['start', 'features', 'config', 'help', 'incoming', 'outgoing', 
                            'remove_incoming', 'begin_autoforwarder', 'stop', 'remove_keywords', 
                            'replace_keywords', 'remove_replacekeywords', 'blacklist', 
                            'remove_blacklist', 'begin_text', 'end_text', 'remove_endtext', 
                            'time_scheduler', 'remove_slots', 'disconnect', 'status', 
                            'templates', 'filters', 'analytics', 'translate', 'watermark', 
                            'backup', 'captions'], handle_command),
            CallbackQueryHandler(handle_callback_query)
        ])

    def get_handlers(self):
        return self.handlers

