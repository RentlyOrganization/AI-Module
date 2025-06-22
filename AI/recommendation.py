import sys
import json

def trapezoidal(r, x):
    a = 0
    b = r
    c = r
    d = r * 1.2

    if x < a or x > d:
        return 0.0
    elif a <= x <= b:
        return 1.0
    elif b < x <= d:
        return (d - x) / (d - c)
    else:
        return 0.0

def triangular(a, b, c, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)
    else:
        return 0.0

estates = [
    {"id": 101, "lat": 52.3791, "lon": 20.9351, "description": "Legionowo", "rooms": 3, "price": 530},
    {"id": 102, "lat": 52.2400, "lon": 21.0000, "description": "Śródmieście", "rooms": 2, "price": 790},
    {"id": 103, "lat": 52.5333, "lon": 20.9500, "description": "Nowy Dwór Mazowiecki", "rooms": 4, "price": 470},
    {"id": 104, "lat": 52.0000, "lon": 20.8000, "description": "Piaseczno", "rooms": 3, "price": 580},
    {"id": 105, "lat": 51.8000, "lon": 20.9000, "description": "Tarczyn", "rooms": 5, "price": 420},
    {"id": 106, "lat": 52.1677, "lon": 22.2900, "description": "Siedlce", "rooms": 2, "price": 350},
    {"id": 107, "lat": 52.1000, "lon": 21.0500, "description": "Wawer", "rooms": 4, "price": 610},
    {"id": 108, "lat": 52.2297, "lon": 21.0122, "description": "Centrum Warszawy", "rooms": 1, "price": 890},
    {"id": 109, "lat": 52.3000, "lon": 22.4000, "description": "Łosice", "rooms": 3, "price": 310},
    {"id": 110, "lat": 51.9651, "lon": 20.1489, "description": "Grójec", "rooms": 4, "price": 480},
    {"id": 111, "lat": 52.1500, "lon": 20.9500, "description": "Ursus", "rooms": 2, "price": 550},
    {"id": 112, "lat": 52.3500, "lon": 21.0500, "description": "Marki", "rooms": 5, "price": 500},
    {"id": 113, "lat": 52.5000, "lon": 21.2000, "description": "Wołomin", "rooms": 3, "price": 470},
    {"id": 114, "lat": 52.6000, "lon": 21.5000, "description": "Mińsk Mazowiecki", "rooms": 4, "price": 450},
    {"id": 115, "lat": 52.1800, "lon": 21.0200, "description": "Praga Południe", "rooms": 2, "price": 690},
    {"id": 116, "lat": 52.6110855, "lon": 21.2780, "description": "Ząbki", "rooms": 3, "price": 540},
    {"id": 117, "lat": 51.4027, "lon": 21.1471, "description": "Radom", "rooms": 5, "price": 320},
    {"id": 118, "lat": 52.0494, "lon": 20.4454, "description": "Żyrardów", "rooms": 2, "price": 390},
    {"id": 119, "lat": 52.2500, "lon": 20.4000, "description": "Błonie", "rooms": 4, "price": 460},
    {"id": 120, "lat": 50.8814, "lon": 20.6190, "description": "Ciechanów", "rooms": 3, "price": 370},
]



cities = {
    'Warsaw': {'latitude': 52.2297, 'longitude': 21.0122, 'radius': 12.83},
    'Krakow': {'latitude': 50.0647, 'longitude': 19.9450, 'radius': 10.20},
    'Lodz': {'latitude': 51.7592, 'longitude': 19.4550, 'radius': 9.66},
    'Wroclaw': {'latitude': 51.1079, 'longitude': 17.0385, 'radius': 9.66},
    'Poznan': {'latitude': 52.4064, 'longitude': 16.9252, 'radius': 9.14},
    'Gdansk': {'latitude': 54.3520, 'longitude': 18.6466, 'radius': 9.14},
    'Katowice': {'latitude': 50.2649, 'longitude': 19.0238, 'radius': 7.23},
    'Plock': {'latitude': 52.5468, 'longitude': 19.7064, 'radius': 5.29},
    'Torun': {'latitude': 53.0138, 'longitude': 18.5984, 'radius': 6.05},
}

results = []


def main():
    input_json = sys.stdin.read()
    data = json.loads(input_json)
#     data = {
#   "price": 700,
#   "longitude": 52.0,
#   "latitude": 20.0,
#   "location": "Warsaw",
#   "rooms": 2,
#   "area": 0.1
# }
    city = cities[data['location']]

    for estate in estates:
        temp = []
        lat = abs(estate['lat'] - city['latitude']) * 111
        lon = abs(estate['lon'] - city['longitude']) * 111
        distance = (lat ** 2 + lon ** 2) ** 0.5
        temp.append(trapezoidal(city['radius'], distance))
        temp.append(trapezoidal(data['price'], estate['price']))
        temp.append(triangular(int(data['rooms']) - 1, int(data['rooms']), int(data['rooms']) + 1, estate['rooms']))
        results.append((estate['id'], min(temp)))

    result = {
        "status": "ok",
        "recommendations": [
            {
                "id": estate_id,
                "score": round(score, 4),
                "description": next(e["description"] for e in estates if e["id"] == estate_id)
            }
            for estate_id, score in sorted(results, key=lambda x: x[1], reverse=True)
            # if score > 0.0
        ]
    }

    print(json.dumps(result))

if __name__ == "__main__":
    main()
