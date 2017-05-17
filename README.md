# nomiepy
A minimal python library for accessing Nomie data stored in CouchDB.

## Setup
* First, `pip install nomiepy`
* Now, you will just need your Mongo DB URL and the username for that DB.
* To test open up the Python shell or write a short script using instructions below.
* Instantiate a Nomie object like so `myNomie = nomiepy.Nomie('db url', 'username')
* For speed, one must cache the trackers in whatever directory you are computing in. To do this you need to run the following command using the object instantiation above. Do this by running `myNomie.saveTrackers()`
* You are now ready to use any of the available methods.

## Basic Operations
* To get a list of every single event you tracked, the `eventList` function is
  here to help. After creating an instance of the Nomie class as done in the
  `setup.py` file, you can query all trackers by simply calling this function.
  (e.g. `alLEvents = nomie.eventList()`)
* This will include the names of the trackers, so you can easily use a for loop
  to check for everytime you did a specific action as well as view the time it
  happened.

## (Optional) Setup from source
* First clone this repository with `git clone https://github.com/huberf/nomiepy`
* To setup your trackers, you will need to open the `setup.py` file and fill in
  the URL for you CouchDB instance as well as the username you have. No password
  is required. Make sure to include the port in your URL.
* After setting up that file, run `python setup.py`. The `trackernames.json` file should be located in
  your clone directory. Check it out and make sure all your trackers are located
  there.
* Congratulations, you are now ready to start querying your Nomie data on
  demand.

More operations and functionality will be added as I find the time. If you have
ideas or want to contribute feel free to open a PR or an issue.
