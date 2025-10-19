from config import env_config
from tasks.celery_config import celery
from PIL import Image
from loguru import logger
from pathlib import Path
from pydantic import EmailStr
import smtplib

from tasks.email_templates import create_booking_confirmation_template


@celery.task
def process_pic(
        path: str
):
    logger.info("Processing image")
    image_path = Path(path)
    image = Image.open(image_path)
    image_resized_1000_500 = image.resize(size=(1000, 500))
    image_resized_200_100 = image.resize(size=(200, 100))
    image_resized_1000_500.save(f"statics/images/resized_1000_500{image_path.name}")
    image_resized_200_100.save(f"statics/images/resized_200_100{image_path.name}")


@celery.task
def send_booking_confirmation_email(
        booking: dict,
        email_to: EmailStr
):
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(env_config.SMTP_HOST, env_config.SMTP_PORT) as server:
        server.login(env_config.SMTP_USER, env_config.SMTP_PWD)
        server.send_message(msg_content)