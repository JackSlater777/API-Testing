from pydantic import BaseModel
from pydantic import validator
# from pydantic import Field


# Schema: {'id': 1, 'title': 'Post 1'}


class Post(BaseModel):
    id: int
    # id: int = Field(le=2)  # Позволяет удалить валидатор под декоратором, см. метод Field
    title: str
    # Если значение начинается с нижнего подчеркивания (приват), то:
    # name: str = Field(alias="_name")

    # Отдельный метод валидации из pydantic (можно заменить на le=2)
    @validator('id')
    def check_id_is_less_than_two(cls, v):
        if v > 2:
            raise ValueError('id is not less than two')
        else:
            return v
