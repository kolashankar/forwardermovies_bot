from telegram import Update
from telegram.ext import ContextTypes

async def incoming(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Set up incoming channel.")

async def outgoing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Set up outgoing channel.")

async def remove_incoming(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Remove incoming channel.")

async def begin_autoforwarder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Start auto-forwarding.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Stop auto-forwarding.")

