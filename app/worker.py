from celery import Celery
import os

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

@celery.task(name="celery_print")
def celery_logger(text: str, code: str):
    with open('log.txt', 'w') as f:
        log = f"{text} - code: {code}"
        f.write(log)
        print(log)
    print(text)
