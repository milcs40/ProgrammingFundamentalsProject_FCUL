# 2019-2020 Fundamentos de Programação
# Grupo 33
# 35354 Maria Joao Martins
# 27745 Miguel Casanova

import copy
from operator import itemgetter
import timeManager

def sortToBestDrone(listPotencialDrones):
    """
    Sorts a list of potencial drones for a client, by time available, autonomy,
    less accumulated distance, name of client.
    Requires: input list of lists following the structure provided in the project.
    Ensures: returns a list sorted as determined in the project.
    """
    
    listPotencialDrones = listPotencialDrones
    potDronesSortList = sorted(listPotencialDrones, key = itemgetter(4, 0)) ## sort by less accumulated KM and then by name
    potDronesSortList = sorted(potDronesSortList, key = itemgetter(5), reverse=True) ## sort by more battery left
    potDronesSortList = sorted(potDronesSortList, key = itemgetter(6, 7)) ## sort by date and hour
    return potDronesSortList

def removeSpace(stringTostrip):
    """
    Removes spaces in selected list elements.
    Requires: An element of a list, as a string.
    Ensures: Specified list element as a string, with no spaces.
    """
    
    stringStriped = stringTostrip.strip(' ')
    return [stringStriped]

def nAcumuDist(droneDist, parcelDelivDist):
    """
    Calculates new acumulated distance (KM) in drone after parcel delivery.
    Requires: Two inputs, a first float corresponding to the total distance the drone
    has travelled so far (KM), the second, an integer correspoding to the distance
    for the delivery (meters).
    Ensures: Specified distances as list without spaces, rounded to one decimal place.
    """
    
    dist = droneDist + parcelDelivDist*0.002
    return round(dist, 1)

def nBateryLeft(droneBatery, parcelDelivDist):
    """
    Calculates batery left (KM) in drone after parcel delivery.
    Requires: Two inputs, a first float corresponding to the autonomy left in the drone (KM),
    the second, an integer correspoding to the distance for the delivery (meters).
    Ensures: Specified distances as list without spaces.
    """
    
    dist = droneBatery - parcelDelivDist*0.002
    return round(dist,1)

def updateListDroneAssigned(listDroneToUpdate, droneUpdatedTemp):
    """
    Update working list of drones available after each parcel delivery. 
    Requires: Two inputs: one list of drones before delivery, list of one element,
    the drone with updated information considering the delivery it was assigned to do.
    Ensures: First list is updated for the drone that was attributed a delivery.
    """
    
    for drone in listDroneToUpdate:
        if drone[0] == droneUpdatedTemp[0][0]: ## finds drone that was just assigned a delivery
            listDroneToUpdate.remove(drone) ## removes initial data for drone
            listDroneToUpdate.append(droneUpdatedTemp[0]) ## adds drone with updated data
    return listDroneToUpdate

def assign_UpdateDrone(drone, parcel):
    """
    Iterates over all parcels (following the hour of delivery request), identifying compatible drones.
    Sorts the drones to identify the most suited to perform the delivery.
    Calculates the time of delivery (as the latest between drone availability and delivery request).
    Updates drone according to delivery (next time available, accumulated distance, autonomy),
    so next pass of the for loop, iterates over the updated drones list.
    Requires: One list of drones and one list of parcels, in which the first element is a tuple with
    header information and the following elements, drones or parcels, respectively.
    Ensures: List of lists. The first list is the list of cancelled drones (sorted as per program specs),
    the second, the timetables for deliveries (sorted as per program specs), and the third list,
    the updated drones list, available for the next delivery time (30 minutes after).
    """
    
    ## copy of drone list so it gets updated after assignment, removes first element (tuple containing the header information)
    listDroneToUpdate = copy.deepcopy(drone[1:])
    
    ## start allocating parcels to drone
    listDroneAssign = [] ## working list for each parcel
    dCancel = [] ## list for each cancelled 

    ## check potential drone per customer in the same zone, check if drone can carry parcel weight, check distance for delivery respects range
    ## for drone flight and enough automony for delivery&back
    for line in parcel[1:]:
        dtmp = []  # working list for potential drones per parcel, temporary   
        listDroneUpdatedTemp = [] # working list for each drone updated time after flight, temporary

        nameClien = line[0]
        zoneClien = line[1]
        dateDelivClien = removeSpace(line[2])
        hourDelivClien = removeSpace(line[3])
        distDeliv = int(line[4])
        kgDeliv = int(line[5])
        time4Deliv = removeSpace(line[6])

        for ln in listDroneToUpdate:
            if zoneClien == ln[1] and kgDeliv <= int(ln[2]) and distDeliv <= int(ln[3]) and distDeliv*2 <= round(float(ln[5]), 1)*1000:
                dtmp.append(ln)
                   
    ## drone not available in area or none meets previous criteria, add customer as cancelled                            
        if len(dtmp) == 0: 
            dCancel.append(dateDelivClien+hourDelivClien+[nameClien,'cancelled'])
            
    ## drone(s) potentially available, sorts with SortToBestDrone from organize
    ## sorts list of drone available when tie between +2 best drones, following specific conditions
        else:
            dtempSort = sortToBestDrone(dtmp) ## sorts to best drone of available drone
            bestDrone = dtempSort[0] ## selects top choice

            nameDrone = bestDrone[0]
            zoneDrone = bestDrone[1]
            kgDrone = bestDrone[2]
            rangeDrone = bestDrone[3]
            acumuDistDrone = round(float(bestDrone[4]),1)
            batteryDrone = round(float(bestDrone[5]),1)
            dateLastLand = removeSpace(bestDrone[6])
            hourLastLand = removeSpace(bestDrone[7])

            ## date and Hour of parcel delivery and date and hour of drone availability are compared
            ## after sorting, the latest time is chosen for delivery
            ## date, time and time for delivery are used to calculate the new time of availabilty for the drone
            dateTimeCompare = (dateDelivClien, hourDelivClien), (dateLastLand, hourLastLand)
            deliveryStartTime = sorted(dateTimeCompare, key=itemgetter(1))[1]
            deliveryIncrementTime = deliveryStartTime[0] + deliveryStartTime[1] + time4Deliv
            updtTime = timeManager.calculateNewTime(deliveryIncrementTime)
            if updtTime == "Cancel": ## in the instances the delivery can't be completed in a full working day.
                dCancel.append(dateDelivClien+hourDelivClien+[nameClien,'cancelled'])
            else:            
                listDroneAssign.append([updtTime[0], updtTime[1], nameClien, nameDrone,]) ## adds info to temporaty list assignements
                listDroneUpdatedTemp.append(bestDrone[0:4] + [str(nAcumuDist(acumuDistDrone, distDeliv)), \
                                                  str(nBateryLeft(batteryDrone, distDeliv)),\
                                                  updtTime[2], updtTime[3]]) ## adds updated drone information to a temporary list
        
    ## assigned drone is updated in the listDroneToUpdate so the selection of the best drone
    ## for the next parcel, takes into consideration the previous drone assignment (and its updated status)
                updateListDroneAssigned(listDroneToUpdate, listDroneUpdatedTemp)

    ## sort final lists according to the rules of the project
    dCancel = sorted(dCancel,key=itemgetter(2))
    listDroneAssign = sorted(listDroneAssign, key=itemgetter(0,1,2))
    listDroneToUpdate = sortToBestDrone(listDroneToUpdate)

    return dCancel, listDroneAssign, listDroneToUpdate
