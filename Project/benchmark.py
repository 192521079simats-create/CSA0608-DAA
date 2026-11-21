import time
from data import venues
from algorithms import (
    greedy_schedule,
    weighted_interval_dp,
    brute_force_schedule,
    backtracking_schedule,
    merge_sort
 )
from test_data import small_dataset, dataset_10x, dataset_100x

datasets = {
    "Small (5 events)": small_dataset,
    "10x (50 events)": dataset_10x,
    "100x (500 events)": dataset_100x
}

print("\nEVENTSPHERE X - PERFORMANCE COMPARISON")
print("=" * 45)

for dataset_name, events in datasets.items():

    print("\n", dataset_name)

    algorithms = [
        ("Greedy", lambda: greedy_schedule(events, venues)),
        ("Dynamic Programming", lambda: weighted_interval_dp(events)),
        ("Merge Sort", lambda: merge_sort(events))
    ]

    if dataset_name == "Small (5 events)":
        algorithms.extend([
            ("Brute Force", lambda: brute_force_schedule(events)),
            ("Backtracking", lambda: backtracking_schedule(events, venues))
        ])

    for name, function in algorithms:
        start = time.perf_counter()
        function()
        end = time.perf_counter()

        print(name, ":", round(end - start, 6), "seconds")

print("\nPerformance testing completed!")