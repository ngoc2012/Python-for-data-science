def ft_statistics(*args, **kwargs):
    """
    Perform statistical calculations based on kwargs instructions.
    """
    try:
        # Extract numeric arguments
        data = [arg for arg in args if isinstance(arg, (int, float))]
        if not data:
            raise ValueError("No numeric data provided.")

        # Sort data for median and quartile calculations
        data.sort()
        n = len(data)
        results = []

        # Helper function to calculate median
        def median(data):
            n = len(data)
            if n % 2 == 0:
                return (data[n // 2 - 1] + data[n // 2]) / 2
            else:
                return data[n // 2]

        for key, value in kwargs.items():
            if value == "mean":
                mean = sum(data) / len(data)
                results.append(f"mean : {mean:.1f}")
            elif value == "median":
                median_value = median(data)
                results.append(f"median : {median_value:.1f}")
            elif value == "quartile":
                # Correct calculation of lower and upper halves
                lower_half = data[:n // 2]
                upper_half = data[n // 2 + (n % 2):]  # Skip the middle element if odd
                q1 = median(lower_half)
                q3 = median(upper_half)
                results.append(f"quartile : [{q1:.1f}, {q3:.1f}]")
            elif value == "std":
                mean = sum(data) / len(data)
                variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
                std = variance ** 0.5
                results.append(f"std : {std:.8f}")
            elif value == "var":
                mean = sum(data) / len(data)
                variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
                results.append(f"var : {variance:.8f}")
            else:
                results.append("ERROR")

        # Print results
        for result in results:
            print(result)

    except Exception as e:
        print("ERROR")
        print("ERROR")
        print("ERROR")


# Test Cases
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
