from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from services.auth_service import AuthService
from services.email_service import EmailService

PHONE, OTP, EMAIL, EMAIL_OTP = range(4)

auth_service = AuthService()
email_service = EmailService()

async def start_phone_auth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter your phone number:")
    return PHONE

async def phone_number_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_number = update.message.text
    if auth_service.is_valid_phone_number(phone_number):
        otp = auth_service.generate_otp()
        context.user_data['phone'] = phone_number
        context.user_data['otp'] = otp
        # In a real scenario, you would send this OTP via Telegram's API
        await update.message.reply_text(f"OTP sent to your Telegram account. Please enter the OTP:")
        return OTP
    else:
        await update.message.reply_text("Invalid phone number. Please try again.")
        return PHONE

async def otp_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_otp = update.message.text
    if user_otp == context.user_data['otp']:
        auth_service.authenticate_user(update.effective_user.id, context.user_data['phone'])
        await update.message.reply_text("Phone number verified successfully!")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Invalid OTP. Please try again.")
        return OTP

async def start_email_verification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter your email address:")
    return EMAIL

async def email_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    email = update.message.text
    if auth_service.is_valid_email(email):
        otp = auth_service.generate_otp()
        context.user_data['email'] = email
        context.user_data['email_otp'] = otp
        email_service.send_otp_email(email, otp)
        await update.message.reply_text("OTP sent to your email. Please enter the OTP:")
        return EMAIL_OTP
    else:
        await update.message.reply_text("Invalid email address. Please try again.")
        return EMAIL

async def email_otp_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_otp = update.message.text
    if user_otp == context.user_data['email_otp']:
        auth_service.verify_email(update.effective_user.id, context.user_data['email'])
        await update.message.reply_text("Email verified successfully! Premium features activated.")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Invalid OTP. Please try again.")
        return EMAIL_OTP

