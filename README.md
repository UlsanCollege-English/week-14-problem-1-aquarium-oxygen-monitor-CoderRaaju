[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IHzGDw_t)
# HW01 — Aquarium Oxygen Monitor (Sliding Window)

## Story

You are maintaining an automated oxygen monitor for a giant public aquarium. Every minute, a sensor records the dissolved oxygen level in the main tank.

Your supervisor wants to know: **"During any continuous block of `k` minutes, what was the highest total oxygen reading?"**

To answer this, you are given a list of integer readings and a window size `k`. You must compute the maximum sum of any contiguous subarray of length `k`.

---

## Technical Description

Write a function in `main.py`:

```python
max_window_sum(readings, k) -> int
```

### Inputs

- `readings`: a list of integers (can be positive, zero, or negative)
  - `len(readings)` can be 0 or more
- `k`: an integer window size

### Outputs

- Return the **maximum sum** of any contiguous subarray of length `k`

### Constraints

- If `k <= 0`, raise `ValueError`
- If `k > len(readings)`, raise `ValueError`
- If `len(readings) == 0`, you **must** raise `ValueError` (no window fits)
- Target time complexity: **O(N)** where N = `len(readings)`
- Target space complexity: **O(1)** extra space (not counting the input list)

You should *not* recompute sums from scratch for every window. Use a **sliding window**.

---

## 8 Steps of Coding (ESL Scaffold)

Use these steps on your worksheet / scratch before writing code.

1. **Read and understand the problem**
   - What is the real-world situation? What is the exact question about the numbers?

2. **Re-phrase the problem**
   - In your own words: "Given … I must return …"

3. **Identify input, output, variables**
   - Write down:
     - Input types and examples for `readings` and `k`
     - Output type and 2–3 sample outputs
     - Important variables you will need (for example: current sum, best sum, indices)

4. **Break down the problem**
   - Describe in simple English how you will:
     - Start the first window
     - Move the window one step to the right
     - Keep track of the best sum
     - Handle invalid cases (`k <= 0`, `k > len(readings)`)

5. **Pseudocode the solution**
   - Write line-by-line pseudocode using loops and if-statements
   - Example structure (do NOT copy as final code):
     - Check errors
     - Compute initial sum of first `k` elements
     - Loop from index `k` to end, updating window sum

6. **Write the actual code (hint)**
   - Translate your pseudocode into Python
   - Use a single pass over the list with a sliding window

7. **Debug (hint)**
   - Test by hand with:
     - Small lists (3–5 elements)
     - Cases with negative numbers
     - Edge cases from this README

8. **Optimize your code (hint)**
   - Check your loops:
     - Are you doing only O(N) work?
     - Are you avoiding extra lists or copies?

---

## Hints

1. Start by handling invalid `k` values **before** any other logic
2. Compute the sum of the first `k` readings once, then, for each step, subtract the number leaving the window and add the new one entering
3. Keep a variable for the **current window sum** and another for the **best (maximum) sum** so far

---

## How to Run Tests Locally

From the project root folder (where `hw01/` lives), run:

```bash
python -m pytest -q
```

Pytest will automatically discover `hw01/tests/test_hw01.py` (and the other homework tests).

---

## FAQ

**Q1: What Python version should I use?**

Use Python 3.11+ if possible. Anything 3.10+ should behave similarly for this assignment.

**Q2: Do I read from stdin or use function arguments?**

Use the function arguments. The tests will call `max_window_sum(readings, k)` directly.

The optional `if __name__ == "__main__":` block is only for your own manual testing.

**Q3: What Big-O complexity is expected?**

Your goal is O(N) time and O(1) extra space. A solution that recomputes the sum from scratch for every window will be O(N · k) and is not acceptable.

**Q4: What are common pitfalls?**

- Forgetting to handle `k <= 0` or `k > len(readings)`
- Off-by-one errors when sliding the window
- Not updating the maximum sum after the initial window

**Q5: How will this be graded?**

Primarily on:

- Correctness against tests
- Respecting the constraints (ValueErrors, O(N) approach)
- Clear, readable code and docstring

**Q6: How do I read pytest failures?**

Look for:

- The test name (e.g., `test_basic_windows`)
- The assertion that failed, showing "expected" vs "actual" values

Use this to create a small example that reproduces the bug in your own code.

**Q7: Can I change the function name?**

No. The tests expect `max_window_sum` imported from `main.py`. Keep the name and parameters exactly the same.
