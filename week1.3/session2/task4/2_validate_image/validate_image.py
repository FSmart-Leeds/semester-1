# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value
with open("images/gradient.pgm") as f:
    contents = f.readlines()
width, height = contents[1].strip().split(" ")
gmax = int(contents[2].strip())

contents = contents[3:]
# checks if they are correct true if they are
Bheight = True
Bwidth = True
Bpixel_values = True

if len(contents) != int(height):
    Bheight = False

for line in contents:
    pixels = line.split()
    if len(pixels) != int(width):
        Bwidth = False
    for pixel in pixels:
        if int(pixel) < 0 or int(pixel) > gmax:
            Bpixel_values = False

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

if Bwidth and Bheight and Bpixel_values:
    print("Valid image")

if not Bwidth:
    print("Invalid width")
if not Bheight:
    print("Invalid height")
if not Bpixel_values:
    print("Invalid pixel values")