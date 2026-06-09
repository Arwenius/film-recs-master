#!/usr/bin/python3

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

print("Content-Type: text/html")
print()

print("""
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Filmempfehlungen</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>

<h1>Deine Filmempfehlungen</h1>
""")

if empfehlungen:

    print("<ul>")

    for film in empfehlungen:
    print(f"""
    <div class="film-card">
        <h2>{film['title']}</h2>
        <p>Genre: {', '.join(film['genre'])}</p>
        <p>Typ: {film['type']}</p>
        <p>Altersgruppe: {film['age']}</p>
    </div>
    """)

else:

    print("<p>Keine passenden Filme gefunden.</p>")

print("""
<p><a href="../index.html">Neue Suche</a></p>

<footer>
<a href="LINK_ZUM_REPOSITORY">
Repository
</a>
</footer>

</body>
</html>
""")
