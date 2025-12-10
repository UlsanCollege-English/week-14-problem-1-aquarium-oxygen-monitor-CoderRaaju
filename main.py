"""
HW01 — Aquarium Oxygen Monitor (Sliding Window)

Implement max_window_sum(readings, k) to return the maximum sum of any
contiguous subarray of length k.

The solution uses the Sliding Window technique to achieve O(N) time 
complexity and O(1) extra space complexity.
"""


def max_window_sum(readings, k):
    """
    Return the maximum sum of any contiguous subarray of length k.

    :param readings: list of integers (may be positive, zero, or negative)
    :param k: length of the sliding window (int)
    :return: maximum sum over all windows of size k (int)
    :raises ValueError: if k <= 0, k > len(readings), or readings is empty
    """
    n = len(readings)

    # 1. Input Validation
    if k <= 0:
        raise ValueError("Window size k must be positive.")
    if n == 0:
        raise ValueError("Readings list cannot be empty.")
    if k > n:
        raise ValueError("Window size k cannot be greater than the length of readings.")

    # 2. Initialization: Calculate the sum of the first window (O(k))
    current_window_sum = sum(readings[:k])
    max_sum = current_window_sum

    # 3. Sliding: Iterate and update the sum (O(N-k))
    # We start the loop from index k, which is the first element of the 
    # second possible window.
    for i in range(k, n):
        # Update the sum:
        # Subtract the element leaving the window (at index i - k)
        # Add the new element entering the window (at index i)
        current_window_sum = current_window_sum - readings[i - k] + readings[i]
        
        # Keep track of the maximum sum found so far
        max_sum = max(max_sum, current_window_sum)

    return max_sum


if __name__ == "__main__":
    # Optional manual testing
    sample_readings = [3, 1, 2, 7, 4, 2]
    sample_k = 3
    print(f"Readings: {sample_readings}, k: {sample_k}")
    # Expected: max([6, 10, 13, 13]) = 13
    print(f"Maximum sum: {max_window_sum(sample_readings, sample_k)}")