import xlrd 
from math import radians, cos, sin, asin, sqrt 
import sys

days = {'sat' : 1,'sun' : 2,'mon' : 3 ,'tue' : 4 ,'wed' : 5  ,'thu' : 6  ,'fri' : 7}
 
class Flight:       
    
    def __init__(self): 
        self.__source = '' 
        self.__destination = ''
        self.__departureTime = ''
        self.__arrivalTime = ''
        self.__flightNumber = ''
        self.__actualTimeInMinutes = 0.0
        self.__day = ''
     
    def setSource(self, source):  
        self.__source = source  
 
    def getSource(self):      
        return self.__source
    
    source = property(getSource,setSource)
 
    def setDestination(self, destination):  
        self.__destination = destination
 
    def getDestination(self):      
        return self.__destination
 
    destination = property(getDestination,setDestination)
    
    def setDepartureTime(self, departureTime):  
        self.__departureTime = departureTime 
 
    def getDepartureTime(self):      
        return self.__departureTime
 
    departureTime = property(getDepartureTime,setDepartureTime)
    
    def setArrivalTime(self, arrivalTime):  
        self.__arrivalTime = arrivalTime  
 
    def getArrivalTime(self):      
        return self.__arrivalTime
    
    arrivalTime = property(getArrivalTime,setArrivalTime)
    
    def setFlightNumber(self, flightNumber):  
        self.__flightNumber = flightNumber 
 
    def getFlightNumber(self):      
        return self.__flightNumber
 
    flightNumber = property(getFlightNumber,setFlightNumber)
    
    def setDay(self, day):
        self.__day = day
 
    def getDay(self):     
        return self.__day
   
    day = property(getDay,setDay)
    
    def setActualTime(self):
        dTime = []
        aTime = []
        dTime = self.__departureTime.split(':')
        aTime = self.__arrivalTime.split(':')
        dHours = int(dTime[0])
        aHours = int (aTime[0])
        if(((dHours >= 12 and aHours >= 12) or (dHours < 12 and aHours < 12)) and (aHours > dHours)) :
            tHours = aHours - dHours
        elif (dHours < 12 and aHours >=12):
            tHours = (aHours - dHours) 
        elif (dHours >= 12 and aHours < 12) or ((dHours >= 12 and aHours >= 12) or (dHours < 12 and aHours < 12)) :
            ans = aHours + 24
            tHours = ans - dHours
 
        dMin = int(dTime[1])
        aMin = int (aTime[1])
        if(aMin >= dMin):
            tMin = aMin - dMin
        else :
            ans = dMin - aMin
            tMin = 60 - ans
            tHours -= 1            
        self.__actualTimeInMinutes = tHours*60 + tMin
 
    def getActualTime(self):
        return self.__actualTimeInMinutes
    
    actualTimeInMinutes = property(getActualTime)
 
 
class HeuristicController :
    
    def getEstimatedTime(self,source,destination):
        c = CitiesContainer()
        for i in range (len(c.cities)):
            file = c.cities[i].name
            file = file.strip()
            source = source.strip()
            destination = destination.strip()
            if(source == file):
                lat1 = c.cities[i].latitude
                lon1 = c.cities[i].longitude
            if(destination == file):
                lat2 = c.cities[i].latitude
                lon2 = c.cities[i].longitude
        d = DistanceController()
        dis = d.distance(lat1,lat2,lon1,lon2)
        estimated = d.estimatedTime(dis)
        return estimated
 
    
class FlightContainer :
    
    def __init__(self) :
        self.__flights = []
        # Reading an excel file using Python 
        # Give the location of the file 
        loc = ("flights.xlsx")    
        # To open Workbook
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0)
 
        for i in range (1,151): 
            listOfDays = []
            listOfDays = sheet.cell_value(i, 5).replace(" ", "")
            listOfDays = listOfDays[1:-1]
            listOfDays = listOfDays.split(',')
 
            if(len(listOfDays) > 1):
                for j in range(len(listOfDays)):
                    obj = Flight()
                    obj.source = sheet.cell_value(i, 0)
                    obj.destination = sheet.cell_value(i, 1)
                    obj.departureTime = sheet.cell_value(i, 2)
                    obj.arrivalTime = sheet.cell_value(i, 3)
                    obj.flightNumber = sheet.cell_value(i, 4)
                    obj.day = listOfDays[j]
                    self.__flights.append(obj)
                    self.__flights[i - 1].setActualTime()
            else:
                obj = Flight()
                obj.source = sheet.cell_value(i, 0)
                obj.destination = sheet.cell_value(i, 1)
                obj.departureTime = sheet.cell_value(i, 2)
                obj.arrivalTime = sheet.cell_value(i, 3)
                obj.flightNumber = sheet.cell_value(i, 4)
                obj.day = (listOfDays[0])
                self.__flights.append(obj)
                self.__flights[i - 1].setActualTime()
                
    def getFlights(self) :
        return self.__flights

    flights = property(getFlights)            
            
 
class City:
    
    def __init__(self) :
        self.__name = ''
        self.__latitude = ''
        self.__longitude = ''
 
    def setName(self, name):  
        self.__name = name  
 
    def getName(self):      
        return self.__name
    
    name = property(getName,setName)
    
    def setLatitude(self, latitude):  
        self.__latitude = latitude
 
    def getLatitude(self):      
        return self.__latitude
    
    latitude = property(getLatitude,setLatitude)
    
    def setLongitude(self, longitude):  
        self.__longitude = longitude
 
    def getLongitude(self):      
        return self.__longitude
    
    longitude = property(getLongitude,setLongitude)   
 
 
class CitiesContainer :
    
    def __init__(self) : 
        self.__cities = []
        loc = ("cities.xlsx")      
        # To open Workbook 
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0)
 
        for i in range (1,21): 
            obj = City()
            for j in range (0,3):
                if(j == 0):
                    obj.name = sheet.cell_value(i, j)
                elif(j == 1):
                    obj.latitude = sheet.cell_value(i, j)
                else:
                    obj.longitude = sheet.cell_value(i, j)
 
            self.cities.append(obj)
            
    def getCities(self) :
        return self.__cities

    cities = property(getCities)           
 
 
class DistanceController :
    
    def distance(self,lat1, lat2, lon1, lon2): 
        # The math module contains a function named radians which converts from degrees to radians. 
        lon1 = radians(lon1) 
        lon2 = radians(lon2) 
        lat1 = radians(lat1) 
        lat2 = radians(lat2) 

        # Haversine formula  
        dlon = lon2 - lon1  
        dlat = lat2 - lat1 
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))  
        # Radius of earth in kilometers. Use 3956 for miles 
        r = 6371
        # calculate the result 
        return(c * r) 
 
    def estimatedTime(self,distance):
        numFloat = float((float(distance) / 800))
        numInt = int((distance) / 800)
        estimateTime = (numInt * 60) + int((numFloat - numInt) * 60 / 100)
        return estimateTime
 
    
class Node :   
    
    def __init__(self): 
        self.__city = ''
        self.__path = []
        self.__g = 0.0
        self.__h = 0.0
        self.__f = 0.0
    
    def __lt__(a,b):
        return a.f < b.f
    
    def setPath(self, path):
        self.__path = path.copy()
        
    def getPath(self):
        return self.__path
    
    path = property(getPath,setPath)
    
    def setCity(self, city):
        self.__city = city
    
    def getCity(self):
        return self.__city
    
    city = property(getCity,setCity)
    
    def setG(self, lastNode):
        waitingTime = 0.0
        count = self.__path[len(self.__path) - 1].actualTimeInMinutes + lastNode.g
        if(len(lastNode.path) > 0):
            oldTime = lastNode.path[len(lastNode.path) - 1].arrivalTime.split(':')
            newTime = self.__path[len(self.__path) - 1].departureTime.split(':')
            oldHours = int(oldTime[0])
            newHours = int (newTime[0])
            oldMinutes = int(oldTime[1])
            newMinutes = int (newTime[1])
            if(lastNode.path[len(lastNode.path) - 1].day == self.__path[len(self.__path) - 1].day):
                waitingTime += ((newHours - oldHours)*60)
                if(newMinutes >= oldMinutes):
                    waitingTime += newMinutes - oldMinutes
                else :
                    ans = oldMinutes - newMinutes
                    tMin = 60 - ans
                    waitingTime -= 60
                    waitingTime += tMin
            else:
                t = TimeComparisonHandler()
                num = 0
                if (t.cmp(lastNode.path[len(lastNode.path)-1].departureTime,lastNode.path[len(lastNode.path)-1].arrivalTime)) == True :
                    num = 1
                oldDay = days[lastNode.path[len(lastNode.path) - 1].day] + num 
                newDay = days[self.__path[len(self.__path) - 1].day]
                waitingTime = (newDay - oldDay) * 24 * 60
                if(newHours < oldHours):
                    waitingTime -= ((oldHours - newHours)*60)
                else:
                    waitingTime += ((newHours - oldHours)*60)
 
                if(newMinutes >= oldMinutes):
                    waitingTime += newMinutes - oldMinutes
                else :
                    ans = oldMinutes - newMinutes
                    tMin = 60 - ans
                    waitingTime -= 60
                    waitingTime += tMin    
        self.__g = count + waitingTime
 
    def setH(self,destination):
        heuristicController  = HeuristicController()
        self.__h = (heuristicController.getEstimatedTime(self.city,destination))
        
    def getH(self):
        return self.__h
    
    h = property(getH)
    
    def getG(self):
        return self.__g
    
    g = property(getG)
    
    def setF(self) :
        self.__f = self.__g + self.__h
    
    def getF(self):
        return self.__f
    
    f = property(getF)
    
class TimeComparisonHandler:
    
    def cmp (self,departureTime,arrivalTime) :
        newTime = departureTime.split(':')
        oldTime = arrivalTime.split(':')
        oldHours = int(oldTime[0])
        newHours = int (newTime[0])
        oldMinutes = int(oldTime[1])
        newMinutes = int (newTime[1])  
        if  oldHours > newHours :
            return False
        elif oldHours == newHours :
            if oldMinutes >= newMinutes :
                return False
        return True
 
class PathHandler :
    
    def __init__(self,source,destination,listOfDays) :
        self.__source = source
        self.__finalDestination = destination
        self.__f = FlightContainer()
        self.__openList = []
        self.__closedList = []
        self.__listOfDays = []
        self.__listOfDays = listOfDays.copy()
        
    def setListOfDays(self,listOfDays) :
        self.__listOfDays = []
        self.__listOfDays = listOfDays.copy()
        
    def getListOfDays(self) :
        return self.__listOfDays
    
    listOfDays = property(getListOfDays,setListOfDays)
        
    def _getAvailableFlights(self,currentNode):
        listOfFlights = []
        t = TimeComparisonHandler()
 
        for i in range(len(self.__f.flights)):
            if(self.__f.flights[i].source == currentNode.city):
                flag = True
                #filter1
                if (days[self.__f.flights[i].day] >= days[self.__listOfDays[0]] and days[self.__f.flights[i].day] <= days[self.__listOfDays[1]]) == False:
                    flag = False
 
                #filter2
                if(t.cmp(self.__f.flights[i].departureTime,self.__f.flights[i].arrivalTime) == True) and (days[self.__f.flights[i].day] == 7) :
                    flag = False
 
 
                if len(currentNode.path) > 0 :
                    #filter3
                    count = 0
                    if (t.cmp(currentNode.path[len(currentNode.path)-1].departureTime,currentNode.path[len(currentNode.path)-1].arrivalTime)) == True :
                            count = 1
                    if days[currentNode.path[len(currentNode.path)-1].day]+count > days[self.__f.flights[i].day] :
                        flag = False
                    elif days[currentNode.path[len(currentNode.path)-1].day]+count == days[self.__f.flights[i].day] :
                        if(t.cmp(self.__f.flights[i].departureTime,currentNode.path[len(currentNode.path)-1].arrivalTime)) == False :
                            flag = False
 
                    #filter4            
                    for j in range(len(self.__closedList)) :
                        if (self.__f.flights[i].destination == self.__closedList[j].city):
                            flag = False
                            break
                if(flag == True) :
                    listOfFlights.append(self.__f.flights[i])
        return listOfFlights
 
    def _removeDuplicates(self):
        i = 0
        while (i < len(self.__openList)-1) :
            j = i+1
            while(j < len(self.__openList)) :
                if(self.__openList[i].city == self.__openList[j].city) :
                    self.__openList.remove(self.__openList[j])
                    j-=1
                j+=1
            i+=1
 
    def getTheGoal(self) :
        self.__openList = []
        self.__closedList = []
        firstNode = Node()
        firstNode.city = self.__source
        self.__openList.append(firstNode)
        while(len(self.__openList) != 0) :
            currentNode = self.__openList.pop(0)
            self.__closedList.append(currentNode)
            if(currentNode.city == self.__finalDestination) :
                return currentNode
            flights = self._getAvailableFlights(currentNode)
            for i in range (len(flights)) :
                node = Node()
                node.city = flights[i].getDestination()
                node.path = currentNode.path
                node.path.append(flights[i])
                node.setG(currentNode)
                node.setH(self.__finalDestination)
                node.setF()
                self.__openList.append(node)
            self.__openList.sort()
            self._removeDuplicates()
        return False 
    
def getKey(val): 
    for key, value in days.items(): 
         if val == value: 
             return key 
         
def travel(source,destination,listOfDays) :
    pathHandler = PathHandler(source,destination,listOfDays)
    if(source != destination) :
        goal = pathHandler.getTheGoal() 
        if(goal == False) :
            if(listOfDays[1] == 'fri' and listOfDays[0]!='sat') :
                day = getKey(days[listOfDays[0]] - 1)
                listOfDays[0] =  day
                pathHandler.listOfDays = listOfDays
                goal = pathHandler.getTheGoal()
                
            elif(listOfDays[1] !='fri' and listOfDays[0]=='sat') :
                day = getKey(days[listOfDays[len(listOfDays) - 1]] + 1)
                listOfDays[1] = day
                pathHandler.listOfDays = listOfDays
                goal = pathHandler.getTheGoal()
                
            elif(listOfDays[1] !='fri' and listOfDays[0]!='sat') :
                day = getKey(days[listOfDays[len(listOfDays) - 1]] + 1)
                listOfDays[1] = day
                day = getKey(days[listOfDays[0]] - 1)
                listOfDays[0] = day
                pathHandler.listOfDays = listOfDays
                goal = pathHandler.getTheGoal()
                
            if(goal == False) :
                print('no answer found!')
            else :
                for i in range (len(goal.path)):
                    print("step " , i+1 , ": use Flight " , goal.path[i].flightNumber , " from " , goal.path[i].source , " to ", goal.path[i].destination , ". Departure Time : " , goal.path[i].departureTime , " and Arrival Time : " , goal.path[i].arrivalTime," and Flight Start Day : ",goal.path[i].day)
        else:
            for i in range (len(goal.path)):
                print("step " , i+1 , ": use Flight " , goal.path[i].flightNumber , " from " , goal.path[i].source , " to ", goal.path[i].destination , ". Departure Time : " , goal.path[i].departureTime , " and Arrival Time : " , goal.path[i].arrivalTime," and Flight Start Day : ",goal.path[i].day)
 
#main
query = input() 
temp = query.split(',')
source = temp[0]
destination = temp[1]
listOfDays = []
listOfDays = temp[2:len(temp)]
listOfDays[0] = listOfDays[0].replace("[","")
listOfDays[len(listOfDays) - 1] = listOfDays[len(listOfDays) - 1].replace("]","")
travel(source, destination, listOfDays)
sys.exit()