# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name:str, birth:date):
        """
        Creates a person with the attributes name and date
        """
        if not isinstance(name, str):
            raise TypeError("name is not a str")
        if name == "":
            raise ValueError("name is empty")
        if not isinstance(birth, date):
            raise TypeError("birth is not a date")
        self.name = name
        self.birth = birth
    def initials(self):
        """
        Returns a string containing the initials of the name
        """
        words = self.name.split()
        initials = ""
        for word in words:
            initials = initials + word[0].upper()
        return initials
    def is_birthday(self):
        """
        Returns true if the persons birthday is today, false if not
        """
        today = date.today()
        if today == self.birth:
            return True
        return False

p = Person("Freddie William Smart", date(2026,10,30))
print(p.initials())
print(p.is_birthday())