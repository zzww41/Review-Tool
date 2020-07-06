'''
@File:      global_definition.py
@Time:      5/21/2020
@Author:    Zhou Wei
@Version:   1.0
@Contact:   Wei.ZHOU10@cn.bosch.com
'''


'''--------------------------------
   ---------EXCEL Definition-------
   --------------------------------'''

EXCEL_DATA_ID = 'A'
EXCEL_BLOCK_NAME = 'B'
EXCEL_COMPONENT = 'C'
EXCEL_SIZE = 'D'
EXCEL_VALUE = 'E'
EXCEL_DELIVERY = 'I'
EXCEL_RESET_TO_DELIVERY = 'J'
EXCEL_REPROG = 'K'
EXCEL_SW_VERSION = 'B4'

DATA_COMPONENT = 'COMPONENT'
DATA_SIZE = 'DATA_SIZE'

start_from_rowNo = 12    #first item of EEPROM is right at Row 12, if excel template is changed, this value should be taken care

'''-----------------------------------
   ----------CNT Definition-----------
   -----------------------------------'''

DATA_BLOCK_NAME = 'DATABLOCK-NAME'
DATA_VALUE = 'DATA'
DATA = 'DATA'
DATA_ID = 'ID'
DATA_SIZE = 'SIZE'
SESSION_DELIVERY = 'DeliveryState'
SESSION_RESET_TO_DELIVERY = 'ResetToDeliveryState'
SESSION_REPROG = 'Reprg'

#index of id, component, size in <data> list in cnt file
#<data></data>
#<data></data>
#<data></data>
#...
DATA_ID_INDEX = 1
DATA_COMPONENT_INDEX = 5
DATA_SIZE_INDEX = 7

DATA_POINTER_NAME = 'DATAPOINTER-NAME'
DATA_BLOCK = 'DATABLOCK'

USE_CASE_RESET = 0
USE_CASE_DELIVERY = 1
USE_CASE_REPROG = 2
USE_CASE_MAPPING = ['ResetToDeliveryState', 'DeliveryState', 'ECUReprogramming']


#used to find the index to add new data blocks  (definded as data_block_template)
SEARCH_BY_TEXT = '__Metadata'
#used to tell if new data blocks need to be created and inserted
TEXT_VALUE_EXSIT = '__Org'


SUBSTRING_EXCLUDE_STRING = '__Metadata'
EEPROM_METADATA = '__EEPROM_METADATA__'  #the name of the block where to get EPK
DATA_EPK_INDEX = 1 #the index where we can find EPK in the <DATA> list

#<DATA>id=xxx</DATA>
#get id from index 3
#if CNT format has changed, like the way to getting id, this number may have to be changed.
ID_START_INDEX = 3

#<DATA>data_size=XX</DATA>
DATA_SIZE_START_INDEX = 10

#NVM_CONFIG_ID is a special item in XML file (.cnt) which needs to be handled with a special WAY
NVM_CONFIGID_ID_INDEX = 0



'''-------------------------------------------------
   ---------CNT tag/element And EXCEL column Mapping Definition--------
   -------------------------------------------------'''
data_mapping_to_cnt_dict = {DATA_BLOCK_NAME:EXCEL_BLOCK_NAME, DATA_ID:EXCEL_DATA_ID, DATA_SIZE:EXCEL_SIZE, DATA_VALUE:EXCEL_VALUE, SESSION_DELIVERY:EXCEL_DELIVERY,
                            SESSION_RESET_TO_DELIVERY:EXCEL_RESET_TO_DELIVERY, SESSION_REPROG:EXCEL_REPROG}


data_mapping_to_excel_dict = {DATA_BLOCK_NAME:EXCEL_BLOCK_NAME, DATA_ID:EXCEL_DATA_ID, DATA_COMPONENT:EXCEL_COMPONENT, DATA_SIZE:EXCEL_SIZE}


'''----------------------------------
   ---------CNT Write Template-------
   ----------------------------------'''

#1st param: block name
#2nd param: <DATA></DATA> ... depending on the size of bytes
#3rd param：block name
#4th param: byte size
#Header is a temp tag, becasue xml.etree require the XML-based string can only
#have one parentNode. Header will be removed later 
data_block_template = "<Header>\r\n\
      <DATABLOCK>\r\n\
          <DATABLOCK-NAME>{0}__Org</DATABLOCK-NAME>\r\n\
          <DATAFORMAT>hexadecimal</DATAFORMAT>\r\n\
          <DATABLOCK-CLASS>eeprom_data_original</DATABLOCK-CLASS>\r\n\
          {1}\r\n\
      </DATABLOCK>\r\n\
      <DATABLOCK>\r\n\
          <DATABLOCK-NAME>{0}__Desc</DATABLOCK-NAME>\r\n\
          <DATAFORMAT>text</DATAFORMAT>\r\n\
          <DATABLOCK-CLASS>eeprom_data_description</DATABLOCK-CLASS>\r\n\
          {1}\r\n\
     </DATABLOCK>\r\n\
     <DATABLOCK>\r\n\
          <DATABLOCK-NAME>{0}</DATABLOCK-NAME>\r\n\
          <UNCOMPRESSED-SIZE>{2}</UNCOMPRESSED-SIZE>\r\n\
          <DATAFORMAT>base64</DATAFORMAT>\r\n\
          <DATABLOCK-CLASS>eeprom_data</DATABLOCK-CLASS>\r\n\
          <DATA></DATA>\r\n\
    </DATABLOCK>\r\n\
    </Header>\r\n"

#1 block name
#2 id
#3 blcok name
#4 ee_datablock/ee_range/ee_erase
# all values except the first actully can be ignored, only making them empty is also ok, the value will be modified by EEEDIT after saving it
data_pointer_template = "<DATAPOINTER>\r\n\
            <DATAPOINTER-NAME>{0}</DATAPOINTER-NAME>\r\n\
            <DATAPOINTER-IDENT>{1}</DATAPOINTER-IDENT>\r\n\
            <DATABLOCK-NAME>{2}</DATABLOCK-NAME>\r\n\
            <LENGTH></LENGTH>\r\n\
            <DATAFORMAT-IDENTIFIER>{3}</DATAFORMAT-IDENTIFIER>\r\n\
            </DATAPOINTER>\r\n"

session_FAILURE_MEMORY_template = "<SESSION>\r\n\
        <COMMENT>representation of failure memory blocks</COMMENT>\r\n\
        <SESSION-NAME>__FAILURE_MEMORY__</SESSION-NAME>\r\n\
        <IMPLIED></IMPLIED>\r\n\
        </SESSION>\r\n"

session_REPROG_template = "<SESSION>\r\n\
        <COMMENT>Reprog</COMMENT>\r\n\
        <SESSION-NAME>ECUReprogramming</SESSION-NAME>\r\n\
        <IMPLIED></IMPLIED>\r\n\
        <DATAPOINTERS>\r\n\
        </DATAPOINTERS>\r\n\
        </SESSION>\r\n"


#this string will be added at the back of 'data_block_template'
#the size of one data is not known when the data template is defined
#there would be one or more added depending on the byte size
data_template = "<DATA>{0}</DATA>"

#{0} - BB number
#{1} - SW / HW
#{2} - INDEX (CNT VERSION)
#{3} - ECU GENERATION
#{4} - SW Type
ProjectInfo_template = '<DATA>Generator=EEEdit</DATA>\r\n\
      <DATA>SWIdent={0}</DATA>\r\n\
      <DATA>ECUIdent=</DATA>\r\n\
      <DATA>ContainerType={1}</DATA>\r\n\
      <DATA>ContainerIndex={2}</DATA>\r\n\
      <DATA>EEPROMSize=0xFFFFFFFF</DATA>\r\n\
      <DATA>Validation=valid</DATA>\r\n\
      <DATA>ExceptionalRelease=0</DATA>\r\n\
      <DATA>VariantHandling=0</DATA>\r\n\
      <DATA>EcuGeneration={3}</DATA>\r\n\
      <DATA>SwType=ESP</DATA>\r\n\
      <DATA>Premium={4}</DATA>\r\n\
      <DATA>Sample={5}</DATA>\r\n\
      <DATA>PDMSize=</DATA>\r\n'

# 0 ABSR/ESP System 9
# 1 1267980336
# 2 1267S80336
# 3 P or S
# 4 00 / 01 ... (CNT VERSION)
ProjectResponsible_template = '<DATE>4/24/2020 4:05:15 PM</DATE>\r\n\
    <PROJECT>\r\n\
      <PROJECT-INFO>\r\n\
        <COMMENT></COMMENT>\r\n\
        <PROJ-DOMAIN>Bosch</PROJ-DOMAIN>\r\n\
        <ECU-FAMILY-DESC>{0}</ECU-FAMILY-DESC>\r\n\
        <PROJECT-DESC>B-No=, BB-No={1]</PROJECT-DESC>\r\n\
        <ECU-IDENT>{1}</ECU-IDENT>\r\n\
        <SW-IDENT>{2}_{3}_SC_{4}</SW-IDENT>\r\n\
        <SW-REVISION></SW-REVISION>\r\n\
        <RESPONSIBLES>\r\n\
          <RESPONSIBLE>\r\n\
            <COMPANY>{5}</COMPANY>\r\n\
            <DEPARTMENT>{6}</DEPARTMENT>\r\n\
            <ROLE>project_responsible</ROLE>\r\n\
            <PERSON-NAME>{7}</PERSON-NAME>\r\n\
            <PHONE>{8}</PHONE>\r\n\
            <EMAIL>{9}</EMAIL>\r\n\
          </RESPONSIBLE>\r\n\
        </RESPONSIBLES>\r\n\
      </PROJECT-INFO>\r\n\
    </PROJECT>\r\n'


'''---------------------------------
   ---------ERROR DATA CHECK--------
   ---------------------------------'''

CHECK_DATA_LEN_WRONG = "Wrong lenth on one byte or more"   # every byte contains two Hex character
CHECK_DATA_SIZE_WRONG = "Wrong size for this item"  # size of data should be equal to its defined size in CNT
CHECK_DATA_CHAR_WRONG = "Unrecognized character"  # every char of one byte must be in [0-9] or [A-F]
CHECK_DATA_USECASE_WRONG = "Unrecognized Use Case"
CHECK_DATA_CORRECT = "Correct"
CHECK_DATA_PATTERN = "[0-9A-F]{1,2}$"



'''---------------------------------
   ---------File Path--------
   ---------------------------------'''
   #used to generate a new cnt and rename it, use powershell to call eeedit.exe to autoprocess generated cnt
XML_PARSE_FILE = 'EEPROM_Container.cnt'
EEEDIT_PATH = 'C:\TSDCT\EEEdit\eeedit.exe'
NEW_CNTFILE_NAME = 'Rename.CNT'
OLD_CNTFILE_NAME = '.CNT'
POWERSHELL_COMMAND_CNT_AUTOPROCESS = r'powershell {0} {1} AUTOPROCESS'.format(EEEDIT_PATH,XML_PARSE_FILE)
