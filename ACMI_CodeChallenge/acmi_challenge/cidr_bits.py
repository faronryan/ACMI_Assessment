'''
Created on Mar 29, 2018

@author: Faron Ryan
'''
 
# RFC 1878 - https://tools.ietf.org/html/rfc1878
NETMASK_LOOKUP_TABLE = ["128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0",
                        "248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0",
                        "255.128.0.0","255.192.0.0","255.224.0.0",
                        "255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0",
                        "255.255.0.0","255.255.128.0","255.255.192.0",
                        "255.255.224.0","255.255.240.0","255.255.248.0",
                        "255.255.252.0","255.255.254.0","255.255.255.0",
                        "255.255.255.128","255.255.255.192","255.255.255.224",
                        "255.255.255.240","255.255.255.248","255.255.255.252",
                        "255.255.255.254","255.255.255.255"]

class OutofBoundsError: # custom error
    pass

def netmask_to_bits(rawinput):
    try: 
        arr = map(int, rawinput.split('.')) 
        check_bounds(rawinput)
        # could have used a base-1 index of the lookup table
        result = [bin(x).count("1") for x in arr] 
        return sum(result)
    except ValueError:
        return -1
    except OutofBoundsError:
        return -1 
    
    return -1

def check_bounds(rawinput):
    if rawinput not in NETMASK_LOOKUP_TABLE:
        raise OutofBoundsError
    
    return True
        