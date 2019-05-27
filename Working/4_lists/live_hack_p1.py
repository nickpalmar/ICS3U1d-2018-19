
def wind_chill(temps, wspeed):
    """

    :param temps:
    :param wspeed:
    :return:
    """
    for i in range(len(temps)):
        wind_chill_t = 13.12 + 0.6125 * temps[i] - 11.37 * wspeed * 0.16 + 0.3965 * temps[i] * wspeed * 0.16
        temps[i] = wind_chill_t

    return temps

temperatures = input("Enter temperatur").split()
w_chill_temps =

