# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

sequence = []
while L > 0:
    if sequence == []:
        sequence.append(0)
    else:
        number = sequence[len(sequence) - 1] - len(sequence)
        if number < 0 or number in sequence:
            number = sequence[len(sequence) - 1] + len(sequence)
        sequence.append(number)
    L = L - 1

# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence