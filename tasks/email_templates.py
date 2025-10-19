from email.message import EmailMessage
from pydantic import EmailStr
from config import env_config

def create_booking_confirmation_template(
        booking: dict,
        email_to: EmailStr
):
    email = EmailMessage()
    email["Subject"] = "Подтверждение бронирования"
    email["From"] = env_config.SMTP_USER
    email["To"] = email_to

    email.set_content(
    f"""
        <h1>Подтвердите бронирование</h1>
        <p1>Вы забронировали отель {booking["date_from"]} по {booking["date_to"]}</p1>
        """,
    subtype="html"
    )
    return email
