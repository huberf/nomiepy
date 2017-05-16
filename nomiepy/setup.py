import __init__ as n

######################################
# Modify the Server URL and Username #
######################################

# For example http://10.10.10.10:5984
serverUrl = ''

# For example nomie
username = ''

h = n.Nomie(serverUrl, username)
h.saveTrackers()
