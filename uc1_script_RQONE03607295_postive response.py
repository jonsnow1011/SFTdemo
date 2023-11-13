from doipclient import *
from doip import *
import time
import sys
import traceback
import datetime

################# BOSCH80124_72_1_2_0.py      --- file for reference

def test(dc,it):
    dc.connect()	
    
#### TC-01####
    dc.addToTrace(True,'#############      TC_1  ################',flashcedereEnv=False)

    dc.addToTrace(True,'############################################',flashcedereEnv=False)
    
    dc.send('10 03')
    dc.receive('50 03>')


    
    dc.send('31 01 03 66 00 00 00')
    dc.receive('71 01 03 66>') 

    dc.send('31 01 03 E7 00 00 00')
    dc.receive('71 01 03 E7>')

    dc.send('31 01 09 12')
    dc.receive('71 01 09 12>')
 
 

 

#### TC-03####
    dc.addToTrace(True,'#############      TC_3  ################',flashcedereEnv=False)

    dc.addToTrace(True,'############################################',flashcedereEnv=False)
    
    dc.send('10 03')
    dc.receive('50 03>')


    
    dc.send('31 01 03 66 00 00 00')
    dc.receive('71 01 03 66>'




#### TC-04####
    dc.addToTrace(True,'#############      TC_4  ################',flashcedereEnv=False)

    dc.addToTrace(True,'############################################',flashcedereEnv=False)
    
    dc.send('31 01 03 E7 00 00 00')
    dc.receive('71 01 03 E7>')



 
 #### TC-05####
    dc.addToTrace(True,'#############      TC_5  ################',flashcedereEnv=False)

    dc.addToTrace(True,'############################################',flashcedereEnv=False)
    
    dc.send('10 03')
    dc.receive('50 03>')

    dc.send('31 01 09 12')
    dc.receive('71 01 09 12>')





 
  


    

    
if __name__ == '__main__':
    debug.set_verbosity('DEBUG')
    logFilePath=r'D:\JPAN1KOR\Test report\uc1_script_RQONE03133580.html'
    #dc = DoipClient("192.168.111.20", doip.DOIP_TCP_PORT,0x0767,logFilePath=r'c:\temp\doip_test\01\test_report.html',flashcedereEnv=False,routeActivationType=0x02,routeActRsvMfData=0x00,logWriteImmediate=False)
    dc = DoipClient("fd53:7cb8:383:2:0:0:0:10F", doip.DOIP_TCP_PORT,0x0E80,logFilePath=r'D:\JPAN1KOR\Test report\uc1_script_RQONE03133580.html',flashcedereEnv=False,routeActivationType=0x00,logWriteImmediate=False)
    for i in range(0,1):
        if i>0:
            time.sleep(25)
        dc.setP2(0.05)
        dc.setP3Max(5.0)
        dc.setP2Star(5.0)
        dc.__p2_P3_Delta=0.5
        try:
            test(dc,i)
            dc.close()
        except Exception as error:
            s=str(traceback.format_exc())
            print s
            dc.addErrorToLog(s)
            try:
                dc.close()
            except:
                pass
        
    dc.generateReport()
    print 'Test done !'
    print 'Please check testreport c:\temp\doip_test\01\Test_report_1.html'
    os.startfile(logFilePath)
    sys.exit(0)
