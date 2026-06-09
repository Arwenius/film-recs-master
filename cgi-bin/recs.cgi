#!/usr/bin/python3
print('Content-type: text/html \n')

import cgi
import sys
from filme import filme

form = cgi.FieldStorage()

genre = form.getvalue("genre", "")
typ = form.getvalue("type", "")
age = form.getvalue("age", "")
filter_liste = form.getlist("filter")

empfehlungen = []

for film in filme:

    if genre not in film["genre"]:
        continue

    if film["type"] != typ:
        continue

    if film["age"] != age:
        continue

    if not all(f in film["filter"] for f in filter_liste):
        continue

    empfehlungen.append(film)

print("""
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Filmempfehlungen</title>
<link rel="stylesheet" href="/~schularw/film-recs-master/style.css">
</head>
<body>

<header>
    <h1>🎬 Deine Filmempfehlungen</h1>
    <p>Basierend auf deinen ausgewählten Filtern</p>
</header>

<main>
""")

if empfehlungen:

    for film in empfehlungen:

        genre_text = ", ".join(film["genre"])
        filter_text = ", ".join(film["filter"])

        print(f"""
        <div class="film-card">
            <h2>{film['title']}</h2>
            <p><strong>Genre:</strong> {genre_text}</p>
            <p><strong>Typ:</strong> {film['type']}</p>
            <p><strong>Altersgruppe:</strong> {film['age']}</p>
            <p><strong>Tags:</strong> {filter_text}</p>
        </div>
        """)

else:

    print("""
    <div class="no-results">
        Keine passenden Filme gefunden.
    </div>
    """)

print("""
<a class="button" href="/~schularw/film-recs-master/index.html">
    Neue Suche
</a>

</main>

<footer>
    <a href="HIER_EURE_REPO_URL_EINFÜGEN">
        Repository
    </a>
</footer>

</body>
</html>
""")
