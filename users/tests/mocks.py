from users.src.schemas.user import User
from users.src.enums.user_enums import Genders, Statuses


mock_user = {
    'id': 2,
    'name': 'Ivan',
    'email': 'myemail@gmail.com',
    'gender': 'female',
    'status': 'inactive'
}

validated_mock_user = User(
    id=2,
    name='Ivan',
    email='myemail@gmail.com',
    gender=Genders.female.value,
    status=Statuses.inactive.value
)

invalid_mock_user = {
    'id': 2,
    'name': 'Ivan',
    'email': 'myemailgmail.com',
    'gender': 'female',
    'status': 'inactive'
}
