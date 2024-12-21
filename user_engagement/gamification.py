from models.user import User

class Gamification:
    @staticmethod
    def award_points(user: User, action: str, points: int):
        if action in user.point_actions:
            user.points += points
            user.save()
            return True
        return False

    @staticmethod
    def get_leaderboard(limit: int = 10):
        return User.objects.order_by('-points')[:limit]

    @staticmethod
    def get_user_rank(user: User):
        return User.objects.filter(points__gt=user.points).count() + 1

    @staticmethod
    def get_next_achievement(user: User):
        achievements = [
            {'name': 'Beginner', 'points': 100},
            {'name': 'Intermediate', 'points': 500},
            {'name': 'Advanced', 'points': 1000},
            {'name': 'Expert', 'points': 5000},
            {'name': 'Master', 'points': 10000}
        ]
        
        for achievement in achievements:
            if user.points < achievement['points']:
                return achievement
        return None

    @staticmethod
    def check_level_up(user: User):
        levels = [0, 100, 250, 500, 1000, 2000, 5000, 10000]
        current_level = user.level
        new_level = next((i for i, points in enumerate(levels) if user.points < points), len(levels)) - 1
        
        if new_level > current_level:
            user.level = new_level
            user.save()
            return True
        return False

python_file="forwarder_bot/user_engagement/feedback_collector.py"
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

class FeedbackCollector:
    def __init__(self, bot):
        self.bot = bot

    async def request_feedback(self, chat_id, message_id):
        keyboard = [
            [
                InlineKeyboardButton("👍", callback_data="feedback_positive"),
                InlineKeyboardButton("👎", callback_data="feedback_negative")
            ],
            [InlineKeyboardButton("💬 Leave a comment", callback_data="feedback_comment")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await self.bot.send_message(chat_id=chat_id, text="How was your experience? Please provide feedback:", reply_markup=reply_markup)

    async def handle_feedback(self, update, context):
        query = update.callback_query
        await query.answer()

        if query.data == "feedback_positive":
            await self.save_feedback(query.from_user.id, "positive")
            await query.edit_message_text(text="Thank you for your positive feedback!")
        elif query.data == "feedback_negative":
            await self.save_feedback(query.from_user.id, "negative")
            await query.edit_message_text(text="We're sorry to hear that. How can we improve?")
        elif query.data == "feedback_comment":
            await query.edit_message_text(text="Please type your feedback comment:")
            context.user_data['awaiting_feedback'] = True

    async def save_feedback(self, user_id, feedback_type, comment=None):
        # Save feedback to database or file
        # This is a placeholder implementation
        print(f"Feedback from user {user_id}: Type: {feedback_type}, Comment: {comment}")

    def add_handler(self, dispatcher):
        dispatcher.add_handler(CallbackQueryHandler(self.handle_feedback, pattern="^feedback_"))

