# 2019-2020 Fundamentos de Programação
# Grupo 33
# 35354 Maria Joao Martins
# 27745 Miguel Casanova

import constants

def convertNumber(n): 
    """ Converts an int < 10 (formatted n), to a str in the nn format.
    Requires: n is an int >= 0
    Ensures: a str in the format "0n" if n < 10, or "n" otherwise.
    """
    
    if n < 10:
        return "0" + str(n)
    else:
        return str(n)

def headerTimeUpdt (header):
    """
    Adds 30 minutes to the header of a file, considering the working hours of 8:00 to 20:00.
    Requires: A tuple with information read from a header, following the specifications
    of the project.
    Ensures: Updated header to be used for generating updated Drone files.
    """
   
    day = (int(header[0].split("-")[0]))
    month = (int(header[0].split("-")[1]))
    year = (int(header[0].split("-")[2]))
    hours = (int(header[1].split("h")[0]))
    minutes = (int(header[1].split("h")[1]))

    updtDay = day
    updtMonth = month
    updtYear = year
    updtHours = hours
    updtMinutes = minutes + constants.TIMEINCREMENT ## adds 30 minutes to header file name

    ## confirms closing hour is respected; If not updated information is available for next day
    ## if next day, corrects for month/year if needed
    if updtMinutes >= constants.MINUTEHOURS:
        updtHours = updtHours+1
        updtMinutes = updtMinutes-constants.MINUTEHOURS
    
    if updtHours >= constants.HOURSINDAY or updtHours > constants.CLOSINGTIME:
        updtHours = constants.OPENINGTIME
        updtMinutes = 0
        updtDay += 1

    if updtDay > constants.DAYSMONTH:
        updtDay = updtDay-constants.DAYSMONTH
        updtMonth += 1

    if updtMonth > constants.MONTHSYEAR:
        updtMonth = 1
        updtYear += 1

    return (str(updtDay)+"-"+str(convertNumber(updtMonth))+"-"+str(updtYear), str(convertNumber(updtHours))+"h"+str(convertNumber(updtMinutes)), header[2], header[3])        

def calculateNewTime (delivTimeAndIncrement):
    """
    Calculates the date and time for both delivery start and delivery completion (with time
    of return of drone) of a parcel by a selected drone.
    Requires: A tuple with three strings, corresponding to date of delivery request, time of
    delivery request and time for delivery, respectively.    
    Ensures: A tuple with 4 strings, corresponding to the updated information (followin the project
    guidelines) of delivery start date, delivery start time, delivery completion date and delivery
    completion time.
    """
    
    if int(delivTimeAndIncrement[2]) > 720: ## in case the delivery time is larger than a working day, delivery can't be made.
        return ("Cancel")

    else:
        delivDay = (int(delivTimeAndIncrement[0].split("-")[2]))
        delivMonth = (int(delivTimeAndIncrement[0].split("-")[1]))
        delivYear = (int(delivTimeAndIncrement[0].split("-")[0]))
        delivHours = (int(delivTimeAndIncrement[1].split(":")[0]))
        increment = (int(delivTimeAndIncrement[2]))
        minutes = (int(delivTimeAndIncrement[1].split(":")[1]))
        delivMinutes = (int(delivTimeAndIncrement[1].split(":")[1])) + increment
        delivRequestHours = (int(delivTimeAndIncrement[1].split(":")[0]))
        delivRequestMinutes = (int(delivTimeAndIncrement[1].split(":")[1]))

        ## confirms closing hour is respected; If not updated information is available for next day
        ## if next day, corrects for month/year if needed 
        if delivMinutes >= constants.MINUTEHOURS:
            delivHours = delivHours + delivMinutes // constants.MINUTEHOURS
            delivMinutes = delivMinutes % constants.MINUTEHOURS

        if (delivHours == constants.CLOSINGTIME and delivMinutes > 0)  or delivHours > constants.CLOSINGTIME:
            delivRequestHours = constants.OPENINGTIME
            delivRequestMinutes = 0
            delivHours = constants.OPENINGTIME
            delivMinutes = increment
            
            while delivMinutes >= constants.MINUTEHOURS:
                delivHours = delivHours + delivMinutes // constants.MINUTEHOURS
                delivMinutes = delivMinutes % constants.MINUTEHOURS
            delivDay += 1
            
        if delivDay > constants.DAYSMONTH:
            delivDay = delivDay - constants.DAYSMONTH
            delivMonth += 1

        if delivMonth > constants.MONTHSYEAR:
            delivMonth = delivMonth - constants.MONTHSYEAR
            delivYear += 1

        return (str(delivYear)+"-"+str(convertNumber(delivMonth))+"-"+str(convertNumber(delivDay)), str(convertNumber(delivRequestHours))+":"+str(convertNumber(delivRequestMinutes)), str(delivYear)+"-"+str(convertNumber(delivMonth))+"-"+str(convertNumber(delivDay)), str(convertNumber(delivHours))+":"+str(convertNumber(delivMinutes)))




