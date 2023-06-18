import requests
import data
import configuration

user_body = {
    "firstName": "Иван",
    "email": "testem2@gmg.com",
    "phone": "+79994445566",
    "comment": "Ребёнок спит, не шумите",
    "address": "г. Москва, ул. Хохотушкина, д. 16",
    # "Authorization": ""
}

user_products = {
    "name": "Мой набор",
    "user": user_body,
    "card": {
        "name": "Под ситуацию"
    },
    "productsList": [
        {
            "id": 1,
            "name": "Икра красная Белое море",
            "price": 45,
            "weight": 5,
            "units": "кг",
            "quantity": 2
        }
    ],
    "productsCount": 1
}
url = "https://b759ac70-e249-43b0-b1c9-797c0f21edbe.serverhub.praktikum-services.ru/api/v1/users"

res = requests.post(url, json=user_body)

if res.status_code == 201 or res.status_code == 200:
    token = res.json().get("authToken")
    print(f"Сохранили токен: {token}")
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {token}"}

    # Вот тут не понятно, почему есть передавать токен в postman и такое тело работает все, а через код мне пишут что не все поля добавлены?Помогите пожалуйста (
    # user_products["user"]["Authorization"] = f"Bearer {token}"
    # print(user_products)

    r = requests.post(url, json=user_products, headers=headers)
    print("Response_body: ", r.json(), " error ", r.status_code)
else:
    print(f"Случилась ошибка: {res.status_code}")
