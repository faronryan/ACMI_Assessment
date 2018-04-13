'''
Created on Mar 30, 2018

@author: Faron Ryan
'''

class CustomDict(object):
    '''
    Inheriting from Application is shorter than writing an explicit main
    method, but it also has some shortcomings. First, you can't use this trait if
    you need to access command line arguments, because the arguments array isn't
    available. For example, because the Summer application uses command-line
    arguments, it must be written with an explicit main method, as shown in Listing
    4.3. Second, because of some restrictions in the JVM threading model,
    you need an explicit main method if your program is multi-threaded. Finally,
    some implementations of the JVM do not optimize the initialization code of
    an object which is executed by the Application trait.
    '''

    def __init__(self, params):
        '''
        Constructor 
         Accept key value pairs
        '''
        temp = params.split(',')
        self.history = {}
        for key_value in temp:
            key = key_value.split('=>')[0].strip()
            value = key_value.split('=>')[1].strip().replace("'","") \
                                            .replace('"','')
            setattr(self, key, value)
    
    def get(self, key): # not in spec but was suggested in test case
        return getattr(self, key)
        
    def add(self, key_value):
        key = key_value.split('=>')[0].strip()
        value = key_value.split('=>')[1].strip().replace("'","") \
                                        .replace('"','')
        setattr(self, key, value)
        self.history[key] = 'ADD '+str(key)+' = '+value
             
    def delete(self, key):
        delattr(self, key)
        self.history[key] = 'DELETE '+str(key)
    
    def modify(self, key_value):
        key = key_value.split('=>')[0].strip()
        value = key_value.split('=>')[1].strip().replace("'","") \
                                        .replace('"','')
        setattr(self, key, value)
        self.history[key] = 'MODIFY '+str(key)+' = '+value
    
    def deltas(self):
        for key, value in self.history.iteritems():
            print(value)
        return self.history
        