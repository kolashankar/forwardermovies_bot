from telegram import Update
from telegram.ext import ContextTypes

async def begin_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Set beginning text.")

async def end_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Set ending text.")

async def remove_endtext(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Remove ending text.")

