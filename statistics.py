import math


def calculateStats(numbers):
    computedStatsDict = {}
    numLength = len(numbers)
    if numLength == 0:
        computedStatsDict = dict.fromkeys(["avg", "max", "min"], float(math.nan))
    else:
        computedStatsDict["avg"] = sum(numbers) / numLength
        computedStatsDict["max"] = max(numbers)
        computedStatsDict["min"] = min(numbers)
    return computedStatsDict

