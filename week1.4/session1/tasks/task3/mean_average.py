#- accept a list of integers and returns the mean average of the list.​
def mean_average(nums):
    return (sum(nums)/len(nums))

userin = (input("Enter nums: ")).split(" ")
userin = [int(s) for s in userin]
print(f"Mean average is: {mean_average(userin)}")