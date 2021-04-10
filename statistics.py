from math import ceil


def main():
    pass


def sum(values):
    total = 0
    for i in values:
        total += i
    return total


def mean(values):
    total = sum(values)
    len_values = len(values)
    return total/len_values


def median(values):
    sorted_values = sorted(values)
    length = len(sorted_values)
    mid = ceil(length/2)

    if length % 2 == 0:
        med = (sorted_values[mid-1]+sorted_values[mid])/2
    else:
        med = sorted_values[mid-1]
    return float(med)


statistic_functions = [sum, mean, median]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    stat_func = statistic_functions
    recorded_values = []
    if is_above:
        for i in range(len(data[treatment])):
            if data[treatment][i] > threshold:
                recorded_values.append(data[target][i])
    else:
        for i in range(0, len(data[treatment])):
            if data[treatment][i] <= threshold:
                recorded_values.append(data[target][i])
    print(f"{feature_description}:\n{target}: {stat_func[1](recorded_values)}, {stat_func[2](recorded_values)}")


if __name__ == "__main__":
    main()
