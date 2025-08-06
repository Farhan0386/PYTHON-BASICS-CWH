#  Can you change the values inside a list which is contained in set S 
s = {8, 7, 12, "Harry", [1, 2]}  # This will raise: TypeError: unhashable type: 'list'
# No, because lists are mutable and cannot be added to a set.   
