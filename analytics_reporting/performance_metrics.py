from sqlalchemy import func
from models.forwarding_task import ForwardingTask
from models.forwarding_stats import ForwardingStats
from datetime import datetime, timedelta

class PerformanceMetrics:
    @staticmethod
    def get_forwarding_success_rate(days: int = 30):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        stats = ForwardingStats.query.filter(ForwardingStats.date >= start_date, ForwardingStats.date <= end_date)
        total_attempts = stats.with_entities(func.sum(ForwardingStats.total_attempts)).scalar() or 0
        successful_forwards = stats.with_entities(func.sum(ForwardingStats.successful_forwards)).scalar() or 0
        
        return (successful_forwards / total_attempts) * 100 if total_attempts > 0 else 0

    @staticmethod
    def get_average_forwarding_time(days: int = 30):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        stats = ForwardingStats.query.filter(ForwardingStats.date >= start_date, ForwardingStats.date <= end_date)
        return stats.with_entities(func.avg(ForwardingStats.average_forwarding_time)).scalar() or 0

    @staticmethod
    def get_busiest_hours(days: int = 30):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        stats = ForwardingStats.query.filter(ForwardingStats.date >= start_date, ForwardingStats.date <= end_date)
        return stats.with_entities(
            ForwardingStats.hour,
            func.sum(ForwardingStats.successful_forwards).label('total_forwards')
        ).group_by(ForwardingStats.hour).order_by(func.sum(ForwardingStats.successful_forwards).desc()).limit(5).all()

    @staticmethod
    def get_most_active_channels(limit: int = 10, days: int = 30):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        return ForwardingTask.query.join(ForwardingStats).filter(
            ForwardingTask.last_forwarded >= start_date
        ).with_entities(
            ForwardingTask.source_channel,
            func.sum(ForwardingStats.successful_forwards).label('total_forwards')
        ).group_by(ForwardingTask.source_channel).order_by(func.sum(ForwardingStats.successful_forwards).desc()).limit(limit).all()

    @staticmethod
    def get_error_rate(days: int = 30):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        stats = ForwardingStats.query.filter(ForwardingStats.date >= start_date, ForwardingStats.date <= end_date)
        total_attempts = stats.with_entities(func.sum(ForwardingStats.total_attempts)).scalar() or 0
        failed_forwards = stats.with_entities(func.sum(ForwardingStats.failed_forwards)).scalar() or 0
        
        return (failed_forwards / total_attempts) * 100 if total_attempts > 0 else 0

