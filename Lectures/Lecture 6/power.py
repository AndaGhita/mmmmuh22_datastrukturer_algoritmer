
# Basfall
# power(4,1) -> returnera 4
# power(4,0) -> returnera 1

# power(4,n=2) -> returnera 4*power(4,n-1)

import math

def power_funktion(x,n):
    if x == 0:
        return 0
    else:
        return pow(x,n)

print(power_funktion(4,6))
