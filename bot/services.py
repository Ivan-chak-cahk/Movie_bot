import requests
from config import KINOPOISK_API_KEY  # Импортируем API-ключ из конфига


class KinopoiskAPI:
    # Базовый URL для API Kinopoisk (версия 1.4)
    BASE_URL = "https://api.kinopoisk.dev/v1.4/"

    def __init__(self, api_key):
        self.api_key = api_key
        # Заголовки для запросов (с API-ключом)
        self.headers = {"X-API-KEY": self.api_key}

    def search_movie(self, title, limit=5):
        """Поиск фильмов по названию"""
        url = f"{self.BASE_URL}movie/search"
        params = {
            "page": 1,  # Пагинация (первая страница)
            "limit": limit,  # Лимит результатов (по умолчанию 5)
            "query": title,  # Поисковый запрос
        }
        # Отправка GET-запроса к API
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_movie_by_rating(self, min_rating, max_rating, limit=5):
        """Поиск фильмов по рейтингу"""
        url = f"{self.BASE_URL}movie"
        params = {
            "page": 1,
            "limit": limit,
            # Фильтр по рейтингу (например, "7-9")
            "rating.kp": f"{min_rating}-{max_rating}",
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_movie_by_budget(self, budget_type, limit=5):
        """Поиск фильмов по бюджету"""
        url = f"{self.BASE_URL}movie"
        params = {
            "page": 1,
            "limit": limit,
            "sortField": "budget.value",  # Сортировка по бюджету
            # Сортировка: -1 = по убыванию (высокий бюджет), 1 = по возрастанию (низкий бюджет)
            "sortType": -1 if budget_type == "high" else 1
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_movie_details(self, movie_id):
        """Получения информации о фильме по ID"""
        url = f"{self.BASE_URL}movie/{movie_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()
