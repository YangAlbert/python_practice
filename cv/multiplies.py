import string
for x in range(1, 11):
    print string.rjust(`x`, 2), string.rjust(`x*x`, 3),
    print string.rjust(`x*x*x`, 4)
