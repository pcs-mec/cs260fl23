from icecream import ic

class Student():
    def __init__(self, name, sid, ssn):
        self.name = name
        self.sid = sid
        self.ssn = ssn


    def __eq__(self, other):
        # return self.ssn == other.ssn
        """ better way """
        if isinstance(other, self.__class__):
            return self.sid == other.sid and self.ssn == other.ssn
        return NotImplemented
    
    def __hash__(self):
        return hash((self.sid, self.ssn ))
        # warning overloading hash must be done with care
        # hash is like a fingerprint: 
        # only hash information that will not change for the object

    def __repr__(self):
        return f'{self.name} {self.sid} {self.ssn}'

s1 = Student(name = 'jane', sid = 1, ssn = "555-22-2123")
s2 = Student(name = 'jon', sid = 2, ssn = "555-33-5523")
s3 = Student(name = 'Oki', sid = 3, ssn = "555-44-5555")
_s1 = Student(name = 'jane', sid = 1, ssn = "555-22-2123")

# s1,_s1 are different objects, but have same information.
# what if you need to be able to compare two objects:
#    such that return True if information is the same
# overload __eq__, 


##########################################################
# what if you wanted to take full advantage of set()
my_set = set([s1,s3])
ic(my_set)
print('add _s1 into the set')
my_set.add(_s1)
ic(my_set)

# see overloaded __hash__() method with a WARNING


