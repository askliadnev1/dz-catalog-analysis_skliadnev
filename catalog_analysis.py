import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    """Средняя оценка по каталогу, округлённая до 1 знака."""
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Кортеж: (возраст самого старого, возраст самого нового, средний возраст)."""
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Переводит минуты в строку вида '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    """Категория фильма по оценке."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Метка фильма по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy(movies):
    """Печатает названия фильмов, которые не относятся к жанру comedy."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies, min_rating=9.0):
    """Ищет первый фильм с рейтингом выше min_rating."""
    i = 0
    while i < len(movies):
        movie = movies[i]
        if movie["rating"] > min_rating:
            print(f"Первый шедевр: {movie['title']} ({movie['rating']})")
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее threshold минут."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    """Приводит название к Title Case без str.title()."""
    words = title.split()
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:])
    return " ".join(new_words)


def make_slug(title):
    """Превращает название в слаг: 'Silent Hours' -> 'silent-hours'."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Строка отчёта с описанием фильма."""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def get_rating(movie):
    """Возвращает рейтинг фильма: используется как key при сортировке."""
    return movie["rating"]


def titles_sorted_by_rating(movies):
    """Названия фильмов по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=get_rating, reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Топ-n фильмов: список кортежей (название, рейтинг)."""
    sorted_movies = sorted(movies, key=get_rating, reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    """Словарь {жанр: количество фильмов}."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Словарь {актёр: [названия фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def above_average_ratings(movies):
    """Словарь {название: рейтинг} для фильмов с рейтингом выше среднего."""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }


def all_genres(movies):
    """Множество всех уникальных жанров."""
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Актёры, снимавшиеся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Жанры, которые есть в movies_a, но нет в movies_b."""
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    """Генератор: лениво отдаёт фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_above(movies, min_rating=7):
    """Суммарная длительность фильмов с рейтингом выше min_rating, в минутах."""
    return sum(
        movie["duration_min"] for movie in movies if movie["rating"] > min_rating
    )


def genre_sort_key(item):
    """Ключ сортировки жанров: по убыванию количества, при равенстве по алфавиту."""
    genre, count = item
    return (-count, genre)


def build_report(movies):
    """Печатает итоговый отчёт по каталогу."""
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    oldest, newest, average_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {average_age} лет")

    print()
    print("Топ-3 фильма:")
    movies_by_title = {movie["title"]: movie for movie in movies}
    for title, _rating in top_n_by_rating(movies, 3):
        print(f"  {format_report_line(movies_by_title[title])}")

    print()
    print("Фильмов по жанрам:")
    genre_counts = sorted(count_by_genre(movies).items(), key=genre_sort_key)
    for genre, count in genre_counts:
        print(f"  {genre} — {count}")

    print()
    print(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")


if __name__ == "__main__":
    build_report(movies)