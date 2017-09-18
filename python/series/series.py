def slices(string, interval):
    if interval > len(string) or interval == 0:
        raise ValueError

    i = 0
    seriesList = []
    while i <= (len(string) - interval):
        # Use list comprehension to generate lists of series
        series = [int(string[j]) for j in range(i, i + interval, 1)]
        seriesList.append(series)
        i += 1

    return seriesList
