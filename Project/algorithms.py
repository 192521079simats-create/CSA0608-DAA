# EventSphere X
# Scheduling Algorithms

# Check whether two events overlap
def is_overlap(event1, event2):
    return (
        event1["start"] < event2["end"]
        and event2["start"] < event1["end"]
    )


# Check venue compatibility
def is_compatible(event, venue):
    return (
        event["attendance"] <= venue["capacity"]
        and event["facility"] in venue["facilities"]
    )


# 1. GREEDY ALGORITHM
def greedy_schedule(events, venues):
    sorted_events = sorted(events, key=lambda x: x["end"])

    assignments = {venue["name"]: [] for venue in venues}
    total_reward = 0

    for event in sorted_events:
        for venue in venues:
            if not is_compatible(event, venue):
                continue

            conflict = any(
                is_overlap(event, assigned)
                for assigned in assignments[venue["name"]]
            )

            if not conflict:
                assignments[venue["name"]].append(event)
                total_reward += event["reward"]
                break

    return assignments, total_reward


# 2. WEIGHTED INTERVAL DYNAMIC PROGRAMMING
def weighted_interval_dp(events):
    sorted_events = sorted(events, key=lambda x: x["end"])
    n = len(sorted_events)

    previous = []

    for i in range(n):
        j = i - 1

        while j >= 0:
            if sorted_events[j]["end"] <= sorted_events[i]["start"]:
                break
            j -= 1

        previous.append(j)

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        include = (
            sorted_events[i - 1]["reward"]
            + dp[previous[i - 1] + 1]
        )

        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    selected = []
    i = n

    while i > 0:
        event = sorted_events[i - 1]

        include = event["reward"] + dp[previous[i - 1] + 1]

        if include > dp[i - 1]:
            selected.append(event)
            i = previous[i - 1] + 1
        else:
            i -= 1

    selected.reverse()

    return selected, dp[n]


# 3. BRUTE FORCE ALGORITHM
def brute_force_schedule(events):
    n = len(events)
    best_reward = 0
    best_schedule = []

    for mask in range(1 << n):
        selected = []

        for i in range(n):
            if mask & (1 << i):
                selected.append(events[i])

        valid = True

        for i in range(len(selected)):
            for j in range(i + 1, len(selected)):
                if is_overlap(selected[i], selected[j]):
                    valid = False
                    break
            if not valid:
                break

        reward = sum(event["reward"] for event in selected)

        if valid and reward > best_reward:
            best_reward = reward
            best_schedule = selected

    return best_schedule, best_reward


# 4. BACKTRACKING ALGORITHM
def backtracking_schedule(events, venues):
    sorted_events = sorted(events, key=lambda x: x["start"])

    assignments = {venue["name"]: [] for venue in venues}

    best_assignments = None
    best_reward = 0

    def solve(index, current_reward):
        nonlocal best_reward, best_assignments

        if index == len(sorted_events):
            if current_reward > best_reward:
                best_reward = current_reward
                best_assignments = {
                    name: list(items)
                    for name, items in assignments.items()
                }
            return

        event = sorted_events[index]

        # Try assigning event to a compatible venue
        for venue in venues:
            if not is_compatible(event, venue):
                continue

            name = venue["name"]

            conflict = any(
                is_overlap(event, assigned)
                for assigned in assignments[name]
            )

            if not conflict:
                assignments[name].append(event)

                solve(
                    index + 1,
                    current_reward + event["reward"]
                )

                assignments[name].pop()

        # Try skipping the event
        solve(index + 1, current_reward)

    solve(0, 0)

    return best_assignments, best_reward
# MERGE SORT ALGORITHM

def merge_sort(events):
    if len(events) <= 1:
        return events

    mid = len(events) // 2

    left = merge_sort(events[:mid])
    right = merge_sort(events[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["start"] <= right[j]["start"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result