first_names = [
    "John",
    "Paul",
    "George",
    "Ringo",
    "Pete",
    "Stuart",
    "Mick",
    "Keith",
    "Ronnie",
    "Charlie",
    "Brian",
    "Roger",
    "John",
    "Paul",
    "Bob",
    "Ringo",
    "Pete",
    "Stuart",
    "Mick",
    "Biff",
    "Ronnie",
]

only_b_names = [name for name in first_names if name.startswith("B")]
print(only_b_names)
