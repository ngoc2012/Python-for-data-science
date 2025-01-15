def calculate_mean(data):
    """Calculate the mean of a dataset."""
    if not data:
        return None
    return sum(data) / len(data)


def calculate_median(data):
    """Calculate the median of a dataset."""
    if not data
        or not isinstance(data, list)
        or not all(isinstance(x, (int, float)) for x in data)
        or len(data) == 0:
        return None
    
    data.sort()  # Sort the dataset
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]


def calculate_quartiles(data):
    """Calculate the quartiles [25%, 75%] of a dataset."""
    if not data:
        return None

    data.sort()  # Sort the dataset
    n = len(data)

    lower_half = data[:n // 2]
    upper_half = data[(n + 1) // 2:]

    q1 = calculate_median(lower_half)
    q3 = calculate_median(upper_half)

    return [q1, q3]


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    next
