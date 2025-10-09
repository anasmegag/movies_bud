import requests
import API  

def get_movie_details(movie_id: int) -> dict:
    """Récupère les détails d'un film TMDb et retourne un dictionnaire."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API.key}&language=fr-FR"
    response = requests.get(url)

    if response.status_code != 200:
        return {
            "error": True,
            "status_code": response.status_code,
            "message": response.text
        }

    data = response.json()

    # On retourne un dictionnaire propre avec les infos utiles
    return {
        "title": data["title"],
        "release_date": data["release_date"],
        "vote_average": data["vote_average"],
        "vote_count": data["vote_count"],
        "genres": [g["name"] for g in data["genres"]],
        "runtime": data["runtime"],
        "overview": data["overview"],
        "budget": data["budget"],
        "revenue": data["revenue"],
        "original_language": data["original_language"],
        "poster_url": f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
    }


