Task 2 – Job Sequencing with Deadlines
1. Problem model
Input: jobs with an ID, deadline and profit; each job needs one time slot.
Output: selected jobs with their assigned slots and total profit.
Objective: maximise profit from jobs completed on or before deadlines.
Constraints: one job per slot; a job assigned to slot s must satisfy s <= deadline.
Decision: whether to select a job and which available slot to assign.
Feasibility information: deadline and whether the chosen slot is empty.
2. Greedy hypothesis
Sort jobs by descending profit and place each job in the latest free slot at or before its deadline. This preserves earlier slots for jobs with tighter deadlines while accepting the most profitable available jobs first.
3. Pseudocode
ALGORITHM JobSequencing(Jobs)
INPUT: Jobs with ID, deadline, profit
OUTPUT: Schedule and maximum profit

BEGIN
    maxDeadline <- maximum deadline among Jobs
    CREATE slots[1..maxDeadline], initially EMPTY
    SORT Jobs by profit in descending order
    totalProfit <- 0

    FOR each job j in Jobs DO
        FOR slot <- MIN(j.deadline, maxDeadline) DOWNTO 1 DO
            IF slots[slot] is EMPTY THEN
                slots[slot] <- j.ID
                totalProfit <- totalProfit + j.profit
                BREAK
            END IF
        END FOR
    END FOR

    RETURN slots, totalProfit
END
4. Desk-check
Input:
Job
Deadline
Profit
A
2
80
B
1
35
C
2
60
D
3
40
E
1
25
Profit order: A(80), C(60), D(40), B(35), E(25).
Job considered
Slot decision
Schedule after decision
Profit
A
Put in slot 2
[–, A, –]
80
C
Slot 2 full; put in slot 1
[C, A, –]
140
D
Put in slot 3
[C, A, D]
180
B
Slot 1 full; reject
[C, A, D]
180
E
Slot 1 full; reject
[C, A, D]
180
Final schedule: slot 1 = C, slot 2 = A, slot 3 = D.
Maximum profit = 60 + 80 + 40 = 180.
5. Challenge / modified input
Change only job D's profit from 40 to 90. The descending order becomes D(90), A(80), C(60), B(35), E(25).
D is placed in slot 3.
A is placed in slot 2.
C is placed in slot 1.
B and E cannot be placed. The schedule remains the same job set {A, C, D}, but the total profit changes to 90 + 80 + 60 = 230. The changed decision is D's priority: it is now considered first.
6. Complexity
Let n be the number of jobs and d the maximum deadline. Sorting takes O(n log n) and slot searching takes at most O(nd). Total time is O(n log n + nd); slot storage is O(d).
