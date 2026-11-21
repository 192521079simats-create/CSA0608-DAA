from data import events

def generate_dataset(multiplier):
    dataset = []

    for i in range(multiplier):
        for event in events:
            new_event = event.copy()
            new_event["name"] = event["name"] + "_" + str(i + 1)
            new_event["start"] = event["start"] + (i * 24)
            new_event["end"] = event["end"] + (i * 24)
            dataset.append(new_event)

    return dataset


small_dataset = events
dataset_10x = generate_dataset(10)
dataset_100x = generate_dataset(100)

print("Small Dataset:", len(small_dataset), "events")
print("10x Dataset:", len(dataset_10x), "events")
print("100x Dataset:", len(dataset_100x), "events")