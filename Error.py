'''
@File:      Error.py
@Time:      5/21/2020
@Author:    Zhou Wei
@Version:   1.0
@Contact:   Wei.ZHOU10@cn.bosch.com
'''

class Error:

#key: location / which item
#value: status
    
    __errors = {}

    @staticmethod
    def getErrors():
        return Error.__errors
    
    @staticmethod
    def getErrorsLocation():
        pass
        #return self.errors
    
    @staticmethod
    def getErrorsStauts():
        pass
        #return self.errors_status
    
    @staticmethod
    def appendErrors(loc, stat):
        Error.__errors[loc] = stat
        
    @staticmethod
    def isErrorExisted():
        if len(Error.__errors) == 0:
            return False
        else:
            return True

'''
class Error:

#key: location / which item
#value: status
    __errors = {}

    @staticmethod
    def getErrors(self):
        return self.errors

    def getErrorsLocation(self):
        pass
        #return self.errors
    
    def getErrorsStauts(self):
        pass
        #return self.errors_status

    def appendErrors(self, loc, stat):
        self.errors[loc] = stat

    def isErrorExisted(self):
        if len(self.errors) == 0:
            return False
        else:
            return True'''
