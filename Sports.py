file = open("sport.txt", "r", encoding="cp1251")

sport_count = {}

for line in file:
    parts = line.split('\t')
    if len(parts) < 4:
        continue

    sports_field = parts[3].strip()
    if sports_field == "":
        continue

    sports = [s.strip() for s in sports_field.split(",")]

    for s in sports:
        sport_count[s] = sport_count.get(s, 0) + 1

file.close()

sorted_sports = sorted(sport_count, key=sport_count.get, reverse=True)

for sport in sorted_sports[:3]:
    print(sport, sport_count[sport])
