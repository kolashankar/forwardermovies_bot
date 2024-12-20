from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from config import config

class SchedulerService:
    def __init__(self):
        jobstores = {
            'default': SQLAlchemyJobStore(url=config.DATABASE_URL)
        }
        executors = {
            'default': ThreadPoolExecutor(20)
        }
        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }
        self.scheduler = AsyncIOScheduler(
            jobstores=jobstores,
            executors=executors,
            job_defaults=job_defaults
        )

    def start(self):
        self.scheduler.start()

    def add_job(self, func, trigger, **kwargs):
        return self.scheduler.add_job(func, trigger, **kwargs)

    def remove_job(self, job_id):
        self.scheduler.remove_job(job_id)

    def get_jobs(self):
        return self.scheduler.get_jobs()

scheduler_service = SchedulerService()

