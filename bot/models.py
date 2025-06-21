from peewee import *
from datetime import datetime

# Создаем соединение с SQLite базой данных
db = SqliteDatabase("movie_bot.db")

# Базовый класс модели для наследования
class BaseModel(Model):
    class Meta:
        database = db  # Все модели будут использовать эту БД

# Модель пользователя Telegram
class User(BaseModel):
    telegram_id = IntegerField(unique=True)  # Уникальный ID пользователя в Telegram
    username = CharField(null=True)  # @username (может отсутствовать)
    full_name = CharField(null=True)  # Полное имя пользователя
    created_ad = DateTimeField(default=datetime.now)  # Дата регистрации

# Модель истории поисковых запросов
class SearchHistory(BaseModel):
    user = ForeignKeyField(User, backref="searches")  # Связь с пользователем
    content_type = CharField()  # Тип поиска (по названию, рейтингу и т.д.)
    query = TextField(null=True)  # Текст запроса (может быть пустым)
    created_ad = DateTimeField(default=datetime.now)  # Время поиска

# Модель истории найденных фильмов
class MovieHistory(BaseModel):
    search = ForeignKeyField(SearchHistory, backref="movies")  # Связь с поисковым запросом
    movie_id = IntegerField()  # ID фильма в Kinopoisk API
    title = CharField()  # Название фильма
    description = TextField(null=True)  # Описание (может отсутствовать)
    rating = FloatField(null=True)  # Рейтинг (может отсутствовать)
    year = IntegerField(null=True)  # Год выпуска
    genres = CharField(null=True)  # Жанры (строка с перечислением)
    age_rating = CharField(null=True)  # Возрастной рейтинг (16+, 18+ и т.д.)
    poster_url = CharField(null=True)  # Ссылка на постер
    is_watched = BooleanField(default=False)  # Отметка о просмотре

# Функция для создания таблиц в БД
def create_tables():
    with db:
        db.create_tables([User, SearchHistory, MovieHistory])
