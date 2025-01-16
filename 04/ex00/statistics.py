def check_data(data: list) -> bool:
    """Check if the data is valid."""
    if not data\
        or not isinstance(data, list)\
        or len(data) == 0:
        return False
    return all(isinstance(x, (int, float)) for x in data)


def calculate_mean(data: list) -> float:
    """Calculate the mean of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    return sum(data) / len(data)


def calculate_median(data):
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


def calculate_quartiles(data):
    """Calculate the quartiles [25%, 75%] of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")

    data.sort()  # Sort the dataset
    n = len(data)

    lower_half = data[:n // 2]
    upper_half = data[(n + 1) // 2:]

    q1 = calculate_median(lower_half)
    q3 = calculate_median(upper_half)

    return [q1, q3]


def calculate_variance(data):
    """Calculate the sample variance of a dataset."""
    if not check_data(data):
        raise ValueError("ERROR")
    if len(data) < 2:
        raise ValueError("Variance requires at least two data points.")
    
    mean = sum(data) / len(data)
    squared_differences = [(x - mean) ** 2 for x in data]
    return sum(squared_differences) / (len(data) - 1)


def calculate_standard_deviation(data):
    """Calculate the sample standard deviation of a dataset."""
    variance = calculate_variance(data)
    return variance ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print statistics of a dataset."""
    params = [v for k, v in kwargs.items()]
    if not all(isinstance(x, str) for x in params):
        raise TypeError("Type of data must be a string.")
    data = [x for x in args]
    for p in params:
        if p == 'mean':
            try:
                print(f"mean: {calculate_mean(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'median':
            try:
                print(f"median: {calculate_median(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'quartile':
            try:
                print(f"quartile: {calculate_quartiles(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'variance' or p == "var":
            try:
                print(f"var: {calculate_variance(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'std' or p == 'standard_deviation':
            try:
                print(f"std: {calculate_standard_deviation(data)}")
            except ValueError as e:
                print("ERROR")
