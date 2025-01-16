def check_data(data: list) -> bool:
    """Check if the data is valid."""
    if not data\
        or not isinstance(data, list)\
        or len(data) == 0:
        return False
    return all(isinstance(x, (int, float)) for x in data)


def mean(data: list) -> float:
    """Calculate the mean of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    return sum(data) / len(data)


def median(data):
    """Calculate the median of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    
    data.sort()
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]


def quartiles(data):
    """Calculate the quartiles [25%, 75%] of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")

    data.sort()  # Sort the dataset
    n = len(data)

    lower_half = data[:n // 2]
    upper_half = data[(n + 1) // 2:]

    q1 = median(lower_half)
    q3 = median(upper_half)

    return [q1, q3]


def variance(data):
    """Calculate the sample variance of a dataset."""
    if not check_data(data):
        raise ValueError("ERROR")
    if len(data) < 2:
        raise ValueError("Variance requires at least two data points.")
    
    m = mean(data)
    squared_differences = [(x - m) ** 2 for x in data]
    return sum(squared_differences) / (len(data) - 1)


def standard_deviation(data):
    """Calculate the sample standard deviation of a dataset."""
    return variance(data) ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print statistics of a dataset."""
    params = [v for k, v in kwargs.items()]
    if not all(isinstance(x, str) for x in params):
        raise TypeError("Type of data must be a string.")
    data = [x for x in args]
    for p in params:
        if p == 'mean':
            try:
                print(f"mean: {mean(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'median':
            try:
                print(f"median: {median(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'quartile':
            try:
                print(f"quartile: {quartiles(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'variance' or p == "var":
            try:
                print(f"var: {variance(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'std' or p == 'standard_deviation':
            try:
                print(f"std: {standard_deviation(data)}")
            except ValueError as e:
                print("ERROR")
