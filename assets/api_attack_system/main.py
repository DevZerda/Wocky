import os, sys, time

from ..Config.main import *
from ..auth.crud import *
from ..auth.crudFunc import *

class APICrud:
    def listAPIs():
        apiDB = open("./assets/db/apis.db", "r").read()
        apis = apiDB.split("\n")

        api_List = "ID | API Name             API Domain                  API Access\r\n______________________________________________________________________________________\r\n"

        i = 0
        for api in apis:
            i += 1
            if len(api) > 5:
                if api.startswith("api_Name="):
                    apiName = api.replace("api_Name=", "")
                    apiURL = apis[i].replace("api_URL=", "")
                    apiMethods = apis[i+1].replace("api_Methods=", "")
                    apiAccess = apis[i+2].replace("api_Access=", "")
                    print(apiAccess)
                    api_List += f"{str(i-1)}  | {apiName}\t {apiURL[0:31]}\t {apiAccess}\r\n\r\n"

        return api_List

    def GetAPI(apiName):
        apiDB = open("./assets/db/apis.db", "r").read()
        apis = apiDB.split("\n")

        i = 0
        for api in apis:
            i += 1
            if len(api) > 5:
                if api.startswith(f"api_Name={apiName}"):
                    apiName = api.replace("api_Name=", "")
                    apiURL = apis[i].replace("api_URL=", "")
                    apiMethods = apis[i+1].replace("api_Methods=", "")
                    apiAccess = apis[i+2].replace("api_Access=", "")
                    return f"{apiName},{apiURL},{apiMethods},{apiAccess}"
        return "[x] Error, No API Found!"

# api_Name=WockAPI
# api_URL=https://WockSec.xyz/api/L4.php?key=fRgtw4t54hFWUj675$ge&host={ip}&port={port}&time={time}&method={method}
# api_Methods=OVH
# api_Access=false
# api_Funnels=SOCIETY-OVH:LDAP,SOCIETY-HOME:HOME-SLAP               
    
    def addAPI(apiName, api, methods):
        apiDB = open("./assets/db/users.db", "a")
        apiDB.write(f"api_Name={apiName}\napi_URL={api}\napi_Methods={methods}\n")

    def removeAPI(apiName):
        pass

    def updateAPI(apiName, new_api, methods):
        pass

# class APIFunc:
