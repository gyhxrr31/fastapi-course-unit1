from fastapi import UploadFile, APIRouter
import shutil

router = APIRouter()


@router.post("/hotels")
async def add_hotel_image(
        file: UploadFile,
        name: int
):
    with open(f"statics/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
