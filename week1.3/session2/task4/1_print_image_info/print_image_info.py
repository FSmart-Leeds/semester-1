# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
with open("images/gradient.pgm") as f:
    contents = f.readlines()
# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)
print(contents[1].strip())
# print max gray value (i.e., Max Gray Value: max_gray_value)
print(contents[2].strip())
