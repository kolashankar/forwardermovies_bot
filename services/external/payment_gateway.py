import stripe
from config.settings import Settings

class PaymentGateway:
    def __init__(self):
        self.settings = Settings()
        stripe.api_key = self.settings.STRIPE_API_KEY

    def create_checkout_session(self, user_id, price_id):
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=str(user_id),
                success_url=f"{self.settings.WEBHOOK_URL}/payment/success?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=f"{self.settings.WEBHOOK_URL}/payment/cancel",
                payment_method_types=["card"],
                mode="subscription",
                line_items=[{
                    "price": price_id,
                    "quantity": 1
                }]
            )
            return checkout_session
        except Exception as e:
            print(f"Error creating checkout session: {str(e)}")
            return None

    def handle_webhook(self, payload, sig_header):
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, self.settings.STRIPE_WEBHOOK_SECRET
            )

            if event['type'] == 'checkout.session.completed':
                session = event['data']['object']
                self.handle_successful_payment(session)
            elif event['type'] == 'customer.subscription.deleted':
                subscription = event['data']['object']
                self.handle_subscription_cancelled(subscription)

            return True
        except Exception as e:
            print(f"Error handling webhook: {str(e)}")
            return False

    def handle_successful_payment(self, session):
        user_id = session['client_reference_id']
        # Update user's premium status in the database
        # You may want to use your DatabaseService here
        print(f"User {user_id} has successfully subscribed to premium")

    def handle_subscription_cancelled(self, subscription):
        user_id = subscription['client_reference_id']
        # Update user's premium status in the database
        # You may want to use your DatabaseService here
        print(f"User {user_id} has cancelled their premium subscription")

    def cancel_subscription(self, subscription_id):
        try:
            cancelled_subscription = stripe.Subscription.delete(subscription_id)
            return cancelled_subscription
        except Exception as e:
            print(f"Error cancelling subscription: {str(e)}")
            return None

payment_gateway = PaymentGateway()

