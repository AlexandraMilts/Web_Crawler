# Example 1
# marker = "AFK"
#replacement = "away from keyboard"
#line = "I will now go to sleep and be AFK until lunch time tomorrow."

#Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

length = len(marker)
start = line.find(marker)
to_replace = line [start:start+length]
end = start + length
replaced = line[0:start] + replacement + line[end:]
print(replaced)