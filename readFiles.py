# 2019-2020 Fundamentos de Programação
# Grupo 33
# 35354 Maria Joao Martins
# 27745 Miguel Casanova

import os

def readHeader(fileName):
    """
    Converts a given file listing drones or parcels and returns day, time,
    company and scope as variables.
    Requires : fileName is str, the name of a .txt file listing drones or parcels,
    following the format specified in the project.
    Ensures: tuple with day, time, company and scope as str.
    """
    
    fileIn = open(fileName, 'r')

    ## reads first 7 lines in file, storing line as variable at every-other line
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    scope = fileIn.readline().strip().replace(":", "")

    fileIn.close()
    
    return (day, time, company, scope)

def headerFilenameError(fileName):
    """
    Confirms that the file corresponding to the fileName provided exists and that the input fileName and header have same information.
    Provides relevant Input error messages.
    Requires: fileName is str, the name of a .txt file listing drones or parcels,
    following the format specified in the project.
    Ensures: returns error if headers are not equivalent with explanatory message; if file name inconsistent with format will indicate so
    if file not present in folder will indicate so
    """

    proceed = True
    file = ""
    
    ## checks whether the file corresponding to the provided filename, exists
    try:
        fileIn = open(fileName, 'r')
        fileIn.close()
    except FileNotFoundError:
        print ("Input Error: file", os.path.basename(fileName), "not found.")
        proceed = False

    nameOfFile = os.path.basename(fileName) # removes the file path.
    
    ## if file is present, checks whether the fileName starts with drones or parcels   
    if proceed == True:
        if nameOfFile.find("drones") == 0:
            file = nameOfFile.replace("drones", "") 
            scope = "Drones"
        elif nameOfFile.find("parcels")== 0:
            file = nameOfFile.replace("parcels", "")
            scope = "Parcels"
        else:
            print ("Input error: the file", os.path.basename(fileName), "is not a valid input file.")
            proceed = False

    ## if all previous error checks passed, confirms if header information matches fileName
    if proceed == True and file != '':
        ## reformates information from fileName to day-month-year
        file = file.replace("y", "-").replace("m", "-").replace(".txt", "").split("_")
        time = file[0]
        y,m,d = file[1].split("-")
        date = (d+"-"+m+"-"+y)

        ## retrives header information using function readHeader
        ## compares year, time and scope between header and file name information; if any do not match saves information as proceed = False
        head = (readHeader(fileName))
        file = (date,time,scope)
        
        if file[0] != head[0] or file[1] != head[1] or file[2] != head[3]:
            print ("Input Error: name and header inconsistent in file", os.path.basename(fileName))
            proceed = False
    return (proceed)

  
def readDronesFile(fileName):
    """
    Converts a given file listing drones into a collection if header and file name information are consistent.
    Requires: fileName is str, the name of a .txt file listing drones, following the format specified in the project sheet.
    Ensures: list whose first element is a list corresponding to the
    first drone in an input file (8 substrings, correspoding to drone name,
    zone of operation name, weight able to handle in KG, distance of flight left in KM,
    date of last flight and hour that the last flight ended) and resumes up until the last drone.
    """
    
    outputListDrones = []
    outputListDrones.append(readHeader(fileName))

    fileIn = open(fileName, 'r')
    fileInLen = open(fileName, 'r')
    lenfile = len(fileInLen.readlines())

    for i in range (7):
        fileIn.readline() ## jumps over first 7 lines, that contain header information
            
    for i in range (lenfile-7):
        outputListDrones.append(fileIn.readline().rstrip().split(', ')) ## starts collecting drone information into a list

    fileIn.close()
    fileInLen.close()

    return outputListDrones
          
def readParcelsFile(fileName):
    """
    Converts a given file listing parcels into a collection if header and file name information are consistent.
    If data scope is parcels, gives error explaining so
    Requires: fileName is str, the name of a .txt file listing drones, following the format specified in the project sheet.
    Ensures: list whose first element is a list corresponding to the
    first drone in an input file (8 substrings, correspoding to drone name,
    zone of operation name, weight able to handle in KG, distance of flight left in KM,
    date of last flight and hour that the last flight ended) and resumes up until the last drone.
    """
    
    outputListParcels = []
    outputListParcels.append(readHeader(fileName))

    fileIn = open(fileName, 'r')
    fileInLen = open(fileName, 'r')
    lenfile = len(fileInLen.readlines())

    for i in range (7):
        fileIn.readline() ## jumps over first 7 lines, that contain header information
            
    for i in range (lenfile-7):
        outputListParcels.append(fileIn.readline().rstrip().split(', ')) ## starts collecting drone information into a list

    fileIn.close()
    fileInLen.close()

    return outputListParcels

def equalInputError(fileNameDrones, fileNameParcels):
    """
    Confirms input file for Drone and parcels have same date, hour and company.
    Requires: fileNames are str, the name of .txt files listing drones and parcels, 
    following the format specified in the project sheet.
    Ensures: returns error if headers are not equivalent with explanatory message. 
    """
    
    equal = True

    ## checks whether header information between parcels and drone files are compatible.
    if readHeader(fileNameDrones)[0:3] != readHeader(fileNameParcels)[0:3]:
        print ('Input error: inconsistent files' , os.path.basename(fileNameDrones), \
               'and' , os.path.basename(fileNameParcels))
        equal = False

    return (equal)
