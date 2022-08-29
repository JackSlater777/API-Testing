# Пример объекта на котором вы можете потренироваться, используя pydantic схемы.
# Example of object for training with pydantic schemas.

player = {
    "account_status": "active",
    "balance": 10,
    "localize": {
        "en": {"nickname": "SolveMe", "countries": {"UA": 3}},
        "ru": {"nickname": "СолвМи"}
    },
    "avatar": "https://google.com"
}

z = {
    "meta": {
        "pagination": {
            "total": 1725,
            "pages": 87,
            "page": 1,
            "limit": 20,
            "links": {
            }
        }
    },
    "data": {
        {
            "id": 1753,
            "name": "API Monitoring:5y3",
            "email": "apimonitoring5y3at@synthetic.com",
            "gender": "femail",
            "status": "inactive"
        }
    }
}

POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'title': {'type': 'string'}
    },
    'required': ['id']
}

# {'id': 1, 'title': 'Post 1'}

computer = {
    "id": 21,
    "status": "ACTIVE",
    "activated_at": "2013-06-01",
    "expiration_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": 'green',
            "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
        },
        "owners": [{
            "name": "Stephan Nollan",
            "card_number": "4000000000000002",
            "email": "shtephan.nollan@gmail.com",
        }]
    }
}
