# main.py
import api_client  # burası çalışınca csv güncellenir
from utils import get_city_day_report

CSV_PATH = "turkey_weather.csv"

def main():

    while True:
        city_or_plate = input("\nŞehir adı / plaka: ").strip()
        day_offset = input("Kaç gün? (-N / 0 / +N): ").strip()

        try:
            report = get_city_day_report(city_or_plate, day_offset, csv_path=CSV_PATH)
            print("\n" + report)
        except Exception as e:
            print(f"Hata: {e}")

        again = input("\nBaşka sorgu yapmak ister misiniz? (e/h): ").strip().lower()
        if again not in ("e", "evet", ""):
            break

if __name__ == "__main__":
    main()
