# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except
try:
    with open("../images/gradient.pgm") as f:
        contents = f.readlines()
except:
    exit("The file was not found")
# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value
header = []
header.append(contents[0])
header.append(contents[1])
header.append(contents[2])
max_gray = int(contents[2].strip())
contents = contents[3:]

inverted_grid = []
for line in contents:
    newline = ""
    pixels = line.split()
    for pix in pixels:
        newline = newline + " " + str( max_gray - int(pix))
    newline = newline.strip()
    newline = newline + "\n"
    inverted_grid.append(newline)
    
# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"
with open("../images/invert_image.pgm", "w") as f:
    for line in inverted_grid:
        f.write(line)