from models.user import User
from models.activity_log import ActivityLog
from datetime import datetime, timedelta

class UserActivityTracker:
    @staticmethod
    def log_activity(user: User, activity_type: str, details: str = None):
        ActivityLog.objects.create(
            user=user,
            activity_type=activity_type,
            details=details
        )

    @staticmethod
    def get_user_activity(user: User, days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        return ActivityLog.objects.filter(user=user, timestamp__gte=start_date).order_by('-timestamp')

    @staticmethod
    def get_most_active_users(limit: int = 10, days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        return User.objects.annotate(
            activity_count=models.Count('activitylog', filter=models.Q(activitylog__timestamp__gte=start_date))
        ).order_by('-activity_count')[:limit]

    @staticmethod
    def get_activity_summary(days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        return ActivityLog.objects.filter(timestamp__gte=start_date).values('activity_type').annotate(
            count=models.Count('id')
        ).order_by('-count')

    @staticmethod
    def get_user_retention(cohort_days: int = 30, retention_days: int = 7):
        cohort_start = datetime.now() - timedelta(days=cohort_days)
        cohort_end = cohort_start + timedelta(days=retention_days)
        retention_date = datetime.now() - timedelta(days=retention_days)

        cohort = User.objects.filter(date_joined__range=(cohort_start, cohort_end))
        retained = cohort.filter(last_login__gte=retention_date)

        return {
            'cohort_size': cohort.count(),
            'retained_users': retained.count(),
            'retention_rate': (retained.count() / cohort.count()) * 100 if cohort.count() > 0 else 0
        }

