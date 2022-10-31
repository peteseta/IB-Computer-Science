class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = fname.capitalize() + " " + lname.capitalize()
        self.initials = fname[0].capitalize() + ". " + lname[0].capitalize()


a1 = Name("john", "smith")
print(a1.lname)
print(a1.fname)
print(a1.fullname)
print(a1.initials)
