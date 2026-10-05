# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

# Pretty-print the data structure

# Display details of one album recorded by a specific artist

music = {
    "The Cure" : ["Wish", "Disintegration", "The head on the door"],
    "Bad Brains" : ["Bad Brains", "Black Dots", "Rock for light"],
    "Title fight" : ["The last thing you forget", "Shed", "Floral Green"],
    "Destroy Boys" : ["Make Room", "Sorry, Mom", "Open mouth, Open heart", "Funeral soundtrack #4"],
    "Jack Off Jill" : ["Clear Hearts Grey Flowers", "Sexless demons and scars"]
}

pprint(music)
pprint(music.get("Bad Brains")[1])