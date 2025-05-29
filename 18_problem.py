def back_to_home(directions):
    south, north = directions.count("S"), directions.count("N")
    west, east = directions.count("W"), directions.count("E")
    
    return south == north and west == east

print(back_to_home("NNNN"), False)
print(back_to_home("NENESSWW"), True)
print(back_to_home("NEESSW"), False)
print(back_to_home("EEWE"), False)
print(back_to_home("NNSSEEEWWWEW"), True)
print(back_to_home("NNNNWW"), False)



'''
Back to Home?
Mubashir has started his journey from home. 
Given a string of directions (N=North, W=West, S=South, E=East),
he will walk for one minute in each direction. 
Determine whether a set of directions will lead him back to the starting position or not.

Examples
back_to_home("EEWE") ➞ False

back_to_home("NENESSWW") ➞ True

back_to_home("NEESSW") ➞ False
'''
