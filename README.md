# Best-Flights-using-A-star-algorithm
Program helps you to get the Best Flights(less distance and time) from one city to another using A* algorithm 

input:
The input is something like that : source,destination,[start available day,end].

Cairo,Aswan,[tue,friday]

conditions :
- No flight takes more than 24 hours.
- All flights duration is within only one week start from Saturday 0:00 to friday 23:59

System Component :

1.	Flight Class: this class contains information of a flight (to encapsulate the flight in one object) and setters and getters for the attributes which are:

-	Source

-	Destination

-	Departure Time

-	Arrival Time

-	Flight Number

-	Actual Time in Minutes: This is the difference between arrival time and departure time in minutes.

-	Day

2.	Heuristic Controller Class: this class is responsible for get the heuristic function for each city the user can go (between the city and the goal) to through calling function called: “getEstimatedTime”.


3.	Flight Container Class: this class contain a list of flight objects, called “flights”, of all flights that exist in an excel file called “flights” and read the data and store it into the list (flights) and getter for the list.


4.	City Class: this class contains information about every city (to encapsulate the city in one object) and its latitude, its longitude, setters and getters for each one.


5.	Cities Container Class: this class contain a list of city objects, called “cities”, of all cities that exist in an excel file called “cities” and read the data and store it into the list (cities) and getter for the list.

6.	Distance Controller Class: this class has two function:

-	distance: this function is responsible for calculate the distance between two cities using their latitude and longitude.

-	estimatedTime: this function take a distance and return the estimated time by divide this distance over 800 which is average speed of a plane.
-	This two functions will be used to get the heuristic distance in the HeuristicControllerClass.


7.	Node Class: this class represent each city that the user can visit as a node which has:

-	city: name of the city.

-	path: is a list contain all the flights that the user take to reach this city.

-	g: is the actual time that the user will take to reach the specific node (city).

-	h: is the heuristic value to a specific node (city).

-	f: is the value of g plus the value of h.

-	set g: calculates the total cost to reach this city includes the waiting time between each two flights and the distance from the start until we reach the city(node)

-	set h: that call getEstimatedTime from Heuristic Controller Class to get the heuristic distance between the city and the goal node 

-	set f : add g and h and put them in f that we will sort the open list according to it 
 

-	setters and getters for each attribute.

8.	Time Comparison Handler Class: this class has a function called “cmp” that takes two times (Arrival Time & Departure Time) and return ‘true’ if the departure time is bigger than the arrival time. In other word, this function return ‘true’ for example if the user travel on Monday 21:00 pm and arrive on Tuesday 2:00 am.


9.	Path Handler Class: this class has the following:

-	source: is the source city that the user want to travel from.

-	finalDestination: is the destination city that the user want to travel to.

-	listOfDays: is a list contain the available days for the user to travel in.

-	getAvailableFlights: a function that get all available flights from a certain city and return a list contains these flights after applying our conditions as no new flight can start before the old flight arrives.

-	removeDuplicates: a function that remove the duplicated flights in a list.

-	getTheGoal: a function that get the final path the user will take to reach his destination by calling getAvailableFlights to get the available flight from the current node then calculate its g,h and f then add it to the openlist if not visited, then sort according to f and get the new node and so on… until we finds the goal


10.	Travel:  a function that takes the input and calls the function to get the path for the user and if no path found it add to the list of days a day before the first day or a day after the last day or both.


