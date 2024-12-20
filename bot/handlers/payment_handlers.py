from telegram import Update, LabeledPrice
from telegram.ext import CallbackContext
from services.payment.stripe_service import StripeService
from models.user import User
from models.subscription_plan import SubscriptionPlan

stripe_service = StripeService()

def start_payment(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if user.is_premium:
        update.message.reply_text("You are already a premium user!")
        return
    
    premium_plan = SubscriptionPlan.get_premium_plan()
    
    context.bot.send_invoice(
        chat_id=user_id,
        title="Premium Subscription",
        description="Upgrade to premium for advanced features",
        payload="premium_subscription",
        provider_token=stripe_service.get_provider_token(),
        currency="INR",
        prices=[LabeledPrice("Premium Plan", premium_plan.price * 100)],  # Amount in cents
        start_parameter="premium-subscription"
    )

def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
    if query.invoice_payload != 'premium_subscription':
        query.answer(ok=False, error_message="Something went wrong...")
    else:
        query.answer(ok=True)

def successful_payment_callback(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    premium_plan = SubscriptionPlan.get_premium_plan()
    user.upgrade_to_premium(premium_plan)
    
    update.message.reply_text("Thank you for your payment. You are now a premium user!")

