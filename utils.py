import pandas as pd
from api_client import CITY_NAMES, CITY_TO_PLATE, PLATE_TO_CITY, CITY_TO_COORDS, CITY_INDEX
from weather_codes import WEATHER_CODES

def get_city_or_plate(user_input):

    text = user_input.strip()
    # Find the city plate if a digit is given
    if text.isdigit():
        plate = f"{int(text):02d}"
        city = PLATE_TO_CITY.get(plate)
        if city is None:
            raise ValueError("Geçersiz plaka kodu.")
    else:
        # Find the city name regardless of upper/lower case
        city = None
        for name in CITY_NAMES:
            if name.casefold() == text.casefold():
                city = name
                break
        if city is None:
            raise ValueError("Geçersiz şehir adı.")
        plate = CITY_TO_PLATE[city]

    idx = CITY_INDEX[city]
    coords = CITY_TO_COORDS[city]
    return {"city": city, "plate": plate, "index": idx, "coords": coords}

def get_date(user_input: str):

    text = user_input.strip()

    if text.lstrip("+-").isdigit():
        days = int(text)
        return days
    else:
        raise ValueError("Geçersiz giriş! +N, -N veya 0 formatında giriniz.")


def get_city_day_row(city_or_plate, day_offset, csv_path="turkey_weather.csv"):

    # Get the name or the plate of the city from the user
    sel = get_city_or_plate(city_or_plate)

    # Get the day offset
    offset = get_date(day_offset)

    # Read the files and filter the list for the chosen city
    df = pd.read_csv(csv_path, parse_dates=["date"])
    city_df = df[df["city"] == sel["city"]].sort_values("date").reset_index(drop=True)

    # Set the center of the list as today
    center = len(city_df) // 2
    idx = center + offset

    if not (0 <= idx < len(city_df)):
        raise ValueError(f"Seçtiğiniz gün sayısı aralık dışında. Geçerli: {-center}..{len(city_df)-1-center}")
    row = city_df.iloc[idx]
    return {
        "city": row["city"],
        "plate": row["plate"],
        "date": row["date"].date().isoformat(),
        "weather_code": int(row["weather_code"]),
        "t_mean": float(row["temperature_2m_mean"]),
        "t_max": float(row["temperature_2m_max"]),
        "t_min": float(row["temperature_2m_min"]),
    }

def get_city_day_report(city_or_plate, day_offset, csv_path="turkey_weather.csv"):

    data = get_city_day_row(city_or_plate, day_offset, csv_path=csv_path)

    # Getting a Turkish description from weather codes
    code = data["weather_code"]
    desc = WEATHER_CODES.get(code, f"Bilinmeyen kod {code}")

    # Getting a descriptive text
    text = (
        f"{data['city']} ({data['plate']}) – {data['date']}\n"
        f"Hava durumu: {desc}\n"
        f"Ortalama: {data['t_mean']:.1f}°C  |  "
        f"Min: {data['t_min']:.1f}°C  |  "
        f"Max: {data['t_max']:.1f}°C"
    )
    return text
