import statistics

FOLDER = "swimdata/"


def read_swim_data(filename):
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER + filename) as file:
        lines = file.readlines()

    times = lines[0].strip().split(",")
    converts = []
    for t in times:
        if ":" in t:
            minutes, rest = t.split(":")
            seconds, hundredths = rest.split(".")
        else:
            minutes = 0
            seconds, hundredths = t.split(".")
        converted_time = (int(minutes) * 60 * 100 + (int(seconds) * 100) + int(hundredths))
        converts.append(converted_time)
    average = statistics.mean(converts)
    min_secs, hundredths = str(round(average/100, 2)).split(".")
    min_secs = int(min_secs)
    minutes = int(min_secs) // 60
    seconds = min_secs - minutes * 60
    average = str(minutes) + ":" + str(seconds) + "." + hundredths
    return swimmer, age, distance, stroke, times, average

