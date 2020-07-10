class Pupils:
    # Private attributes
    def __init__(self, name, age, contact):
        self.__name = name
        self.__age = age
        self.__contact = contact

    def __displayDetails(self): # NB this can't be access directory
        results = f"""
            Name:{self.__name},
            Age: {self.__age},
            Contact: {self.__contact}"""
        return results

    def accessprivate(self):
        return self.__displayDetails()

pupil = Pupils('linux', 24, 551519828)
print(pupil.accessprivate())
