from pydantic import BaseModel, conint
from pydantic import HttpUrl  # Проверяет Url
from players.src.enums.player_enums import Statuses
from typing import Optional


class Country(BaseModel):
    """Класс для описания структуры никнейма."""
    UA: conint(strict=True)  # Чтобы избежать конвертации строки в число pydantic'oм


class Language(BaseModel):
    """Класс для описания структуры перевода."""
    nickname: str
    countries: Optional[Country]


class Localize(BaseModel):
    """Класс для описания структуры локализации."""
    en: Language
    ru: Language


class Player(BaseModel):
    """Класс для описания структуры игрока."""
    account_status: Statuses
    balance: conint(strict=True)  # Чтобы избежать конвертации строки в число pydantic'oм
    localize: Localize
    avatar: HttpUrl
