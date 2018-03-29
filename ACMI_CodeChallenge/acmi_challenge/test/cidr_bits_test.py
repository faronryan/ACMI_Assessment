'''
Created on Mar 29, 2018

@author: Faron Ryan
'''
import unittest
import acmi_challenge.cidr_bits as cb

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

if __name__ == "__main__":
    unittest.main()