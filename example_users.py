# Это пример responce'a при запросе:
# response = requests.get("https://gorest.co.in/public/v1/users").json()
# print(response)

response_body = {
    'meta': {
        'pagination': {
            'total': 4000,
            'pages': 400,
            'page': 1,
            'limit': 10,
            'links': {
                'previous': None,
                'current': 'https://gorest.co.in/public/v1/users?page=1',
                'next': 'https://gorest.co.in/public/v1/users?page=2'
            }
        }
    },
    'data': [
        {'id': 4075, 'name': 'Rageswari Kaur', 'email': 'kaur_rageswari@mayer.com', 'gender': 'male', 'status': 'active'},
        {'id': 4069, 'name': 'Bilva Kapoor', 'email': 'bilva_kapoor@muller-mckenzie.name', 'gender': 'male', 'status': 'inactive'},
        {'id': 4068, 'name': 'Chandini Patel', 'email': 'chandini_patel@gutmann.biz', 'gender': 'female', 'status': 'inactive'},
        {'id': 4067, 'name': 'Swami Nayar I', 'email': 'i_swami_nayar@dibbert.io', 'gender': 'male', 'status': 'active'},
        {'id': 4066, 'name': 'Aruna Pillai', 'email': 'pillai_aruna@wintheiser.net', 'gender': 'female', 'status': 'inactive'},
        {'id': 4065, 'name': 'Devagya Guneta', 'email': 'guneta_devagya@kautzer.com', 'gender': 'female', 'status': 'active'},
        {'id': 4064, 'name': 'Amogh Johar', 'email': 'johar_amogh@farrell-schiller.name', 'gender': 'male', 'status': 'inactive'},
        {'id': 4063, 'name': 'Bhilangana Sethi', 'email': 'sethi_bhilangana@hartmann.org', 'gender': 'female', 'status': 'inactive'},
        {'id': 4062, 'name': 'Sujata Namboothiri', 'email': 'namboothiri_sujata@connelly.io', 'gender': 'male', 'status': 'inactive'},
        {'id': 4061, 'name': 'Menaka Mahajan', 'email': 'mahajan_menaka@crooks-deckow.biz', 'gender': 'male', 'status': 'active'}]
}
