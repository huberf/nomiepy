import requests as r
import datetime
import json
import formatdate

class Nomie:
  url = ''
  username = ''
  def __init__(self, urlWithPort, username):
    if urlWithPort[0:4] == 'http':
      self.url = urlWithPort
    else:
      self.url = 'http://' + urlWithPort
    self.username = username

  def setup(self):
    self.saveTrackers()
    return True

  def getTrackers(self):
    response = r.get(self.url + '/' + self.username + '_trackers/_all_docs')
    ids = json.loads(response.text)
    trackerNames = []
    for i in ids['rows']:
      trackerDetails = r.get(self.url + '/' + self.username + '_trackers/' + i['id']);
      details = json.loads(trackerDetails.text)
      trackerNames += [{'id': i['id'], 'label': details['label'], 'type': details['config']['type']}]
    return trackerNames

  def getAllEvents(self):
    response =  r.get(self.url + '/' + self.username + '_events/_all_docs')
    return response.text

  def cache(self):
    listOfEvents = self.eventList()
    textToPut = json.dumps(listOfEvents)
    cacheFile = open('event_cache.json', 'w')
    cacheFile.write(textToPut)
    cacheFile.close()

  def backup(self, filename):
    listOfEvents = self.getAllEvents()
    fileToWrite = open(filename, 'w')
    fileToWrite.write(listOfEvents)

  def eventObjects(self):
    objects = json.loads(self.getAllEvents())
    return objects

  def saveTrackers(self):
    allTrackers = self.getTrackers()
    trackers = {}
    for i in allTrackers:
      trackers[i['id']] = i['label']
    trackers = json.dumps(trackers)
    fileToWrite = open('trackernames.json', 'w')
    fileToWrite.write(trackers)

  def getName(self, id):
    fileOfNames = open('trackernames.json', 'r')
    contents = fileOfNames.read()
    names = json.loads(contents)
    try:
        return names[id]
    except:
        return 'deleted'

  def eventList(self):
    items = self.getAllEvents()
    items = json.loads(items)
    for i in range(len(items['rows'])):
      idName = items['rows'][i]['id']
      if idName[5:7] == 'pr':
        timeOf = items['rows'][i]['id'].split('|')[3]
        items['rows'][i]['name'] = self.getName(items['rows'][i]['id'].split('|')[2])
        items['rows'][i]['time'] = timeOf
        dateOf = datetime.datetime.fromtimestamp(float(timeOf)/1000.0)
        dateFormatter = formatdate.FormatDate()
        strDate = dateFormatter.format(dateOf.year, dateOf.month, dateOf.day, dateOf.hour, dateOf.minute, dateOf.second)
        items['rows'][i]['date'] = strDate
      elif idName[5:7] == 'tm':
        timeOf = items['rows'][i]['id'][8:21]
        items['rows'][i]['name'] = self.getName(items['rows'][i]['id'][22:42])
        items['rows'][i]['time'] = timeOf
        dateOf = datetime.datetime.fromtimestamp(float(timeOf)/1000.0)
        dateFormatter = formatdate.FormatDate()
        strDate = dateFormatter.format(dateOf.year, dateOf.month, dateOf.day, dateOf.hour, dateOf.minute, dateOf.second)
        items['rows'][i]['date'] = strDate
      else:
        print "Unknown case!!!!!"
    return items

def test_module():
    print("Success...")
