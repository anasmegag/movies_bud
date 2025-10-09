import requests
import API  # ton fichier API.py contient : key = "ta_clé_tmdb"

def get_popular_movies(page: int = 1) -> list[dict]:
    """
    Récupère les films populaires depuis TMDb.
    Retourne une liste de dictionnaires : [{id, title, poster}, ...]
    """
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API.key}&language=en-EN&page={page}"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Erreur :", response.status_code, response.text)
        return []

    data = response.json()
    movies = []

    for m in data.get("results", []):
        movies.append({
            "id": m["id"],
            "title": m["title"],
            "poster": f"https://image.tmdb.org/t/p/w500{m['poster_path']}" if m.get("poster_path") else None
        })

    return movies


# --- Exemple d’utilisation ---
if __name__ == "__main__":
    popular_movies = get_popular_movies()
    for movie in popular_movies[:10]:  # afficher les 10 premiers
        print(movie)
