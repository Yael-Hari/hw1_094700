from math import ceil


def sum(values):
    """
    this func sums a list of values
    :param values: list of numbers
    :return: the sum (int/float)
    """
    total = 0
    for i in values:
        total += i
    return total


def mean(values):
    """
    this func calculate the mean of a list of values
    :param values: list of numbers
    :return: the mean (float)
    """
    total = sum(values)
    len_values = len(values)
    return total/len_values


def median(values):
    """
        this func gives the median of a list of values
        :param values: list of numbers
        :return: the median (int/float)
        """
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
    """
     this func calculate and prints the mean and median of a feature above or below a threshold
     :param feature_description: features of the wanted data
     :param data: dict of values
     :param treatment: category of checked threshold
     :param target: category calculated and printed data
     :param threshold: numeric value of the threshold
     :param is_above: bool var indicates on calculation above or below the threshold
     :param statistic_functions: functions that are being used to calculate mean and median
     :return: prints (feature_description, target category, stat_info1; stat_info2)
     """
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
