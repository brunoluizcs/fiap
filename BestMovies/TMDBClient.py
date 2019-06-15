import requests


class TMDBClient:
    BASE_URL = "https://api.themoviedb.org/3/discover/movie"
    API_KEY = ""

    def request_best_movies_from_year(self, year):
        params = {
            'language': 'pt-BR',
            'primary_release_year': year,
            'sort_by': 'vote_average.desc',
            'api_key': self.API_KEY,
            'vote_count.gte': 100
        }

        r = requests.get(self.BASE_URL, params)
        data = r.json()

        movies = []
        for d in data["results"]:
            movie = {
                'id': d["id"],
                'title': d["title"],
                'original_title': d["original_title"],
                'release_date': d["release_date"],
                'overview': d["overview"],
                'vote_average': d["vote_average"],
                'vote_count': d["vote_count"]
            }
            movies.append(movie)
        return movies









