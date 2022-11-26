from pydantic import BaseModel, conint
from pydantic import EmailStr  # Проверяет email
from users.src.enums.user_enums import Genders, Statuses


class User(BaseModel):
    """Класс для описания структуры пользователя."""
    id: conint(strict=True)  # Чтобы избежать конвертации строки в число pydantic'oм
    name: str
    email: EmailStr
    gender: Genders
    status: Statuses
