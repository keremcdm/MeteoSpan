import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# --- Plaka sırasına göre şehir isimleri ---
CITY_NAMES = [
    "Adana","Adıyaman","Afyonkarahisar","Ağrı","Amasya","Ankara","Antalya","Artvin","Aydın","Balıkesir",
    "Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli",
    "Diyarbakır","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari",
    "Hatay","Isparta","Mersin","İstanbul","İzmir","Kars","Kastamonu","Kayseri","Kırklareli","Kırşehir",
    "Kocaeli","Konya","Kütahya","Malatya","Manisa","Kahramanmaraş","Mardin","Muğla","Muş","Nevşehir",
    "Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat",
    "Trabzon","Tunceli","Şanlıurfa","Uşak","Van","Yozgat","Zonguldak","Aksaray","Bayburt","Karaman",
    "Kırıkkale","Batman","Şırnak","Bartın","Ardahan","Iğdır","Yalova","Karabük","Kilis","Osmaniye","Düzce"
]

# --- Plaka sırasına göre şehir koordinatları ---
LAT = [36.98542, 37.76299, 38.756217, 39.718993, 40.656314, 39.942928, 36.896126, 41.18131, 37.838044, 39.644878, 40.14296, 38.88472, 38.400664, 40.732006, 37.718293, 40.182816, 40.146777, 40.60019, 40.549853, 37.783026, 37.9137, 41.675907, 38.6763, 39.75, 39.905994, 39.766724, 37.062931, 40.917921, 40.458673, 37.57812, 36.202621, 37.762627, 36.810307, 41.046419, 38.423652, 40.601469, 41.378133, 38.7221, 41.735547, 39.146209, 40.7656, 37.872817, 39.419993, 38.35539, 38.614027, 37.582047, 37.313051, 37.215266, 38.732415, 38.623861, 37.96911, 40.985592, 41.025113, 40.773626, 41.28157, 37.927462, 42.026596, 39.750528, 40.978127, 40.323397, 41.001289, 39.108101, 37.1586, 38.678883, 38.501287, 39.820954, 41.45265, 38.370386, 40.250858, 37.1812, 39.849998, 37.882999, 37.522781, 41.633178, 41.112875, 39.895802, 40.657659, 41.200069, 36.717999, 37.074695, 40.839377]
LON = [35.32502, 38.277298, 30.537846, 43.047663, 35.837068, 32.860481, 30.713081, 41.820537, 27.845571, 27.885361, 29.979159, 40.496391, 42.108971, 31.607052, 30.282248, 29.066148, 26.40822, 33.616304, 34.953694, 29.096246, 40.224899, 26.553608, 39.221802, 39.5, 41.273784, 30.525608, 37.378159, 38.389876, 39.478961, 43.733805, 36.160045, 30.553612, 34.620414, 29.033115, 27.142797, 43.097496, 33.776539, 35.489122, 27.224502, 34.160577, 29.940659, 32.491991, 29.985721, 38.333476, 27.429533, 36.926934, 40.732555, 28.363718, 41.489878, 34.712756, 34.678619, 37.879123, 40.516397, 30.403235, 36.33812, 41.94227, 35.151245, 37.015028, 27.511091, 36.552149, 39.716549, 39.548199, 38.797901, 29.404976, 43.372931, 34.808617, 31.790032, 34.026986, 40.202831, 33.222315, 33.5, 41.130901, 42.459438, 32.338396, 42.702389, 44.040821, 29.268905, 32.629601, 37.116901, 36.246347, 31.159454]

# --- Şehir koordinat eşleştirmesi ---
CITY_TO_COORDS = {name: (LAT[i], LON[i]) for i, name in enumerate(CITY_NAMES)}
CITY_INDEX = {name: i for i, name in enumerate(CITY_NAMES)}

# --- Plaka ve şehir ismi eşleştirmesi ---
CITY_TO_PLATE = {name: f"{i+1:02d}" for i, name in enumerate(CITY_NAMES)}
PLATE_TO_CITY = {v: k for k, v in CITY_TO_PLATE.items()}
PLATE_TO_COORDS = {p: CITY_TO_COORDS[n] for n, p in CITY_TO_PLATE.items()}

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": LAT,
    "longitude": LON,
    "daily": ["weather_code", "temperature_2m_mean", "temperature_2m_max", "temperature_2m_min"],
    "timezone": "Africa/Cairo",
    "past_days": 14,
    "forecast_days": 14
}
responses = openmeteo.weather_api(url, params=params)

rows = []

# Process 81 locations
for idx, response in enumerate(responses):
    city = CITY_NAMES[idx]
    daily = response.Daily()

    dates = pd.date_range(
        start=pd.to_datetime(daily.Time(), unit="s", utc=True),
        end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=daily.Interval()),
        inclusive="left"
    )

    # Process daily data. The order of variables needs to be the same as requested.
    wcode = daily.Variables(0).ValuesAsNumpy()
    tmean = daily.Variables(1).ValuesAsNumpy()
    tmax  = daily.Variables(2).ValuesAsNumpy()
    tmin  = daily.Variables(3).ValuesAsNumpy()

    df = pd.DataFrame({
        "plate": f"{idx+1:02d}",
        "city": city,
        "date": dates,
        "weather_code": wcode,
        "temperature_2m_mean": tmean,
        "temperature_2m_max": tmax,
        "temperature_2m_min": tmin
    })
    rows.append(df)

final_df = pd.concat(rows, ignore_index=True)
final_df.to_csv("turkey_weather.csv", index=False, encoding="utf-8")
