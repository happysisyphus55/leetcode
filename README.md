## interview-prep
 
interview practice mono-repo.

### How do Coding Interviews Work 
- Not all coding interviews are created equal. 4 main types a candidate generally faces:
  - Phone Screen 
    - First live interaction.
    - Phone screen lasts 30 to 60 minutes over a shred online editor like coderpad.

  - Onsite(virtual or in-person)
    - block of 4 to 6 interviews spread across a single day (or 2 half-days for virtual onsites).
    - each round lasts 45 to 60 minutes and covers a different area.

    - Round	Duration	Focus
    - Round 1	45 min	Data structures and algorithms
    - Round 2	45 min	Data structures and algorithms
    - Round 3	45 min	System design (senior+)
    - Round 4	45 min	Behavioral / culture fit
    - Round 5	45 min	Coding or domain-specific

  - Key thing to understand about onsites is that no single round makes or breaks. 
  - Interviewers submit independent feedback, and a hiring committee reviews the full picture. 

### Live Coding 
- Share screen and write code in a real IDE.
- Testing: Can you write production-quality code under pressre 
  - they want to see us use a IDE naturally, run test cases, and debug issues in real time.

### Take home 
- Gives us a project (2 to 6 hours of work) to complete in our own time.
- Might build a small API, implement a feature, or solve a more complex algorithmic challenge.
- Tests depth over speed. 
  - Without time pressure, companies expect cleaner code, better test coverage, and thoughtful architecture.
  - Many take-homes are followed by a review session where we walk through our solution and answer questions about design choices.

### Hiring Timeline

Stage	Timeline	What Happens
Application	Day 0	Submit resume or get a referral
Recruiter screen	Week 1-2	15-30 min call about background and role fit
Phone screen	Week 2-4	1 technical coding round
Onsite	Week 4-7	4-6 rounds in one/two days
Hiring committee	Week 7-9	Independent review of all feedback
Offer	Week 8-10	Compensation discussion and offer letter
Startups move faster. You might go from application to offer in two weeks. Larger companies, especially those with hiring committees (Google is the classic example), can take two to three months.

### Evaluation Rubric

- **Correctness**: baseline, code should produce the right output for standard inputs and handle edge cases.
- **Efficiency**: demonstrate algorithmic knowledge. Can we identify that a problem needs O(n log n) instead of O(n^2) ? Do you understand time-space trade-offs ?
- **Communication**: tests our ability to clearly explain thought process. Can you explain your approach before writing code ? Do you talk through your decisions as you make them ?
- **Problem-Solving**: measures how you handle ambiguity. when we hit a wall, do you try a different approach or sit in silence ? can you break a complex problem into smaller subproblems ? do you recognize patterns from problems we have seen before ?

###  How Rubrics Typically Work
Most companies score each dimension on a scale. Here is a simplified version of what many FAANG-style rubrics look like:

Score	Meaning	What It Looks Like
Strong Hire	Exceeded expectations	Optimal solution, clean code, excellent communication, handled follow-ups
Hire	Met expectations	Working solution, good efficiency, communicated approach clearly
Lean Hire	Borderline	Solution worked with hints, some inefficiency, decent communication
Lean No Hire	Below bar	Needed significant hints, major bugs, unclear communication
Strong No Hire	Well below bar	Could not make meaningful progress, fundamentally wrong approach


The critical insight is that a "Hire" rating does not require perfection. You can have a small bug, miss one edge case, or need a minor hint and still get a strong score if your communication and problem-solving approach were solid.

### FAANG vs Startups

Companies like Google, Meta, Amazon, Apple, and Microsoft run highly standardized processes. Interviewers receive training, use calibrated rubrics, and submit feedback independently. A hiring committee (not the interviewer) makes the final decision.

What this means for you:

  - Problems come from curated question banks and tend toward classic algorithmic challenges.
  - System design is weighted heavily for senior roles (L5+ at Google, E5+ at Meta).
  - Behavioral rounds use structured frameworks like Amazon's Leadership Principles.

Startups optimize for speed and practical skill assessment. Their interviews are less standardized but often more realistic.

What this means for you:

  - You might get a take-home project instead of a whiteboard problem.
  - The coding round might involve a real codebase, not an isolated algorithm.
  - Culture fit and domain experience carry more weight.
  - The hiring manager often has final say, not a committee.

Dimension	FAANG	Startups
Process length	6-10 weeks	1-3 weeks
Number of rounds	4-6	2-4
Problem style	Classic algorithmic	Practical / domain-specific
Decision maker	Hiring committee	Hiring manager
System design	Dedicated round	Often combined with coding
Behavioral	Structured (STAR format)	Conversational


### Algorithms and Data Structures Resources

- To understand the theoretical aspect and the theory behind a lot
of algorithms and data structures :
  1. Abdul Bari
  2. Micheal Sambol -> to recap all these algorithms and data structures that we need to understand
- VisualAlgo.net -> Visualizations for everything that we need to know in algorithms.
- Leetcode Patterns
  - https://seanprashad.com/leetcode-patterns/

  
### System Design Resources

- [How to answer in interviews](https://www.hellointerview.com/)
- [LLD](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/introduction)
- [HLD](https://github.com/donnemartin/system-design-primer)
- [Python Design Patterns](https://python-patterns.guide/)
- [Software Design by Example in Python](https://third-bit.com/sdxpy/) 
<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
| Problem Name | Difficulty |
| ------- | ------- |
| [0014-longest-common-prefix](https://github.com/happysisyphus55/leetcode/tree/main/0014-longest-common-prefix/) | Easy |
| [0049-group-anagrams](https://github.com/happysisyphus55/leetcode/tree/main/0049-group-anagrams/) | Medium |
| [0056-merge-intervals](https://github.com/happysisyphus55/leetcode/tree/main/0056-merge-intervals/) | Medium |
| [0057-insert-interval](https://github.com/happysisyphus55/leetcode/tree/main/0057-insert-interval/) | Medium |
| [0435-non-overlapping-intervals](https://github.com/happysisyphus55/leetcode/tree/main/0435-non-overlapping-intervals/) | Medium |
| [1267-count-servers-that-communicate](https://github.com/happysisyphus55/leetcode/tree/main/1267-count-servers-that-communicate/) | Medium |
| [1606-find-servers-that-handled-most-number-of-requests](https://github.com/happysisyphus55/leetcode/tree/main/1606-find-servers-that-handled-most-number-of-requests/) | Hard |
| [3105-longest-strictly-increasing-or-strictly-decreasing-subarray](https://github.com/happysisyphus55/leetcode/tree/main/3105-longest-strictly-increasing-or-strictly-decreasing-subarray/) | Easy |
| [3420-count-non-decreasing-subarrays-after-k-operations](https://github.com/happysisyphus55/leetcode/tree/main/3420-count-non-decreasing-subarrays-after-k-operations/) | Hard |
| [3693-climbing-stairs-ii](https://github.com/happysisyphus55/leetcode/tree/main/3693-climbing-stairs-ii/) | Medium |
## Depth-First Search
| Problem Name | Difficulty |
| ------- | ------- |
| [1267-count-servers-that-communicate](https://github.com/happysisyphus55/leetcode/tree/main/1267-count-servers-that-communicate/) | Medium |
## Breadth-First Search
| Problem Name | Difficulty |
| ------- | ------- |
| [1267-count-servers-that-communicate](https://github.com/happysisyphus55/leetcode/tree/main/1267-count-servers-that-communicate/) | Medium |
## Union-Find
| Problem Name | Difficulty |
| ------- | ------- |
| [1267-count-servers-that-communicate](https://github.com/happysisyphus55/leetcode/tree/main/1267-count-servers-that-communicate/) | Medium |
## Matrix
| Problem Name | Difficulty |
| ------- | ------- |
| [1267-count-servers-that-communicate](https://github.com/happysisyphus55/leetcode/tree/main/1267-count-servers-that-communicate/) | Medium |
## Counting
| Problem Name | Difficulty |
| ------- | ------- |
| [1267-count-servers-that-communicate](https://github.com/happysisyphus55/leetcode/tree/main/1267-count-servers-that-communicate/) | Medium |
## Heap (Priority Queue)
| Problem Name | Difficulty |
| ------- | ------- |
| [1606-find-servers-that-handled-most-number-of-requests](https://github.com/happysisyphus55/leetcode/tree/main/1606-find-servers-that-handled-most-number-of-requests/) | Hard |
## Simulation
| Problem Name | Difficulty |
| ------- | ------- |
| [1606-find-servers-that-handled-most-number-of-requests](https://github.com/happysisyphus55/leetcode/tree/main/1606-find-servers-that-handled-most-number-of-requests/) | Hard |
## Ordered Set
| Problem Name | Difficulty |
| ------- | ------- |
| [1606-find-servers-that-handled-most-number-of-requests](https://github.com/happysisyphus55/leetcode/tree/main/1606-find-servers-that-handled-most-number-of-requests/) | Hard |
## Dynamic Programming
| Problem Name | Difficulty |
| ------- | ------- |
| [0435-non-overlapping-intervals](https://github.com/happysisyphus55/leetcode/tree/main/0435-non-overlapping-intervals/) | Medium |
| [3693-climbing-stairs-ii](https://github.com/happysisyphus55/leetcode/tree/main/3693-climbing-stairs-ii/) | Medium |
## String
| Problem Name | Difficulty |
| ------- | ------- |
| [0014-longest-common-prefix](https://github.com/happysisyphus55/leetcode/tree/main/0014-longest-common-prefix/) | Easy |
| [0049-group-anagrams](https://github.com/happysisyphus55/leetcode/tree/main/0049-group-anagrams/) | Medium |
## Trie
| Problem Name | Difficulty |
| ------- | ------- |
| [0014-longest-common-prefix](https://github.com/happysisyphus55/leetcode/tree/main/0014-longest-common-prefix/) | Easy |
## Hash Table
| Problem Name | Difficulty |
| ------- | ------- |
| [0049-group-anagrams](https://github.com/happysisyphus55/leetcode/tree/main/0049-group-anagrams/) | Medium |
## Sorting
| Problem Name | Difficulty |
| ------- | ------- |
| [0049-group-anagrams](https://github.com/happysisyphus55/leetcode/tree/main/0049-group-anagrams/) | Medium |
| [0056-merge-intervals](https://github.com/happysisyphus55/leetcode/tree/main/0056-merge-intervals/) | Medium |
| [0435-non-overlapping-intervals](https://github.com/happysisyphus55/leetcode/tree/main/0435-non-overlapping-intervals/) | Medium |
## Math
| Problem Name | Difficulty |
| ------- | ------- |
| [3789-minimum-cost-to-acquire-required-items](https://github.com/happysisyphus55/leetcode/tree/main/3789-minimum-cost-to-acquire-required-items/) | Medium |
## Greedy
| Problem Name | Difficulty |
| ------- | ------- |
| [0435-non-overlapping-intervals](https://github.com/happysisyphus55/leetcode/tree/main/0435-non-overlapping-intervals/) | Medium |
| [3789-minimum-cost-to-acquire-required-items](https://github.com/happysisyphus55/leetcode/tree/main/3789-minimum-cost-to-acquire-required-items/) | Medium |
## Quicksort
| Problem Name | Difficulty |
| ------- | ------- |
| [0056-merge-intervals](https://github.com/happysisyphus55/leetcode/tree/main/0056-merge-intervals/) | Medium |
## Stack
| Problem Name | Difficulty |
| ------- | ------- |
| [3420-count-non-decreasing-subarrays-after-k-operations](https://github.com/happysisyphus55/leetcode/tree/main/3420-count-non-decreasing-subarrays-after-k-operations/) | Hard |
## Segment Tree
| Problem Name | Difficulty |
| ------- | ------- |
| [3420-count-non-decreasing-subarrays-after-k-operations](https://github.com/happysisyphus55/leetcode/tree/main/3420-count-non-decreasing-subarrays-after-k-operations/) | Hard |
## Queue
| Problem Name | Difficulty |
| ------- | ------- |
| [3420-count-non-decreasing-subarrays-after-k-operations](https://github.com/happysisyphus55/leetcode/tree/main/3420-count-non-decreasing-subarrays-after-k-operations/) | Hard |
## Sliding Window
| Problem Name | Difficulty |
| ------- | ------- |
| [3420-count-non-decreasing-subarrays-after-k-operations](https://github.com/happysisyphus55/leetcode/tree/main/3420-count-non-decreasing-subarrays-after-k-operations/) | Hard |
## Monotonic Stack
| Problem Name | Difficulty |
| ------- | ------- |
| [3420-count-non-decreasing-subarrays-after-k-operations](https://github.com/happysisyphus55/leetcode/tree/main/3420-count-non-decreasing-subarrays-after-k-operations/) | Hard |
## Monotonic Queue
| Problem Name | Difficulty |
| ------- | ------- |
| [3420-count-non-decreasing-subarrays-after-k-operations](https://github.com/happysisyphus55/leetcode/tree/main/3420-count-non-decreasing-subarrays-after-k-operations/) | Hard |
<!---LeetCode Topics End-->