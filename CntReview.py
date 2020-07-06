'''
@File:      CntReview.py
@Time:      6/2/2020
@Author:    Zhou Wei
@Version:   1.0
@Contact:   Wei.ZHOU10@cn.bosch.com
'''


from openpyxl import load_workbook
from openpyxl import workbook
from openpyxl import worksheet
from global_definition import *

import os

#if new file name is empty, the default file is original one which means no new file will be created.
NEW_FILE_NAME = 'RESULT.xlsm'

class CntReview:
    
    def __init__(self,file,sheet):
        self.filePath = file
        self.sheetName = sheet
        try:
            self.wb = load_workbook(self.filePath, keep_vba = True)
        except FileNotFoundError:
            #print("please make sure the file 'PDM_Collection_and_Review.xlsx' is already in the current directory")
            raise FileNotFoundError
            

    def _loadSheet(self):
        sheet = self.wb[self.sheetName]
        #sheet.active()
        return sheet
        
    def _saveFile(self, toPath = ''):
        
        if toPath == '' or toPath == None:
            self.wb.save(self.filePath)
        else:
            self.wb.save(toPath)
                

    def loadDataFromCnt(self,content, element_num):
        sheet = self._loadSheet()
        for i in range(0,element_num - 1):
            #print(content[i])
            string = data_mapping_to_excel_dict[DATA_ID] + str(i + start_from_rowNo)
            #print(string)
            sheet[string] = content[i][DATA_ID]
            string = data_mapping_to_excel_dict[DATA_COMPONENT] + str(i + start_from_rowNo)
            sheet[string] = content[i][DATA_COMPONENT]
            string = data_mapping_to_excel_dict[DATA_BLOCK_NAME] + str(i + start_from_rowNo)
            sheet[string] = content[i][DATA_BLOCK_NAME]
            string = data_mapping_to_excel_dict[DATA_SIZE] + str(i + start_from_rowNo)
            sheet[string] = content[i][DATA_SIZE]
        self._saveFile(NEW_FILE_NAME)

    def setSWVersion(self, epk):
        sheet = self._loadSheet()
        sheet[EXCEL_SW_VERSION] = epk
        self._saveFile(NEW_FILE_NAME)
