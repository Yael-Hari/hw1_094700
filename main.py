import sys
import data as dt
import statistics as stats


def main(argv):
    features = ["cnt", "t1", "hum", "is_holiday", "season"]
    data = dt.load_data('london.csv', features)
    Q1(data)
    Q2(data)


def Q1(data):
    print("Question 1:")
    features = ["hum", "t1", "cnt"]
    summer = (dt.filter_by_feature(data, "season", {1}))[0]
    holiday = (dt.filter_by_feature(data, "is_holiday", {1}))[0]
    all = data

    q1_categories = {"Summer": summer, "Holiday": holiday, "All": all}

    for category in q1_categories:
        print("%s:" % category)
        dt.print_details(q1_categories[category], features, stats.statistic_functions)


def Q2(data):
    winter_time = (dt.filter_by_feature(data, "season", {3}))[0]
    yes_holiday, no_holiday = dt.filter_by_feature(winter_time, "is_holiday", {1})

    print_statements = ["If t1<=13.0, then:", "If t1>13.0, then:"]

    print("\nQuestion 2:")

    for index, elem in enumerate(print_statements):
        print(elem)
        for key, dict in ({"Winter holiday records": yes_holiday, "Winter weekday records": no_holiday}).items():
            stats.population_statistics(key, dict, "t1", "cnt", 13.0, index, stats.statistic_functions)


if __name__ == '__main__':
    main(sys.argv)
