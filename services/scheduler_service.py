from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from models.forwarding_task import ForwardingTask
from services.forwarding.message_forwarder import MessageForwarder

class SchedulerService:
    def __init__(self, bot):
        self.scheduler = BackgroundScheduler()
        self.message_forwarder = MessageForwarder(bot)

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()

    def add_task(self, task: ForwardingTask):
        job_id = f"task_{task.id}"
        self.scheduler.add_job(
            self.message_forwarder.forward_messages,
            CronTrigger.from_crontab(task.schedule),
            id=job_id,
            args=[task],
            replace_existing=True
        )

    def remove_task(self, task_id: int):
        job_id = f"task_{task_id}"
        self.scheduler.remove_job(job_id)

    def update_task(self, task: ForwardingTask):
        self.remove_task(task.id)
        self.add_task(task)

    def get_task_schedule(self, task_id: int):
        job_id = f"task_{task_id}"
        job = self.scheduler.get_job(job_id)
        return job.trigger.expression if job else None

    def set_schedule(self, user, schedule):
        for task in user.forwarding_tasks:
            task.schedule = schedule
            self.update_task(task)

    def clear_schedule(self, user):
        for task in user.forwarding_tasks:
            self.remove_task(task.id)
            task.schedule = None

