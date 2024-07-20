#Конечно! Давайте напишем тесты, которые будут проверять функции `get_cat_breeds`
# и `get_cat_image_by_breed`, используя библиотеки `pytest` и `pytest-mock`.
#1. Установите необходимые библиотеки, если они еще не установлены:
#2. Создайте файл теста, например `test.py`:


# test.py
import pytest
import requests
from main1 import get_cat_breeds, get_cat_image_by_breed

def test_get_cat_breeds_success(mocker):
    # Создаем мок-объект для requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"id": "abys", "name": "Abyssinian"},
        {"id": "aege", "name": "Aegean"},
        {"id": "abob", "name": "American Bobtail"}
    ]

    # Настраиваем мок так, чтобы он использовался вместо requests.get
    mocker.patch("requests.get", return_value=mock_response)

    # Вызываем тестируемую функцию
    result = get_cat_breeds()

    # Проверяем, что результат соответствует ожидаемым данным
    assert result == [
        {"id": "abys", "name": "Abyssinian"},
        {"id": "aege", "name": "Aegean"},
        {"id": "abob", "name": "American Bobtail"}
    ]

def test_get_cat_image_by_breed_success(mocker):
    breed_id = "abys"
    expected_image_url = "https://example.com/cat_image.jpg"

    # Создаем мок-объект для requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"url": expected_image_url}
    ]

    # Настраиваем мок так, чтобы он использовался вместо requests.get
    mocker.patch("requests.get", return_value=mock_response)

    # Вызываем тестируемую функцию
    result = get_cat_image_by_breed(breed_id)

    # Проверяем, что результат соответствует ожидаемому URL
    assert result == expected_image_url

# Объяснение кода теста

#1. **Импортируем необходимые модули:** Мы импортируем `pytest`, `requests`
# и тестируемые функции `get_cat_breeds` и `get_cat_image_by_breed`.

#2. **Тест для `get_cat_breeds`:**
 #  - Создаем мок-объект для `requests.get`, который возвращает статус-код 200 и JSON с данными о породах.
  # - Настраиваем мок так, чтобы он использовался вместо `requests.get`.
   #- Вызываем функцию `get_cat_breeds` и проверяем, что результат соо
    # тветствует ожидаемым данным.

#3. **Тест для `get_cat_image_by_breed`:**
   #- Создаем мок-объект для `requests.get`, который возвращает статус-код 200 и JSON с URL изображения.
   #- Настраиваем мок так, чтобы он использовался вместо `requests.get`.
   #- Вызываем функцию `get_cat_image_by_breed` и проверяем, что результат соответствует ожидаемому URL.

#Теперь вы можете запустить тесты



#Если все настроено правильно, тесты должны пройти успешно, указывая на то, что функции
# `get_cat_breeds` и `get_cat_image_by_breed` корректно обрабатывают успешные HTTP-запросы
# и возвращают правильные данные.

