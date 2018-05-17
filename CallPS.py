import subprocess

def main():
    #Gets Powershell Command and Filepath to nps from User
    psCommand = input("Enter Command: ")
    filepath = input("Enter filepath for nps.exe: ")
    rawFlag = False
    while(True):
        needRaw = input("Does filename have spaces (Yes or No): ")
        if(needRaw == ('Yes' or 'YES' or 'yes')):
            rawFlag = True
            break
        elif(needRaw == ('No' or 'no' or 'NO')):
            break
        else:
            continue
    truepath = stringtoRawString(filepath)[:-1]
    try:
        if(rawFlag):
            subprocess.call([truepath, psCommand])
        else:
            subprocess.call([filepath, psCommand])
    except:
        pass

def stringtoRawString(string):
    #method to convert string to raw string if needed for filepath
    rawString = ""
    for char in string.split('\\'):
        rawString = rawString+("%r"%char).strip("'")+"\\"
    return rawString

if __name__ == "__main__":
    main()
