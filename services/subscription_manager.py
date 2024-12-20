from models.user import User
from models.subscription_plan import SubscriptionPlan

class SubscriptionManager:
    @staticmethod
    def change_subscription(user: User, new_plan: SubscriptionPlan):
        user.subscription_plan = new_plan
        user.is_premium = new_plan.name != 'Free'
        
        # Adjust user's forwarding tasks if necessary
        if len(user.forwarding_tasks) > new_plan.max_incoming_channels:
            excess_tasks = user.forwarding_tasks[new_plan.max_incoming_channels:]
            for task in excess_tasks:
                user.forwarding_tasks.remove(task)

    @staticmethod
    def can_add_channel(user: User, channel_type: str):
        if channel_type == 'incoming':
            return len(user.get_incoming_channels()) < user.subscription_plan.max_incoming_channels
        elif channel_type == 'outgoing':
            return len(user.get_outgoing_channels()) < user.subscription_plan.max_outgoing_channels
        return False

    @staticmethod
    def can_forward_message(user: User):
        if user.subscription_plan.max_messages_per_day == -1:  # Unlimited
            return True
        
        today_stats = user.get_today_stats()
        return today_stats.messages_forwarded < user.subscription_plan.max_messages_per_day

    @staticmethod
    def upgrade_to_premium(user: User):
        premium_plan = SubscriptionPlan.get_premium_plan()
        SubscriptionManager.change_subscription(user, premium_plan)
        return True

    @staticmethod
    def downgrade_to_free(user: User):
        free_plan = SubscriptionPlan.get_free_plan()
        SubscriptionManager.change_subscription(user, free_plan)
        return True

