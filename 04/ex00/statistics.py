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

    return [data[n // 4], data[(n // 4) * 3]]


def variance(data):
    """Calculate the sample variance of a dataset."""
    if not check_data(data):
        raise ValueError("ERROR")
    if len(data) < 2:
        raise ValueError("Variance requires at least two data points.")
    # import statistics
    # print("Variance:", statistics.variance(data))
    import numpy as np
    variance = np.var(data, ddof=1)  # ddof=1 for sample variance
    print("Variance:", variance)
    m = mean(data)
    squared_differences = [(x - m) ** 2 for x in data]
    return sum(squared_differences) / (len(data) - 1)


def standard_deviation(data):
    """Calculate the sample standard deviation of a dataset."""
    # import statistics
    # print("Standard Deviation:", statistics.stdev(data))
    import numpy as np
    std_dev = np.std(data, ddof=0)  # ddof=1 for sample standard deviation
    print("Standard Deviation:", std_dev)
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
