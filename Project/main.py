# EventSphere X
# Main Program

from data import events, venues, display_events, display_venues

from algorithms import (
    greedy_schedule,
    weighted_interval_dp,
    brute_force_schedule,
    backtracking_schedule
)


def display_assignments(assignments, reward):
    print("\n========== FINAL SCHEDULE ==========")

    if not assignments:
        print("No events scheduled.")
        return

    for venue, scheduled_events in assignments.items():
        print("\nVenue:", venue)

        if not scheduled_events:
            print("No events assigned.")
            continue

        for event in scheduled_events:
            print(
                event["name"],
                "| Time:", event["start"], "-", event["end"],
                "| Reward:", event["reward"]
            )

    print("\nTotal Reward:", reward)


def main():

    while True:

        print("\n===================================")
        print("       EVENTSPHERE X")
        print("  MULTI-VENUE EVENT SCHEDULING")
        print("===================================")

        print("1. View Events")
        print("2. View Venues")
        print("3. Greedy Algorithm")
        print("4. Dynamic Programming")
        print("5. Brute Force Algorithm")
        print("6. Backtracking Algorithm")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_events()

        elif choice == "2":
            display_venues()

        elif choice == "3":
            assignments, reward = greedy_schedule(events, venues)
            display_assignments(assignments, reward)

        elif choice == "4":
            selected, reward = weighted_interval_dp(events)

            print("\nDynamic Programming Result:")
            for event in selected:
                print(event["name"], "| Reward:", event["reward"])

            print("Maximum Reward:", reward)

        elif choice == "5":
            selected, reward = brute_force_schedule(events)

            print("\nBrute Force Result:")
            for event in selected:
                print(event["name"], "| Reward:", event["reward"])

            print("Maximum Reward:", reward)

        elif choice == "6":
            assignments, reward = backtracking_schedule(events, venues)
            display_assignments(assignments, reward)

        elif choice == "7":
            print("\nThank you for using EventSphere X!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()