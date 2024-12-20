from models.forwarding_stats import ForwardingStats
from models.user import User
from datetime import datetime, timedelta

class AnalyticsService:
    @staticmethod
    def get_user_stats(user_id, days=30):
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        stats = ForwardingStats.query.filter(
            ForwardingStats.user_id == user_id,
            ForwardingStats.date >= start_date,
            ForwardingStats.date <= end_date
        ).all()
        
        total_messages = sum(stat.messages_forwarded for stat in stats)
        daily_average = total_messages / days if days > 0 else 0
        
        return {
            'total_messages': total_messages,
            'daily_average': daily_average,
            'days_analyzed': days
        }

    @staticmethod
    def get_overall_stats(days=30):
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        stats = ForwardingStats.query.filter(
            ForwardingStats.date >= start_date,
            ForwardingStats.date <= end_date
        ).all()
        
        total_messages = sum(stat.messages_forwarded for stat in stats)
        total_users = User.query.count()
        active_users = ForwardingStats.query.filter(
            ForwardingStats.date >= start_date,
            ForwardingStats.date <= end_date
        ).distinct(ForwardingStats.user_id).count()
        
        return {
            'total_messages': total_messages,
            'total_users': total_users,
            'active_users': active_users,
            'days_analyzed': days
        }

    @staticmethod
    def get_user_activity(user_id, days=30):
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=days)
        
        stats = ForwardingStats.query.filter(
            ForwardingStats.user_id == user_id,
            ForwardingStats.date >= start_date,
            ForwardingStats.date <= end_date
        ).order_by(ForwardingStats.date).all()
        
        activity = [{'date': stat.date, 'messages': stat.messages_forwarded} for stat in stats]
        
        return activity

