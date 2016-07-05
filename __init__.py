import requests as r
import json

class Nomie:
  url = ''
  def __init__(self, urlWithPort):
    if urlWithPort[0:4] == 'http':
      self.url = urlWithPort
    else:
      self.url = 'http://' + urlWithPort

  def getAllEvents(self):
    response =  r.get(self.url + '/nomie_events/_all_docs')
    return response.text
  
  def getAllTrackers(self):
    response =  r.get(self.url + '/nomie_trackers/_all_docs')
    return response.text

  def backup(self, filename):
    listOfEvents = self.getAllEvents()
    fileToWrite = open(filename, 'w')
    fileToWrite.write(listOfEvents)

  def eventObject(self):
    objects = json.loads(self.getAllEvents())
    return objects
  
  def saveTrackers(self):
    trackers = self.getAllTrackers()
    fileToWrite = open('trackers.json', 'w')
    fileToWrite.write(trackers)

  def getName(self, id):
    fileOfNames = open('trackernames.json', 'r')
    contents = fileOfNames.read()
    names = json.loads(contents)
    return names[id]

  def eventList(self):
    items = self.getAllEvents()
    items = json.loads(items)
    for i in range(len(items['rows'])):
      idName = items['rows'][i]['id']
      if idName[5:7] == 'pr':
        timeOf = items['rows'][i]['id'][29:42]
        items['rows'][i]['name'] = self.getName(items['rows'][i]['id'][8:28])
        items['rows'][i]['time'] = timeOf
      elif idName[5:7] == 'tm':
        timeOf = items['rows'][i]['id'][8:21]
        items['rows'][i]['name'] = self.getName(items['rows'][i]['id'][22:42])
        items['rows'][i]['time'] = timeOf
      else:
        print "Unknown case!!!!!"
    return items
