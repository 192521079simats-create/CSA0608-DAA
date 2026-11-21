# EVENTSPHERE X
## Multi-Venue Event Scheduling and Conflict Resolution Engine

**Name:** Rajashree S  
**Register Number:** 192521079  
**Department:** Information Technology  
**Academic Year:** 2025–2029

## 1. Introduction
EventSphere X is a Python-based project designed to schedule events across multiple venues. It helps organize events while considering scheduling conflicts and venue availability.

## 2. Objectives
- Schedule events efficiently.
- Reduce scheduling conflicts.
- Compare different algorithms.
- Measure execution time for different dataset sizes.
- Identify suitable algorithms for larger datasets.

## 3. Technologies Used
- Python
- Visual Studio Code
- Matplotlib
- NumPy

## 4. Algorithms Implemented
1. Greedy Algorithm
2. Weighted Interval Dynamic Programming
3. Brute Force Algorithm
4. Backtracking Algorithm
5. Merge Sort

## 5. Dataset Details
Three synthetic datasets were used:
- Small Dataset – 5 events
- Medium Dataset – 50 events
- Large Dataset – 500 events

## 6. Performance Comparison
Execution time was measured using Python's time module.

| Algorithm | 5 Events (sec) | 50 Events (sec) | 500 Events (sec) |
|---|---:|---:|---:|
| Greedy | 0.000170 | 0.000883 | 0.067153 |
| Dynamic Programming | 0.000147 | 0.000213 | 0.000637 |
| Merge Sort | 0.000082 | 0.000277 | 0.000989 |

Brute Force and Backtracking were tested using the small dataset.

## 7. Complexity Analysis
| Algorithm | Time Complexity |
|---|---|
| Greedy | O(n log n) for sorting, excluding other scheduling checks |
| Dynamic Programming | O(n²) |
| Brute Force | Exponential |
| Backtracking | Exponential in the worst case |
| Merge Sort | O(n log n) |

## 8. Testing
The project was tested with small, medium and large datasets. The output of each algorithm was checked, and execution times were recorded.

## 9. Results
The algorithms produced different execution times for different dataset sizes. Merge Sort and Dynamic Programming showed low execution times in the recorded tests. Greedy scheduling took more time on the 500-event dataset.

## 10. Conclusion
EventSphere X demonstrates how different algorithm design techniques can be used for event scheduling and conflict resolution. Performance testing helps compare the algorithms and understand how their execution time changes as the dataset grows.