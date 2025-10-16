from config import env_config
from celery import Celery

celery = Celery(
    "tasks",
    broker=env_config.REDIS_URL,
    include=["tasks.tasks"]
)