# Week 1.6, Session 1: Task 5
from feed import QuakeFeed
from dataset import QuakeDataset
from quake import Quake
# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like
sig = input("Significance level: ")
time = input("Time period: ")
feed = QuakeFeed(sig, time)
data = QuakeDataset(feed)
data.read_feed()
print(data)
print(f"mean depth is {data.mean_depth():.3f}")
print(f"mean magnitude is {data.mean_magnitude():.3f}")

strongest_quake = data.strongest_quake()
print(strongest_quake)