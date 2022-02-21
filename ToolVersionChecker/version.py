# Tool Auto Version Checker and Updater By ToxicNoob
# https://github.com/Toxic-Noob/

# Required Modules
import requests
import sys
import os
import time

# PSB Flush Print
def psb(z):
    try:
        speed = int(custom.Speed)
        if (speed == "") or (speed == 0):
            speed = 0.2
    except:
        speed = 0.2
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(speed/10)

# Print Type
def printType(data):
    try:
        if (custom.printType == "psb"):
            psb(data)
        elif (custom.printType == "print"):
            print(data)
        else:
            psb(data)
    except:
            psb(data)

# Generating Tool Name
def ReName(url):
    data = url.split("/")
    name = data[4]
    return name

# Generating URL of Tool's' Version File
def vUrl(url, file):
    head = "https://raw.githubusercontent.com/"
    tail = "/main/"
    data = url.split("/")
    path = data[3]+"/"+data[4]
    rawURL = head+path+tail+file
    return rawURL

# Custom Output Data
def custom(check = "", update = "", updateSuccess = "", checkSuccess = "", printType = "", Speed = ""):
    custom.check = check
    custom.update = update
    custom.updateSuccess = updateSuccess
    custom.checkSuccess = checkSuccess
    custom.printType = printType
    if not ("." in Speed):
        Speed = ("Speed"+"0")
    if not (".0" in Speed):
        Speed = Speed.replace(".", "")
    custom.Speed = Speed

# Checking Custom Output Data and Returning to Main Function #

def customCheck():
    try:
        check = custom.check
        if (check == ""):
            check = ("\n\033[0;92m    [*] Please Wait..\n    [*] Checking Update...\033[37m")
        elif ("$blank$" in check.lower()):
            check = ""
    except:
        check = ("\n\033[0;92m    [*] Please Wait..\n    [*] Checking Update...\033[37m")
    return check


def customUpdate():
    try:
        update = custom.update
        if (update == ""):
            update = ("\n\033[92m    [*] Tool Update Found..\n    [*] Please Wait, Updating Tool...\033[37m")
        elif ("$blank$" in update.lower()):
            update = ""
    except:
        update = ("\n\033[92m    [*] Tool Update Found..\n    [*] Please Wait, Updating Tool...\033[37m")
    return update

        
def customUpdateSuccess():
    try:
        updateSuccess = custom.updateSuccess
        if (updateSuccess == ""):
           updateSuccess = ("\033[92m\n    [*] Tool Updated Successfully...\033[37m\n")
        elif ("$blank$" in updateSuccess.lower()):
            updateSuccess = ""
    except:
        updateSuccess = ("\n\033[92m    [*] Tool Updated Successfully...\033[37m\n")
    return updateSuccess


def customCheckSuccess(RepoURL):
    try:
        checkSuccess = custom.checkSuccess.replace("$Toolname$", ReName(RepoURL)).replace("$TOOL$", ReName(RepoURL))
        if (checkSuccess == ""):
            checkSuccess = ("\n\033[92m    [*] You Are Using The Latest Version Of "+ReName(RepoURL)+"....\033[37m\n")
        elif ("$blank$" in checkSuccess.lower()):
            checkSuccess = ""
    except:
        checkSuccess = ("\n\033[92m    [*] You Are Using The Latest Version Of "+ReName(RepoURL)+"....\033[37m\n")
    return checkSuccess

# Main Function#

def check(verFile = "", RepoURL = "", RepoFile = ""):
    
    # Check If All Data Are Specified
    if (verFile == "") or (RepoURL == ""):
        printType("\n\033[91m    [!] Required Data Is not Specified [!]")
        printType("\n\033[92m    [!] Must Specify \"verFile\" (Version File Path) and \"RepoURL\" (Repository URL Link)....\n\033[37m")
        time.sleep(1)
        sys.exit()
    
    # Getting Output Data #
    
    check = customCheck()
        
    update = customUpdate()
        
    updateSuccess = customUpdateSuccess()
        
    checkSuccess = customCheckSuccess(RepoURL)
    
    # Reading Version Data From Cloned Tool
    try:
        preVer = open(verFile, "r").read()
    except FileNotFoundError:
        printType("\n\033[91m    [!] Version File Not Found!!")
        printType("\033[92m    [!] Skipping Update Checking Process!\033[37m")
        time.sleep(1)
        return
    
    # Main Process #
    
    # Getting Repository / Tool Name and Version URL #
    RepoName = ReName(RepoURL)
    verURL = vUrl(RepoURL, verFile)
    
    printType(check)
    
    # Reading Version Data From Main Tool
    try:
        mainVer = requests.get(verURL).text
    except:
        time.sleep(0.7)
        printType("\n\033[91m    [!] Internet Connection Error!")
        printType("\033[92m    [!] Skipping Update Checking Process!!\033[37m")
        time.sleep(1)
        return
    
    # Update Tool, If Update Found
    if not (preVer == mainVer):
        printType(update)
        try:
            os.system("cd .. && rm -rf "+RepoName+" && git clone "+RepoURL+" > /dev/null 2>&1")
            printType(updateSuccess)
        except:
            time.sleep(0.6)
            printType("\n\033[91m    [!] An Error Occurred..")
            printType("\033[92m    [!] Skipping Update....\033[37m")
            time.sleep(1)
            return
        
        if not (RepoFile == ""):
            os.system("cd .. && cd "+RepoName+" && python "+RepoFile)
        else:
            sys.exit()
    else:
        printType(checkSuccess)
        time.sleep(1)
