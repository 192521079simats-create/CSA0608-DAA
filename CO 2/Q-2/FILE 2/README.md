Q2 – Sequential Search

Problem Context

Aircraft Maintenance Tool Tracking

Aim

To implement Sequential Search to locate a tool ID in a list and count the number of comparisons.

Algorithm

1. Read the list of tool IDs.
2. Read the target tool ID.
3. Compare the target with each element.
4. If a match is found, display its position.
5. If no match is found, display that the tool is unavailable.
6. Record the number of comparisons.

Time Complexity

- Best Case: O(1)
- Average Case: O(n)
- Worst Case: O(n)
- Auxiliary Space: O(1)

Observation

Sequential Search is suitable for small lists and occasional searches. The number of comparisons increases with the list size.

Recommendation

For a large organisation with frequent tool lookups, dictionary-based indexing can provide faster average lookup performance.

Result

Sequential Search is implemented and tested for successful and unsuccessful searches.
