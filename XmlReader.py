'''
@File:      XmlReader.py
@Time:      5/21/2020
@Author:    Zhou Wei
@Version:   1.0
@Contact:   Wei.ZHOU10@cn.bosch.com
'''

import xml.etree.ElementTree as ETree

from Error import *
import os
import time
from global_definition import *

cnt_element_name = ['EE_ID','EE_NAME','EE_Component']

DATA_Dict = {}

#  Format
# [
#    {ID, COMPONENT, NAME, DATA_SIZE},
#    {ID, COMPONENT, NAME, DATA_SIZE},
#    ...
# ]

DataBlock_Dict = []

DataBlock_ID_List = []
#DataBlock_Dict[DATA_BLOCK_NAME] = {}
#DataBlock_Dict[DATA] = {}

LIST_TYPE_ID = 1
LIST_TYPE_COMPONENT = 2
LIST_TYPE_BLOCK = 3
DataBlock_ID_List = []
DataBlock_COMPONENT_List = []
DataBlock_BLOCK_List = []



            
class XmlReader:
    
    def __init__(self,file):
        self.filePath = file
        try:
            self.tree = ETree.parse(self.filePath)
        except FileNotFoundError:
            #print("please make sure the file 'EEPROM_Container.cnt' is already in the current directory")
            raise FileNotFoundError
            
        self.max_element_number = 0
        self.root = self.tree.getroot()
        #self._init_dict(152);
        
    #remove suffix
    def substring(text, split_point):
        idx = text.find(split_point)
        return text[:idx]

    def _init_dict(self, length):
        for i in range (0,length):
            DataBlock_Dict.append({})
    
    def read(self):
        mem = self.root.find('MEM')
        datablocks = mem.findall(DATA_BLOCK)
        self._init_dict(len(datablocks))
        j = 0;
        for block in datablocks:
            block_name = block.find(DATA_BLOCK_NAME).text
            idx = block_name.find(SUBSTRING_EXCLUDE_STRING)
            if idx < 0:
                continue
                    
            DataBlock_Dict[j][DATA_BLOCK_NAME] = block_name[:idx]

            if 'NvM_ConfigId' in block_name:
                #DataBlock_Dict[j][DATA_BLOCK_NAME] = block_name[:idx]
                data = block.findall(DATA)
                DataBlock_Dict[j][DATA_ID] = data[NVM_CONFIGID_ID_INDEX].text[ID_START_INDEX:]
                DataBlock_Dict[j][DATA_COMPONENT] = 'CSW'
                DataBlock_Dict[j][DATA_SIZE] = data[NVM_CONFIGID_ID_INDEX + 5].text[DATA_SIZE_START_INDEX:]
                j = j + 1
                continue
                    
            #print(DataBlock_Dict[j])
            i = 0
            for data in block.findall(DATA):
                if i == DATA_ID_INDEX:
                    DataBlock_Dict[j][DATA_ID] = data.text[ID_START_INDEX:]
                elif i == DATA_COMPONENT_INDEX:
                    content = data.text
                    idx1 = content.find(':')
                    idx2 = content.find('\n')
                    DataBlock_Dict[j][DATA_COMPONENT] = content[idx1 + 1:idx2]
                elif i == DATA_SIZE_INDEX:
                    DataBlock_Dict[j][DATA_SIZE] = data.text[DATA_SIZE_START_INDEX:]
                else:
                    pass
                i = i + 1
            #print(DataBlock_Dict[0][DATA_BLOCK_NAME])
            j = j + 1
        
        self.max_element_number = j + 1

    # @1 praram: string - content of ID, component name or block name
    # @2 praram: typeStr - what will the list store. ID, component name or block name
    def setList(string, typeStr):

        if typeStr == LIST_TYPE_ID:
            DataBlock_ID_List[j] = string
        elif typeStr == LIST_TYPE_COMPONENT:
            DataBlock_COMPONENT_List[j] = string
        elif typeStr == LIST_TYPE_BLOCK:
            DataBlock_BLOCK_List[j] = string
        else:
            pass
        

        
    def getEPK(self):
        data_block_list = self.root.find('MEM').findall(DATA_BLOCK)
        epk = ''
        for block in data_block_list:
            name = block.find(DATA_BLOCK_NAME).text
            if name == EEPROM_METADATA:
                data_list = block.findall(DATA)
                epk = data_list[DATA_EPK_INDEX].text
                epk = epk[4:]
                print(epk)
        return epk

    def getUseCases():
        pass
                
    def sortWhileadding(DataBlock_Dict, new_element):
        #if(DataBlock_Dict[0][DataBlock_Dict] < new_elment[DATA_ID]
        pass
    
    def sort_key(self, array):
        try:
            val = array[DATA_ID]
        except KeyError:
            return 9999999
            
        return int(val)
    
    def sort(self, result_array):
        result_array.sort(key=self.sort_key)
        #print(result_array)
        #pass


