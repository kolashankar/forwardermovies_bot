from models.forwarding_task import ForwardingTask
from models.forwarding_stats import ForwardingStats
from datetime import datetime, timedelta

class PerformanceMetrics:
    @staticmethod
    def get_forwarding_success_rate(days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        stats = ForwardingStats.objects.filter(date__gte=start_date)
        total_attempts = stats.aggregate(models.Sum('total_attempts'))['total_attempts__sum'] or 0
        successful_forwards = stats.aggregate(models.Sum('successful_forwards'))['successful_forwards__sum'] or 0
        
        return (successful_forwards / total_attempts) * 100 if total_attempts > 0 else 0

    @staticmethod
    def get_average_forwarding_time(days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        stats = ForwardingStats.objects.filter(date__gte=start_date)
        return stats.aggregate(models.Avg('average_forwarding_time'))['average_forwarding_time__avg'] or 0

    @staticmethod
    def get_busiest_hours(days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        stats = ForwardingStats.objects.filter(date__gte=start_date)
        return stats.values('hour').annotate(
            total_forwards=models.Sum('successful_forwards')
        ).order_by('-total_forwards')[:5]

    @staticmethod
    def get_most_active_channels(limit: int = 10, days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        return ForwardingTask.objects.filter(last_forwarded__gte=start_date).values('source_channel').annotate(
            total_forwards=models.Sum('forwarding_stats__successful_forwards')
        ).order_by('-total_forwards')[:limit]

    @staticmethod
    def get_error_rate(days: int = 30):
        start_date = datetime.now() - timedelta(days=days)
        stats = ForwardingStats.objects.filter(date__gte=start_date)
        total_attempts = stats.aggregate(models.Sum('total_attempts'))['total_attempts__sum'] or 0
        failed_forwards = stats.aggregate(models.Sum('failed_forwards'))['failed_forwards__sum'] or 0
        
        return (failed_forwards / total_attempts) * 100 if total_attempts > 0 else 0

