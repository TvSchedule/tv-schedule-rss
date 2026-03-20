from datetime import datetime, timedelta
import os

print("=== generate.py started ===")
print("Current working directory:", os.getcwd())

def generate_ical(path: str):
    print("generate_ical called. Writing to:", path)

    now = datetime.now()
    start = now.replace(hour=21, minute=0, second=0, microsecond=0)
    end = start + timedelta(hours=1)

    ical = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//TV Schedule//JP//\n"
    ical += "BEGIN:VEVENT\n"
    ical += f"DTSTART:{start.strftime('%Y%m%dT%H%M%S')}\n"
    ical += f"DTEND:{end.strftime('%Y%m%dT%H%M%S')}\n"
    ical += "SUMMARY:ダミー番組\n"
    ical += "END:VEVENT\nEND:VCALENDAR\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(ical)

    print("File written successfully.")

if __name__ == "__main__":
    rss_dir = os.path.join(os.getcwd(), "rss")
    print("Ensuring rss directory exists:", rss_dir)
    os.makedirs(rss_dir, exist_ok=True)

    output_path = os.path.join(rss_dir, "animalplanet.ics")
    print("Output path:", output_path)

    generate_ical(output_path)

    print("=== generate.py finished ===")
　
