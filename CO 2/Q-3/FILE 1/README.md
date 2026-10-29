Q3 – Brute-Force String Matching

Problem Context

Cybersecurity Log Screening

Aim

To locate a pattern in a text using Brute-Force String Matching and measure character comparisons.

Algorithm

1. Read the text and pattern.
2. Align the pattern with the text.
3. Compare characters one by one.
4. Record the position if all characters match.
5. Shift the pattern by one position after a mismatch.
6. Count the character comparisons.

Time Complexity

- Best Case: O(n), for fixed-length patterns that fail quickly at each alignment.
- Worst Case: O(nm)
- Auxiliary Space: O(k), where k is the number of matches stored.

Here, n is the text length and m is the pattern length.

Observation

Repeated characters can cause repeated partial matches and increase the number of character comparisons.

Result

Brute-Force String Matching is implemented and tested using three text-pattern pairs.
