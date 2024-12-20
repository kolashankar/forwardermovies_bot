from telegram import Update
from telegram.ext import CallbackContext
from .basic_commands import start, features, config, help_command
from .channel_commands import incoming, outgoing, remove_incoming, begin_autoforwarder, stop
from .filter_commands import remove_keywords, replace_keywords, remove_replacekeywords, blacklist, remove_blacklist
from .text_commands import begin_text, end_text, remove_endtext
from .scheduler_commands import time_scheduler, remove_slots, disconnect, status
from .advanced_commands import handle_advanced_command

def handle_command(update: Update, context: CallbackContext):
    command = update.message.text.split()[0][1:].lower()
    
    command_handlers = {
        'start': start,
        'features': features,
        'config': config,
        'help': help_command,
        'incoming': incoming,
        'outgoing': outgoing,
        'remove_incoming': remove_incoming,
        'begin_autoforwarder': begin_autoforwarder,
        'stop': stop,
        'remove_keywords': remove_keywords,
        'replace_keywords': replace_keywords,
        'remove_replacekeywords': remove_replacekeywords,
        'blacklist': blacklist,
        'remove_blacklist': remove_blacklist,
        'begin_text': begin_text,
        'end_text': end_text,
        'remove_endtext': remove_endtext,
        'time_scheduler': time_scheduler,
        'remove_slots': remove_slots,
        'disconnect': disconnect,
        'status': status
    }
    
    if command in command_handlers:
        command_handlers[command](update, context)
    else:
        handle_advanced_command(update, context)

