import pandas as pd


def main():
    pass


def load_data(path, features):
    df = pd.read_csv(path)
    data = df.to_dict('list')
    keys = list(data.keys())
    for item in keys:
        if item not in features:
            del(data[item])
    return data


def filter_by_feature(data, feature, values):
    data1 = dict()
    data2 = dict()
    for key in data.keys():
        data1[key] = []
        data2[key] = []
    for i in range(len(data[feature])):
        if (data[feature])[i] in values:
            add_to_dict(data, data1, i)
        else:
            add_to_dict(data, data2, i)
    return data1, data2


def add_to_dict(main_dict, second_dict, i):
    for key in main_dict.keys():
        second_dict[key].append((main_dict[key])[i])


def print_details(data, features, statistic_functions):
    for feature in features:
        print("%s: " % feature, end="")
        for i in range(len(statistic_functions)):
            if feature == "cnt" and i == 0:
                print("%d" % int(statistic_functions[i](data[feature])), end="")
            elif i == 0 or i == 2:
                print("%.1f" % (statistic_functions[i](data[feature])), end="")
            else:
                print(statistic_functions[i](data[feature]), end="")
            if i < len(statistic_functions) - 1:
                print(", ", end="")
            else:
                print()


if __name__ == '__main__':
    main()
