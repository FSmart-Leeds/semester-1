# Week 1.6, Session 1: Task 5

from datetime import datetime

from feed import QuakeFeed
from quake import Quake


class QuakeDatasetError(Exception):
    """
    An exception type for errors involving QuakeDataset.
    """


class QuakeDataset:
    """
    An earthquake dataset obtained from a USGS data feed.
    """

    def __init__(self, feed):
        """
        Creates an empty dataset, linked to a specific data feed.
        """
        if not isinstance(feed, QuakeFeed):
            raise TypeError("feed must be specified as a QuakeFeed object")

        self.feed = feed
        self.data = []

    def read_feed(self):
        """
        Refreshes this dataset with data from the linked feed.

        The new data replaces any existing data.
        """
        # Write code here to replace existing data with new earthquake data.
        # Use the value returned by the feed's reader() method as the
        # subject of a for loop.
        self.data = []
        for item in self.feed.reader():
            d = dict(item)
            time = d["time"]
            rawyear = time.split("T")[0]
            # this contains {year}-{month}-{day}
            year = rawyear.split("-")

            leftover = time.split("T")[1]
            rawtime = leftover.split(".")[0]
            # this contains {hour}:{min}:{second}
            time = rawtime.split(":")

            newdatetime = datetime(int(year[0]), int(year[1]), int(year[2]), int(time[0]), int(time[1]), int(time[2]))
            quake = Quake(newdatetime, float(d["longitude"]), float(d["latitude"]), float(d["depth"]), float(d["mag"]))
            self.data.append(quake)
        # Keep in mind that the items obtained by this for loop will be
        # dictionaries. You will need to extract the required values from
        # each dictionary and convert them into the required types before
        # creating a Quake object and storing it in the list.

    def __len__(self):
        """
        Returns the size of this dataset.
        """
        # Write code here that returns the number of quakes downloaded
        return len(self.data)

    def __str__(self):
        """
        Returns information on this dataset as a string.
        """
        # Write code here to create and return a string representation
        # (Include number of quakes and details of the feed that was used)
        return f"{self.feed} with {len(self)} recorded earthquakes "

    def mean_depth(self):
        """
        Returns the mean depth of the quakes in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.depth for quake in self.data)
        return total / len(self.data)

    def mean_magnitude(self):
        """
        Returns the mean magnitude of the quakes in this dataset.
        """
        # Write code here that computes the mean magnitude of all the
        # quakes currently in the dataset

        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")
        
        total = sum(quake.magnitude for quake in self.data)
        return total / len(self.data)

    def shallowest_quake(self):
        """
        Returns details of the shallowest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        shallowest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth < shallowest.depth:
                shallowest = quake
        return shallowest

    def strongest_quake(self):
        """
        Returns details of the strongest quake in this dataset.
        """
        # Write code here that finds and returns the strongest quake
        # (i.e., the one with the largest magnitude)

        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")
        
        deepest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth > deepest.depth:
                deepest = quake
        return deepest
