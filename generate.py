from datetime import datetime, timedelta
import os

def generate_ical(path: str):
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

if __name__ == "__main__":
    os.makedirs("rss", exist_ok=True)
    generate_ical("rss/animalplanet.ics")
