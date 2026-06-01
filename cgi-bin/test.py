from filme import filme

genre = "action"
typ = "film"
age = "adults"
filter_liste = ["twenties"]

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

for film in empfehlungen:
    print(film["title"])
