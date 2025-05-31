string = "OIZEHSGLB"

def turn_calc(n):
    
    return ''.join([string[int(i)] for i in str(n)[::-1] if i != "."])

print(turn_calc(0.7734), "HELLO", "convert the numbers into corresponding letters.")
print(turn_calc(3045), "SHOE", "convert the numbers into corresponding letters.")
print(turn_calc(5508), "BOSS")
print(turn_calc(707), "LOL")
print(turn_calc(57108), "BOILS")
print(turn_calc(3781637), "LEGIBLE")
print(turn_calc(35380), "OBESE")
print(turn_calc(461375), "SLEIGH")
print(turn_calc(5355378), "BLESSES")
print(turn_calc(38076), "GLOBE")
print(turn_calc(35006), "GOOSE")
print(turn_calc(8075), "SLOB")

# Hidden Calculator Words
# At school, we used to play with our calculators and send each other secret messages. 
# The trick was to enter a special number and turn the calculator upside-down. LOL ... I mean 707!

# Given a number, create a function that converts it into 
# a word by turning the integer 180 degrees around.

# Examples

# turn_calc(707) ➞ "LOL"

# turn_calc(5508) ➞ "BOSS"

# turn_calc(3045) ➞ "SHOE"
# number	letter
# 1	I
# 2	Z
# 3	E
# 4	H
# 5	S
# 6	G
# 7	L
# 8	B
# 9	-
# 0	O
# Notes

# Convert to uppercase words.
# Ignore dots.
