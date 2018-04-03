'''
Created on Mar 29, 2018

@author: Faron Ryan
'''
import unittest
import acmi_challenge.code_challenge as cb
import acmi_challenge.custom_dict as cd
import os

INPUT_DIR = "../inputs/"

class Test(unittest.TestCase):
    
    def testCidrBitsPass(self):
        rawinput = "255.255.252.0"
        result = cb.netmask_to_bits(rawinput)
        expected = 22
        self.assertEqual(expected, result, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
    def testCidrBitsFailValueError(self):
        rawinput = "255.1.2.x"
        result = cb.netmask_to_bits(rawinput)
        expected = -1
        self.assertEqual(expected, result, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
    
    def testCidrBitsFailOutofBoundsError(self):
        rawinput = "255.1.2.3" 
        result = cb.netmask_to_bits(rawinput)
        expected = -1
        self.assertEqual(expected, result, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
    def testCheckBounds(self):
        rawinput = "255.255.0.0" 
        result = cb.check_bounds(rawinput)
        expected = True
        self.assertEqual(expected, result, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
    def testFindMacAddresFile1(self):
        for filename in os.listdir(INPUT_DIR):            
            # rawinput = open(INPUT_DIR+"inputs01.txt", "r")
            rawinput = open(INPUT_DIR+filename, "r") 
            result = cb.find_mac_address(filename,rawinput)
            
            if(filename == "inputs01.txt"): # just checking one file in the 
                                            # directory; more can be addeded
                # print filename, result
                expected = [{'inputs01.txt': {'line[1]': 
                                              ['AA:BB:CC:DD:EE:FF', 'AA:BB:CC:DD:EE:FF']}},
                             {'inputs01.txt': {'line[3]': ['BA:BC:CC:DD:EE:FF']}}, 
                             {'inputs01.txt': {'line[5]': ['CC:BB:CC:DD:EE:DD']}}, 
                             {'inputs01.txt': {'line[7]': ['DE:AD:BE:EF:AA:CC']}}, 
                             {'inputs01.txt': {'line[23]': ['BE:DE:AD:BE:EF:AA']}}, 
                             {'inputs01.txt': {'line[26]': ['AA:BB:CC:DD:EE:FF']}}]
                self.assertEqual(expected, result, 
                             'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
    
    def testNestedHashConstructor(self):
        rawinput = ['app1|server1|uptime|5', 
                    'app1|server1|loadavg|0.01 0.02 0.03',
                    'app1|server1|conn1|state|up', 
                    'app1|server2|uptime|10', 
                    'app1|server2|loadavg|0.11 0.22 0.33', 
                    'app1|server2|conn1|state|down', 
                    'app1|running|true', ]
        result = cb.explodereport(rawinput)
        expected = {'app1': {'running': 'true', 
                             'server1': {'uptime': '5', 
                                         'loadavg': '0.01 0.02 0.03', 
                                         'conn1': {'state': 'up'}}, 
                             'server2': {'uptime': '10', 
                                         'loadavg': '0.11 0.22 0.33', 
                                         'conn1': {'state': 'down'}}}}
 
        self.assertEqual(expected, result, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
        
    def testCustomDictConstructorInit(self):
        # Tricky, because I could just use the internal dict syntax 
        # but I used a string to keep the input format
        # just one extra step. Also, could have a wild card on 
        # input parameters, another step to parse a **params array.
        rawinput = "deer => 'park', foo => 'bar', this => 'that'" 
        result = cd.CustomDict(rawinput)
        expected = 'that'
        self.assertEqual(expected, result.this, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
        expected = 'park'
        self.assertEqual(expected, result.deer, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
        expected = 'bar'
        self.assertEqual(expected, result.foo, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
    
    def testCustomDictConstructorModifiers(self):
        rawinput = "deer => 'park', foo => 'bar', this => 'that'"
        result = cd.CustomDict(rawinput)
        result.delete('this'); 
        result.add("gnu => 'linux'"); 
        result.modify("gnu => 'not unix'"); 
        print result.get('gnu') 
        result.modify("deer => 'venison'"); 
        result.modify("gnu => 'emacs'"); 
        result.deltas; 
        expected = 'emacs'
        self.assertEqual(expected, result.gnu, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
        expected = 'bar'
        self.assertEqual(expected, result.foo, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
        res = result.deltas()
        expected = {'this': 'DELETE this', 'deer': 'MODIFY deer = venison', 
                    'gnu': 'MODIFY gnu = emacs'}
        self.assertEqual(expected, res, 
                         'Error: expected %s, received %s'% (str(expected),
                                                             str(result)))
        
if __name__ == "__main__":
    unittest.main()