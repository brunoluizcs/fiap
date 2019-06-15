from flask import Flask
from TMDBClient import TMDBClient
from flask import abort
from flask import jsonify

app = Flask(__name__)
client = TMDBClient()


@app.route('/')
def index():
    return "<p>Saiba quais foram os melhores filmes do ano do seu nascimento.<p>"


@app.route('/api/v1/movies/<int:year>')
def get_movies_by_year(year):
    try:
        assert (year > 0)
    except:
        abort(400, "Para de sacanagem ! \{year} não é um ano válido")

    data = client.request_best_movies_from_year(year)

    return jsonify({"result": data})
