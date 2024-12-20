from models.user import User
from models.subscription_plan import SubscriptionPlan
from services.subscription_manager import SubscriptionManager

class Subscription:
    def __init__(self):
        self.subscription_manager = SubscriptionManager()

    def upgrade_user(self, user_id: int):
        user = User.get_by_id(user_id)
        if user:
            premium_plan = SubscriptionPlan.get_premium_plan()
            self.subscription_manager.change_subscription(user, premium_plan)
            return True
        return False

    def downgrade_user(self, user_id: int):
        user = User.get_by_id(user_id)
        if user:
            free_plan = SubscriptionPlan.get_free_plan()
            self.subscription_manager.change_subscription(user, free_plan)
            return True
        return False

    def get_user_subscription(self, user_id: int):
        user = User.get_by_id(user_id)
        if user:
            return user.subscription_plan
        return None

