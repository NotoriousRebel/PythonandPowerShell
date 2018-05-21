import subprocess
import base64

def main():
    #Gets Powershell Command and Filepath to nps from User
    Command = input("Enter Command: ")
    psPath = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" #path to powershell.exe
    encodeFlag = getNeedEncode()
    DeterminePSorNPS()
    if (psFlag):
        runPSCommand(encodeFlag, psPath, Command)
    else:
        filePath = input("Enter file path for nps.exe : ")
        rawFlag = getNeedRaw()
        truePath = stringtoRawString(filePath)[:-1]
        runNPSCommand(encodeFlag, rawFlag, truePath, filePath, Command)

def runNPSCommand(encodeFlag,rawFlag,truePath,filePath,Command):
    #method to run NPS command
    try:
        #tries to run NPS command
        if(encodeFlag):
            byteCommand = Command.encode('utf-16be')
            if(rawFlag):
                subprocess.call([truePath, " -encodedcommand ", encodeCommand(byteCommand)])
            else:
                subprocess.call([filePath," -encodedcommand ", encodeCommand(byteCommand)])
        else:
            if (rawFlag):
                subprocess.call([truePath, Command])
            else:
                subprocess.call([filePath, Command])
    except:
        print("Could not run command successfully")

def runPSCommand(encodeFlag,psPath,Command):
    #method to run PS command
    try:
        #tries to run PS command
        if(encodeFlag):
          byteCommand = Command.encode('utf-16be')
          subprocess.call([psPath," -encodedcommand ", encodeCommand(byteCommand)])
        else:
          subprocess.call([psPath, Command])
    except:
        print("Could not run command successfully")

def DeterminePSorNPS():
    #method to determine if user wants NPS or PS
    global psFlag, npsFlag
    psFlag = False
    npsFlag = False
    PSorNPS= input("Would you like to use NPS or PS: ")
    while (True):
        if (PSorNPS == 'PS' or PSorNPS == 'NPS'):
            break
        else:
            PSorNPS = input("Does filepath contain spaces (Yes or No): ")
    if (PSorNPS == 'NPS'):
        npsFlag = True
    else:
        psFlag = True


def getNeedEncode():
    #gets User Input to know if they would like to encode their command
    encodeFlag = False
    needEncode = input("Would you like to encode command (Yes or No): ")
    correctReponses = ['Yes','No','no','NO','YES','yes']
    while (True):
        if (needEncode in correctReponses):
            break
        else:
            needEncode = input("Would you like to encode command (Yes or No): ")

    if (needEncode == 'Yes' or needEncode == 'YES' or needEncode == 'yes'):
        encodeFlag = True
    return encodeFlag

def getNeedRaw():
    #gets User Input to know if file path has spaces
    rawFlag = False
    needRaw = input("Does filename have spaces (Yes or No): ")
    correctReponses = ['Yes', 'No', 'no', 'NO', 'YES', 'yes']
    while (True):
        if (needRaw in correctReponses):
            break
        else:
            needRaw = input("Does filepath contain spaces (Yes or No): ")
    if (needRaw == 'Yes' or needRaw == 'YES' or needRaw == 'yes'):
        rawFlag = True
    return rawFlag


def encodeCommand(commandBytes):
    #method to encode command
    command = ''
    for byte in commandBytes: #iterate through bytes and encode them
        command += base64.b64encode(byte.encode('utf-8'))
    return command

def stringtoRawString(string):
    #method to convert string to raw string if needed for filepath
    rawString = ""
    for char in string.split('\\'):
        rawString = rawString+("%r"%char).strip("'")+"\\"
    return rawString

if __name__ == "__main__":
    main()
