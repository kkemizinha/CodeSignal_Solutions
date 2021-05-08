def centuryFromYear(year):
    if year <= 100:
       return 1
    result = divmod(year, 100)
    if result[1] == 0:
       return result[0]
    else:
       return result[0] + 1