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


def median(data: list, sorted: bool = False) -> float:
    """Calculate the median of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    if not sorted:
        data = sort(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]


def quartiles(data: list) -> list:
    """Calculate the quartiles [25%, 75%] of a dataset."""
    if not check_data(data):
        raise ValueError("Invalid data.")
    if len(data) == 1:
        return [data[0], data[0]]
    data = sort(data)
    n = len(data)
    lower = (n - 1) / 4
    upper = 3 * (n - 1) / 4
    lower_index = int(lower)
    upper_index = int(upper)
    lower_value = data[lower_index] + \
        (data[lower_index + 1] - data[lower_index]) * (lower - lower_index)
    upper_value = data[upper_index] + \
        (data[upper_index + 1] - data[upper_index]) * (upper - upper_index)

    return [lower_value, upper_value]


def variance(data: list) -> float:
    """Calculate the sample variance of a dataset."""
    if not check_data(data):
        raise ValueError("ERROR")
    if len(data) == 1:
        return 0
    m = mean(data)
    squared_differences = [(x - m) ** 2 for x in data]
    return sum(squared_differences) / len(data)


def standard_deviation(data: list) -> float:
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
                print(f"mean : {mean(data)}")
            except ValueError:
                print("ERROR")
        elif p == 'median':
            try:
                m = median(data)
                if int(m) == m:
                    print(f"median : {int(m)}")
                else:
                    print(f"median : {m}")
            except ValueError:
                print("ERROR")
        elif p == 'quartile':
            try:
                print(f"quartile : {list(map(float, quartiles(data)))}")
            except ValueError:
                print("ERROR")
        elif p == 'variance' or p == "var":
            try:
                v = variance(data)
                if int(v) == v:
                    print("var :", int(v))
                else:
                    print("var :", v)
            except ValueError:
                print("ERROR")
        elif p == 'std' or p == 'standard_deviation':
            try:
                print(f"std : {standard_deviation(data)}")
            except ValueError:
                print("ERROR")
