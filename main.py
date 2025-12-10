def max_window_sum(readings, k):
    """
    Return the maximum sum of any contiguous subarray of length k.

    :param readings: list of integers (may be positive, zero, or negative)
    :param k: length of the sliding window (int)
    :return: maximum sum over all windows of size k (int)
    :raises ValueError: if k <= 0, k > len(readings), or readings is empty
    """

    # error checks
    if k <= 0:
        raise ValueError("k must be positive")
    if len(readings) == 0:
        raise ValueError("readings list is empty")
    if k > len(readings):
        raise ValueError("k cannot be larger than number of readings")

    # compute the initial window
    current_sum = sum(readings[:k])
    max_sum = current_sum

    # slide the window across the list
    for i in range(k, len(readings)):
        current_sum = current_sum - readings[i - k] + readings[i]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum