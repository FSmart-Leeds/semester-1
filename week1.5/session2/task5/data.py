# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        with open(filename) as f:
            data = f.readline()
        add = True
        current = ""
        for s in data:
            if s == '[' or s == ']' or s == ' ':
                continue
            if s == ',':
                add = True
                continue
                        
            if add:
                self.data.append(int(current+s))
            else:
                current = current+s

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        return (sum(self.data) / len(self.data))

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        templist = []
        for item in self.data:
            templist.append(item)
        templist.sort()
        if len(templist) % 2 == 0:
            return (templist[(len(templist) / 2) - 1] + templist[len(templist) / 2]) / 2
        else:
            return (templist[(len(templist) // 2)])
