from fastapi import UploadFile, APIRouter
from tasks.tasks import process_pic
import shutil

router = APIRouter()


@router.post("/hotels")
async def add_hotel_image(
        file: UploadFile,
        name: int
):
    image_path = f"statics/images/{name}.webp"
    with open(f"statics/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(image_path)