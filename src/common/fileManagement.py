# File Management & Manipulation Functions
import os.path
from datetime import datetime
import json
# Global VARS
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# env_path = '../../../env'
# env_path = 'env'

def sayHello():
    print('hello')

def removeCurrent(completeName):
    # used in outputToFile()
    if os.path.exists(completeName):
        os.remove(completeName)
        return 'File: Overwritten'
    else:
        return "File: Created"
    
def JSONExport(fileName,save_path,mylist): 
    completeName = os.path.join(save_path, fileName) 
    print(completeName) 
    overwriteStatus = removeCurrent(completeName)
    with open(completeName, 'w') as f:
        json.dump(mylist, f)
    print('Records Exported:',len(mylist),'records' )
    print(current_time, 'Exported file:',completeName,overwriteStatus,)

def JSONImport(fileName,save_path): 
    completeName = os.path.join(save_path, fileName) 
    print(current_time,'Imported file:',completeName) 
    with open(completeName) as f:
        result = json.load(f)
    return result 
def JSONImportEnv(envVar,env_path): 
    fileName = 'env.json'
    completeName = os.path.join(env_path, fileName) 
    print(current_time,'Imported Env:',completeName) 
    with open(completeName) as f:
        result = json.load(f)
    return result[0][envVar] 

