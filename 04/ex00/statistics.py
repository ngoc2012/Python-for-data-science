def check_data(data: list) -> bool:
    """Check if the data is valid."""
    if not data\
        or not isinstance(data, list)\
        or len(data) == 0:
        return False
    return all(isinstance(x, (int, float)) for x in data)


def sort(data: list) -> list:
    """Sort the data."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data


def mean(data: list) -> float:
    """Calculate the mean of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    return sum(data) / len(data)


def median(data):
    """Calculate the median of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    
    data = sort(data)
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
    # import pandas as pd
    # data_series = pd.Series(data)
    # print("Quartile: ", [data_series.quantile(0.25), data_series.quantile(0.75)])
    data = sort(data)
    n = len(data)
    return [data[n // 4], data[(n // 4) * 3]]


def variance(data):
    """Calculate the sample variance of a dataset."""
    if not check_data(data):
        raise ValueError("ERROR")
    if len(data) < 2:
        raise ValueError("Variance requires at least two data points.")
    # import numpy as np
    # variance = np.var(data, ddof=0)
    # print("Variance:", variance)
    m = mean(data)
    squared_differences = [(x - m) ** 2 for x in data]
    return sum(squared_differences) / len(data)


def standard_deviation(data):
    """Calculate the sample standard deviation of a dataset."""
    # import numpy as np
    # std_dev = np.std(data, ddof=0)
    # print("Standard Deviation:", std_dev)
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
                print(f"mean : {mean(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'median':
            try:
                m = median(data)
            except ValueError as e:
                print("ERROR")
            if int(m) == m:
                print(f"median : {int(m)}")
            else:
                print(f"median : {m}")
        elif p == 'quartile':
            try:
                print(f"quartile : {list(map(float, quartiles(data)))}")
            except ValueError as e:
                print("ERROR")
        elif p == 'variance' or p == "var":
            try:
                print(f"var : {variance(data)}")
            except ValueError as e:
                print("ERROR")
        elif p == 'std' or p == 'standard_deviation':
            try:
                print(f"std : {standard_deviation(data)}")
            except ValueError as e:
                print("ERROR")
