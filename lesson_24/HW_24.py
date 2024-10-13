import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

logging.basicConfig(level=logging.INFO, filename='test_search.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

@pytest.fixture(scope='class')
def authenticated_session():
    session = requests.Session()
    auth_url = "http://127.0.0.1:8080/auth"
    auth_data = {"username": "test_user", "password": "test_pass"}

    response = session.post(auth_url, auth=HTTPBasicAuth(auth_data['username'], auth_data['password']))

    if response.status_code == 200:
        access_token = response.json().get('access_token')
        session.headers.update({'Authorization': f'Bearer {access_token}'})
        logger.info("Аутентифікація пройшла успішно")
    else:
        logger.error(f"Аутентифікація не вдалася: {response.status_code} - {response.text}")
        pytest.fail("Аутентифікація не вдалася")

    return session


# Параметризація для різних запитів з параметрами sort_by і limit
@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 7),
    ("engine_volume", 3),
    ("brand", 10),
    (None, 5),
    ("year", None),
    (None, None),
])
def test_search_cars(authenticated_session, sort_by, limit):
    search_url = "http://127.0.0.1:8080/cars"

    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    response = authenticated_session.get(search_url, params=params)

    assert response.status_code == 200, f"Помилка запиту: {response.status_code} - {response.text}"

    cars = response.json()
    logger.info(f"Запит: sort_by={sort_by}, limit={limit}")
    logger.info(f"Отримано {len(cars)} записів: {cars}")

    for car in cars:
        assert "brand" in car
        assert "year" in car
        assert "engine_volume" in car
        assert "price" in car