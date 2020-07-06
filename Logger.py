'''
@File:      Logger.py
@Time:      5/21/2020
@Author:    Zhou Wei
@Version:   1.0
@Contact:   Wei.ZHOU10@cn.bosch.com
'''

import logging

class Logger:

    @staticmethod
    def init():
        logging.basicConfig(filename = 'CNT.log', level = logging.DEBUG)

    @staticmethod
    def recordLog(message, printOnScreen = False):
        
        logging.debug(message)
        if printOnScreen == True:
            print(message)
