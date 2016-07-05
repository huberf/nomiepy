class FormatDate:
  def format(self, year, month, day, hour=0, minute=0, second=0):
    toReturn = ''
    if int(year) < 100:
      toReturn += '20' + str(year)
    else:
      toReturn += str(year)

    toReturn += '-'

    if month < 10:
      toReturn += '0' + str(month)
    else:
      toReturn += str(month)

    toReturn += '-'

    if day < 10:
      toReturn += '0' + str(day)
    else:
      toReturn += str(day)

    toReturn += 'P'

    if hour < 10:
      toReturn += '0' + str(hour)
    else:
      toReturn += str(hour)

    toReturn += ':'

    if minute < 10:
      toReturn += '0' + str(minute)
    else:
      toReturn += str(minute)

    toReturn += ':'

    if second < 10:
      toReturn += '0' + str(second)
    else:
      toReturn += str(second)

    toReturn += '.000-06:000'

    return toReturn
