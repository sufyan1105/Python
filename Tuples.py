#  Tuples are Immutable just like strings. Lists are Mutable

Tup = (12,13,14,15,13)
print(type(Tup))


print(Tup.index(13)) # Returns the index of the first occurence of the element
print(Tup.count(13)) # Returns the number of occurences of the element
