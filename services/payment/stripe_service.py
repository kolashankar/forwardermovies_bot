import stripe
from config.config import STRIPE_API_KEY, STRIPE_WEBHOOK_SECRET

stripe.api_key = STRIPE_API_KEY

class StripeService:
    @staticmethod
    def create_checkout_session(user_id, plan_id):
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': plan_id,
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='https://example.com/cancel',
                client_reference_id=str(user_id),
            )
            return checkout_session.id
        except Exception as e:
            print(f"Error creating checkout session: {str(e)}")
            return None

    @staticmethod
    def handle_webhook(payload, sig_header):
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, STRIPE_WEBHOOK_SECRET
            )
            
            if event['type'] == 'checkout.session.completed':
                session = event['data']['object']
                user_id = session.get('client_reference_id')
                if user_id:
                    # Update user's subscription status
                    pass
            
            return True
        except stripe.error.SignatureVerificationError:
            print("Invalid signature")
            return False
        except Exception as e:
            print(f"Error handling webhook: {str(e)}")
            return False

    @staticmethod
    def cancel_subscription(subscription_id):
        try:
            stripe.Subscription.delete(subscription_id)
            return True
        except Exception as e:
            print(f"Error cancelling subscription: {str(e)}")
            return False

