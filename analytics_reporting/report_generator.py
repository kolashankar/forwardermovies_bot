import matplotlib.pyplot as plt
import io
from .user_activity_tracker import UserActivityTracker
from .performance_metrics import PerformanceMetrics

class ReportGenerator:
    @staticmethod
    def generate_user_activity_report(days: int = 30):
        activity_summary = UserActivityTracker.get_activity_summary(days)
        
        # Create a pie chart
        labels = [item['activity_type'] for item in activity_summary]
        sizes = [item['count'] for item in activity_summary]
        
        plt.figure(figsize=(10, 10))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(f'User Activity Summary (Last {days} days)')
        
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        
        return img_buffer

    @staticmethod
    def generate_performance_report(days: int = 30):
        success_rate = PerformanceMetrics.get_forwarding_success_rate(days)
        avg_forwarding_time = PerformanceMetrics.get_average_forwarding_time(days)
        busiest_hours = PerformanceMetrics.get_busiest_hours(days)
        error_rate = PerformanceMetrics.get_error_rate(days)
        
        report = f"""
        Performance Report (Last {days} days)
        
        Forwarding Success Rate: {success_rate:.2f}%
        Average Forwarding Time: {avg_forwarding_time:.2f} seconds
        Error Rate: {error_rate:.2f}%
        
        Busiest Hours:
        """
        
        for hour in busiest_hours:
            report += f"  {hour['hour']}:00 - {hour['total_forwards']} forwards\n"
        
        return report

    @staticmethod
    def generate_retention_report(cohort_days: int = 30, retention_days: int = 7):
        retention_data = UserActivityTracker.get_user_retention(cohort_days, retention_days)
        
        report = f"""
        User Retention Report
        
        Cohort: Users who joined {cohort_days} days ago
        Retention Period: {retention_days} days
        
        Cohort Size: {retention_data['cohort_size']}
        Retained Users: {retention_data['retained_users']}
        Retention Rate: {retention_data['retention_rate']:.2f}%
        """
        
        return report

