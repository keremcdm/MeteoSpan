# main.py
import api_client  # when this runs, the CSV is updated
from utils import get_city_day_report

CSV_PATH = "turkey_weather.csv"

def main():

    while True:
        city_or_plate = input("\nCity name / plate: ").strip()
        day_offset = input("How many days? (-N / 0 / +N): ").strip()

        try:
            report = get_city_day_report(city_or_plate, day_offset, csv_path=CSV_PATH)
            print("\n" + report)
        except Exception as e:
            print(f"Error: {e}")

        again = input("\nDo you want to make another query? (y/n): ").strip().lower()
        if again not in ("y", "yes", ""):
            break

if __name__ == "__main__":
    main()
