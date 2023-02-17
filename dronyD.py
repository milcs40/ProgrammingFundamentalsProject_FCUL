# 2019-2020 Fundamentos de Programação
# Grupo 33
# 35354 Maria Joao Martins
# 27745 Miguel Casanova

import sys
import readFiles
import organize
import writeFiles

def allocate(fileNameDrones, fileNameParcels):
    """
    Assign given drones to given parcels.
    Requires: fileNameDrones, fileNameParcels are str, with the names
    of the files representing the list of drones and parcels, respectively,
    following the format indicated in the project sheet.
    Ensures: Two output files, respectively, with the listing of scheduled
    transportation of parcels and the updated listing of drones, following the format
    and naming convention indicated in the project sheet.
    """

    ## Reads the files and:
    ## - Creates a list for each of the filename, containing a tuple with header information, and all drones
    ##   (for drones file) or parcels (for parcels file) as lists.
    ## - assigns the above lists to variables.
    drones = readFiles.readDronesFile(fileNameDrones)
    parcels = readFiles.readParcelsFile(fileNameParcels)

    ## Runs the assign_UpdateDrone function, that assures:
    ## - Creates a deecopy list of all drones and iterates over all parcels (following the hour of delivery request)
    ##   to match it for a compatible and best drone to perform the delivery.
    ## - Calculates the time of delivery (as the latest between drone availability and delivery request).
    ## - Updates drone according to delivery (next time available, accumulated distance, autonomy).
    ## - Next pass of the for loop, iterates over the updated drones list.
    ## - Function provides a list of lists. The first list in the list of cancelled drones (sorted as per program specs),
    ##   the second, the timetables for deliveries (sorted as per program specs), and the third list, the updated drones
    ##   list, available for the next delivery time (30 minutes after).
    listOfAllDrones = organize.assign_UpdateDrone(drones, parcels)

    ## - Creates a new drones file, with a time increase of 30 over the previous file, using previous header info.
    ## - Adds the updated drones info into the above file.
    updatedDrones = writeFiles.writeNewDronesFile(fileNameDrones)
    writeFiles.addUpdtdDrones(updatedDrones, listOfAllDrones)

    
    ## - Creates a new timetable file, with the same schedule as the input file (as per test set specification).
    ## - Adds all the delivery requests, including cancelled and deliveries client/drone and hour of delivery start.
    timetable = writeFiles.writeParcelsFile(fileNameParcels)
    writeFiles.addDeliveries(timetable, listOfAllDrones)


## Program start
inputFileName1, inputFileName2 = sys.argv[1:]

## - Check for header/filename errors (invalid filename) and whether the structure of the filename
##   and header are compatible. Does this for both input files.
## - Checks whether header information within the two input files is compatible.
## - Only if no errors are found in the files (and between them), the program tries to allocate
##   drones to parcels.
checkFile1 = readFiles.headerFilenameError(inputFileName1)
checkFile2 = readFiles.headerFilenameError(inputFileName2)
checkCompatibleFiles = False

if checkFile1 and checkFile2:
    checkCompatibleFiles = readFiles.equalInputError(inputFileName1, inputFileName2)
    
if checkCompatibleFiles:     
    allocate(inputFileName1, inputFileName2)


