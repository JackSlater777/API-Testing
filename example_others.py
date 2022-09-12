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
