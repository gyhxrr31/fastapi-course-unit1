from tasks.celery_config import celery
from PIL import Image
from loguru import logger
from pathlib import Path

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