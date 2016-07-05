import csv

csvfile = open('csv_export.csv')
output = csv.reader(csvfile)

trackernames = []
firstHit = True
for i in output:
  if firstHit:
    firstHit = False
  else:
    indexToInsert = -1
    for a in range(len(trackernames)):
      if trackernames[a][0] == i[5]:
        indexToInsert = a
    if indexToInsert == -1:
      trackernames += [[i[5], i[6]]]
    else:
      trackernames[indexToInsert] = [i[5], i[6]]

print trackernames

toreturn = '{\n'
for i in trackernames:
  toreturn += '"' + str(i[1]) + '": "' + str(i[0]) + '",\n'

toreturn += '}'

outputfile = open('trackernames.json', 'w')
outputfile.write(toreturn)
