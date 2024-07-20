#Конечно! Давайте изменим код, чтобы он выводил информацию о первых трех породах
# кошек, включая их идентификаторы и ссылки на изображения.


from config import the_cat_api_key
import requests

def get_cat_breeds():
    """
    Получает список всех пород кошек.
    """
    url = "https://api.thecatapi.com/v1/breeds"
    headers = {"x-api-key": the_cat_api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def get_cat_image_by_breed(breed_id):
    """
    Получает изображение кошки по идентификатору породы.
    """
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}"
    headers = {"x-api-key": the_cat_api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['url']
    return None

def main():
    breeds = get_cat_breeds()
    for breed in breeds[:3]:  # Показать первые три породы
        breed_id = breed['id']
        breed_name = breed['name']
        image_url = get_cat_image_by_breed(breed_id)
        print(f"Порода: {breed_name}")
        print(f"ID: {breed_id}")
        if image_url:
            print(f"Изображение: {image_url}")
        else:
            print(f"Не удалось получить изображение для породы {breed_name}.")
        print()

if __name__ == "__main__":
    main()


#Объяснение кода:

#1. **get_cat_breeds**: Функция для получения списка всех пород кошек.
#2. **get_cat_image_by_breed**: Функция для получения изображения кошки по идентификатору породы.
#3. **main**: Главная функция, которая выводит информацию о первых трех породах кошек, включая их идентификаторы и ссылки на изображения.

#Запустите этот скрипт, и он выведет информацию о первых трех породах кошек.
# Если изображение для какой-либо породы не удалось получить, будет выведено
# соответствующее сообщение.

