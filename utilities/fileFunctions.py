def removeCurrent(fileName):
    # used in outputToFile()
    completeName = os.path.join(G_save_path, fileName)
    if os.path.exists(completeName):
        os.remove(completeName)
        return 'File: Overwritten'
    else:
        return "File: Created"   
def JSONExport(mylist,fileName): 
    completeName = os.path.join(G_save_path, fileName)  
    overwriteStatus = removeCurrent(completeName)
    with open(completeName, 'w') as f:
        json.dump(mylist, f)
    print('Records Exported:',len(mylist),'records' )
    print(current_time, 'Exported file:',completeName,overwriteStatus,)
def JSONImport(fileName):
    completeName = os.path.join(G_save_path, fileName) 
    print(current_time,'Imported file:',completeName) 
    with open(completeName) as f:
        result = json.load(f)
    return result 
def JSONImportTestFiles(fileName):
    completeName = os.path.join(G_test_Path, fileName) 
    print(current_time,'Imported TEST file:',completeName) 
    with open(completeName) as f:
        result = json.load(f)
    return result 
def printKey(myDict,position):
    result = list(myDict[position].keys())[0]
    print(result)