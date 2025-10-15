from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from routers.hotels.router import get_hotels_by_name

router = APIRouter()

templates = Jinja2Templates(directory="pages/templates")

@router.get("/hotels")
async def get_hotel_page(
        request: Request,
        hotels = Depends(get_hotels_by_name)
):
    return templates.TemplateResponse(
        name="hotels.html",
        context={"request": request, "hotels": hotels}
    )