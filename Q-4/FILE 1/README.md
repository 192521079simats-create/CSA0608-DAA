Q4 – Brute-Force Closest Pair

Problem Context

Drone Collision-Risk Monitoring

Aim

To find the two closest points in a set of two-dimensional coordinates.

Mathematical Derivation

For n points, the number of unique pairs is:

Number of pairs = n(n - 1) / 2

Algorithm

1. Read the point coordinates.
2. Examine every unique pair.
3. Calculate the Euclidean distance between each pair.
4. Keep the pair with the minimum distance.
5. Count the distance calculations.
6. Display the closest pair and minimum distance.

Time Complexity

O(n²)

Auxiliary Space

O(1), excluding the input points and returned result.

Observation

The number of distance calculations increases quadratically with the number of points.

Result

The Brute-Force Closest-Pair algorithm is implemented and tested using multiple points.
