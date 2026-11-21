# EventSphere X
# Event and Venue Details

events = [
    {
        "id": 1,
        "name": "Tech Conference",
        "start": 9,
        "end": 11,
        "reward": 100,
        "attendance": 80,
        "facility": "Projector"
    },
    {
        "id": 2,
        "name": "Music Festival",
        "start": 10,
        "end": 13,
        "reward": 150,
        "attendance": 120,
        "facility": "Sound System"
    },
    {
        "id": 3,
        "name": "Workshop",
        "start": 11,
        "end": 13,
        "reward": 90,
        "attendance": 40,
        "facility": "Projector"
    },
    {
        "id": 4,
        "name": "Startup Meeting",
        "start": 13,
        "end": 15,
        "reward": 120,
        "attendance": 60,
        "facility": "WiFi"
    },
    {
        "id": 5,
        "name": "Cultural Event",
        "start": 14,
        "end": 16,
        "reward": 200,
        "attendance": 150,
        "facility": "Sound System"
    }
]

venues = [
    {
        "name": "Main Hall",
        "capacity": 200,
        "facilities": ["Projector", "Sound System", "WiFi"]
    },
    {
        "name": "Conference Room",
        "capacity": 100,
        "facilities": ["Projector", "WiFi"]
    },
    {
        "name": "Open Auditorium",
        "capacity": 180,
        "facilities": ["Sound System"]
    }
]


def display_events():
    print("\n========== EVENT DETAILS ==========")

    for event in events:
        print(
            event["id"],
            event["name"],
            event["start"],
            "-",
            event["end"],
            "Reward:", event["reward"]
        )


def display_venues():
    print("\n========== VENUE DETAILS ==========")

    for venue in venues:
        print(
            venue["name"],
            "| Capacity:", venue["capacity"],
            "| Facilities:", venue["facilities"]
        )