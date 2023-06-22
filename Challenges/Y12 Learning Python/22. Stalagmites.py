# Stalactites or Stalagmites? Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.

# Create a function that determines whether the input represents "stalactites" or "stalagmites". If it represents both, return "both". Input will be a 2D list, with 1 representing a piece of rock, and 0 representing air space.

# Examples mineral_formation([ [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0] ]) ➞ "stalactites"
# mineral_formation([ [0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1] ]) ➞ "stalagmites"
# mineral_formation([ [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1] ]) ➞ "both"

# There won't be any examples where both stalactites and stalagmites meet (because those are called pillars).
# There won't be any example of neither stalactites or stalagmites.
# In other words, if the first list has 1s, return "stalactites".
# If the last list has 1s, return "stalagmites".
# If both have them, return "both".


def mineral_formation(list):
    return (
        "both"
        if 1 in list[0] and 1 in list[-1]
        else "stalactites"
        if 1 in list[0]
        else "stalagmites"
        if 1 in list[-1]
        else "none"
    )


print(mineral_formation_count([[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]))
print(mineral_formation_count([[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]))
print(mineral_formation_count([[1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]))

assert (
    mineral_formation([[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
    == "stalactites"
)
assert (
    mineral_formation([[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]])
    == "stalagmites"
)
assert (
    mineral_formation([[1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]])
    == "both"
)
