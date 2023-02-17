# 2019-2020 Fundamentos de Programação
# Grupo 33
# 35354 Maria Joao Martins
# 27745 Miguel Casanova

import timeManager
import readFiles

def writeNewDronesFile (inputFileName1):
    """
    This will use the information in a header to open a new file in write mode,
    writing the header in the file and the matching filename (with a 30 minutes increase).
    This will be the updated drones file.
    Requires: A tuple output from a readHeader function, with:
    ("date", "time", "company", "scope")
    Ensures: The creation of a file with the appropriate header and filename,
    as described in the project.
    """
    
    header = readFiles.readHeader(inputFileName1) ## reads header information from input file
    updtHeader = timeManager.headerTimeUpdt(header) ## updates the header information, adding 30 minutes
    
    time = updtHeader[1]
    company = updtHeader[2]
    scope = updtHeader[3]
    day = updtHeader[0]

    ## creates a file with a name matching the information on the updated header
    filename = scope.lower()+time+"_"+day.split("-")[2]+"y"+day.split("-")[1]+"m"+day.split("-")[0]+".txt"
    file = open(filename, "w")
    file.writelines(["Time: \n", time, "\n", "Day: \n", day, "\n", "Company: \n", company,
                     "\n", scope,":", "\n"]) ## writes into the new file, the updated header information
    
    file.close()
    return filename

def addUpdtdDrones (filename, listAllUpdts):
    """
    Adds updated drone information to a drones file.
    Requires: filename is str, the name of a .txt file for storing drone information.
    A list of drones with information following the format specified in the project.
    Ensures: A drone .txt file with the drone infomation.
    """

    file = open(filename, "a")
    drones = "\n".join(", ".join(map(str,element)) for element in listAllUpdts[2]) ## adds the updated drone information into the new drone file
    
    file.write(drones)
    file.close()
            
def writeParcelsFile (inputFileName2):
    """
    This will use the information in a header to open a new file in write mode,
    writing the header in the file and the matching filename (with a 30 minutes increase).
    This will be the new timetable file for deliveries.
    Requires: A tuple output from a readHeader function, with:
    ("date", "time", "company", "scope")
    Ensures: The creation of a file with the appropriate header and filename,
    as described in the project.
    """

    header = readFiles.readHeader(inputFileName2) ## reads header information from input file
    
    time=header[1]
    company=header[2]
    day=header[0]

    ## creates a file with a name matching the information on the header
    filename = "timetable"+time+"_"+day.split("-")[2]+"y"+day.split("-")[1]+"m"+day.split("-")[0]+".txt" 
    file = open(filename, "w")
    file.writelines(["Time: \n", time, "\n", "Day: \n", day, "\n", "Company: \n", company,
                     "\n", "Timeline:", "\n"]) ## writes into the new file, the header information

    file.close()
    return filename

def addDeliveries (filename, listAllUpdts):
    """
    Adds relevant delivery information to a Timetable file.
    Requires: filename is str, the name of a .txt file for storing deliveries information.
    A list of deliveries with respective information, following the format specified
    in the project.
    Ensures: A timetable .txt file, with the relevant information for deliveries.
    """
    
    file = open(filename, "a")
    canceled = "\n".join(", ".join(map(str,element)) for element in listAllUpdts[0]) ## adds cancelled parcel information
    assigned = "\n".join(", ".join(map(str,element)) for element in listAllUpdts[1]) ## adds deliveries into file


    file.write(canceled)
    file.write("\n")
    file.write (assigned)
    file.close()

