'''
@File:      ProgramStart.py
@Time:      5/21/2020
@Author:    Zhou Wei
@Version:   1.0
@Contact:   Wei.ZHOU10@cn.bosch.com
'''

from CntReview import *
from CntWriter import *
from XMLReader import *
from Error import *
from Logger import *


#*****Program Starts*****

print("---Select what you want to do, input 1 or 2--- \r\n")
print("1. Read items from CNT \r\n")
print("2. Write values into CNT \r\n")
Logger.init()
func_id = input("")
if not str(func_id).isdigit():
    func_id = -1
else:
    func_id = int(func_id)

# Read value in CNT file to prepare EXCEL file
if func_id == 1:
    Logger.recordLog('\r\n****************** CNT Items Reading Tool Start **************')
    #excel_name = input("Input the path where PDM Review EXCEL is located: \r\n")
    excel_name = r'N:\Cross\Active_Safety\Internal\006_Cross_Functional\08_CSW_Function_Team\Template&Tools\02_Tools\CNTReviewTool\PDM_Collection_and_Review.xlsm'
    if not os.path.isfile(excel_name):
        Logger.recordLog('\r\n****************** PDM Review EXCEL does not exist **************', True)
        exit(0)
    try:
        xmlReader = XmlReader(XML_PARSE_FILE)
        xmlReader.read()
        xmlReader.sort(DataBlock_Dict)
        cntReview = CntReview(excel_name,'Project Specific Checklist')
        cntReview.loadDataFromCnt(DataBlock_Dict, xmlReader.max_element_number)
        cntReview.setSWVersion(xmlReader.getEPK())
        Logger.recordLog("---parse finished---",True)
        
    except FileNotFoundError:
        Logger.recordLog("!!! please make sure the file 'EEPROM_Container.cnt' is already in the current directory and the name must be correct and the path of PDM Collection file provided is correct  !!!\n", True)
        

# Write value in EXCEL file to prepare CNT file    
elif func_id == 2:
    Logger.recordLog('\r\n****************** CNT Writing Tool Start **************')
    excel_name = input("Input the path where PDM Review EXCEL is located: \r\n")
    if not os.path.isfile(excel_name):
        Logger.recordLog('\r\n****************** PDM Review EXCEL does not exist **************', True)
        exit(0)
    if not os.path.isfile(XML_PARSE_FILE):
        Logger.recordLog('\r\n****************** EEPROM_Container.cnt does not exist **************', True)
        exit(0)
    cntWriter = CntWriter(excel_name,XML_PARSE_FILE,'Project Specific Checklist')
    
    read_result = cntWriter.read()
    if not read_result:
        Logger.recordLog(Error.getErrors(), True)
        exit(0)
    result = cntWriter.write()

    if not result:
        print("---------CNT Writing Failed------")
        print(Error.getErrors())
    else:
        print("---------CNT Writing Succeeded------")
        if os.path.isfile(EEEDIT_PATH) and os.path.isfile(XML_PARSE_FILE):
            if os.system(POWERSHELL_COMMAND_CNT_AUTOPROCESS) == 0:
                #procedure won't be blocked. funtion "os.system()" can block the procedure, but when powershell starts
                #running, 'system' function WILL return because powershell has been started, and powershell will take time to finish
                time.sleep(7)
                new_file_name = input("Rename your cnt file:") + ".CNT"
                try:
                    os.rename(OLD_CNTFILE_NAME,new_file_name)
                    os.remove(XML_PARSE_FILE)
                except FileNotFoundError:
                    print("****Rename failed***")
                    Logger.recordLog('****Rename failed, no \'.CNT\' file found in current path****')
            else:
                print("CNT Autoprocess failed")
                Logger.recordLog('****CNT Autoprocess failed****')
        else:
            print("---EEEdit.exe or CNT Not Found---")
            Logger.recordLog('--- EEEdit.exe or CNT Not Found, The default path of EEEDIT is C:\TSDCT\EEEdit\eeedit.exe ---')
else:
    Logger.recordLog('\r\n****************** Input a wrong number, only 1 and 2 is valid **************')
    
input("Press 'Enter' key to exit")

