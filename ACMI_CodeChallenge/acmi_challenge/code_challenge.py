'''
Created on Mar 29, 2018

@author: Faron Ryan
'''

import re
import json

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
        print "Invalid character found in NETMASK!"
    except OutofBoundsError:
        return "Invalid NETMASK!"
    
    return -1 

def check_bounds(rawinput):
    if rawinput not in NETMASK_LOOKUP_TABLE:
        raise OutofBoundsError
    
    return True

def find_mac_address(filename, sys_stdin):
    matches = []
    i=1
    for line in sys_stdin:
        match = re.findall('[\\s]+[a-f0-9_]{2}:[a-f0-9_]{2}:[a-f0-9_]{2}:'+
                   '[a-f0-9_]{2}:[a-f0-9_]{2}:[a-f0-9_]{2}[\\s]+', 
                   line, re.IGNORECASE)
        if match:
            matches.append({filename: {'line['+str(i)+']':map(str.strip, match)}})
        i = i+1
                       
    return matches

def explodereport(rawinput):
    dumper = {}
    for line in rawinput:
        exploder_helper(line.split('|'), 0, dumper) 
    
    # use json dumper for desired print
    print json.dumps(dumper, indent=4, sort_keys=True)
    
    return dumper  

def exploder_helper(lst, index, hsh):
    
    if index < (len(lst) -1):
        if hsh.has_key(str(lst[index])):
            hsh[str(lst[index])] = exploder_helper(lst, index+1, 
                                                   hsh[str(lst[index])])
            return hsh
        else:
            hsh[str(lst[index])] = exploder_helper(lst, index+1, {})
            return hsh        
    else:
        return lst[index] 
    
    