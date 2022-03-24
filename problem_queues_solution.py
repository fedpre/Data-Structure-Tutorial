from datetime import datetime, timedelta

# Airport departure queue
class Airport_Departures():
    """
    The Airport_Departures class allow users to enter a flight to the flights queue. Flights will be dequeued according to flight departure time compared to the current time. If a flight is a delayed, it will move back in the queue before the closest flight.
    """
    class Flight():
        """
        Each Flight in the queue will have a code assigned to it and the departure time.
        """
        def __init__(self, code, date_string):
            self.code = code
            self.date_time = datetime.strptime(date_string, '%m/%d/%y %H:%M') # '09/18/19 01:55'
        
        def __str__(self):
            """
            Graphical representation of the flight
            """
            return "Flight code {}. Departure time: {}".format(self.code, self.date_time.strftime('%m/%d/%y %H:%M'))

    def __init__(self):
        """
        Initialize an empty queue
        """
        self.queue = []

    def enqueue_flight(self, code, date_string):
        """
        Add a new Flight at the back of the queue with a value and a user attached. The Flight will always be added at the back of the queue.
        """
        # Check if the date and time is greater than current time
        if datetime.strptime(date_string, '%m/%d/%y %H:%M') <= datetime.now():
            print("Invalid flight departure time.")
            return None

        # Check if the flight code is already in the queue
        for flight in self.queue:
            if flight.code == code:
                print("Flight already in the queue.")
                return None
        
        new_flight = Airport_Departures.Flight(code, date_string)
        self.queue.append(new_flight)

    def dequeue_flight(self):
        """
        Dequeue the earliest flight in the queue. 
        """
        # Check if the queue is empty
        if len(self.queue) == 0:
            print("There are no flights in the queue")
            return None

        earliest_flight = self.queue[0]
        for flight in self.queue:
            if flight.date_time < earliest_flight.date_time:
                index = self.queue.index(flight)

        self.queue.pop(index)
        print(f"Flight code {flight.code} has been successfuly dequeued and it is ready to depart on {flight.date_time.strftime('%m/%d/%y %H:%M')}.")
        return None

    def reschedule(self, code, date_string):
        """
        Allows the user to change the departure date and time of a particular flight through the unique code.
        """
        new_date_time = datetime.strptime(date_string, '%m/%d/%y %H:%M')
        if new_date_time <= datetime.now():
            print("Invalid departure date")
            return None

        for flight in self.queue:
            if flight.code == code:
                flight.date_time = new_date_time
                print(f"Departure time of flight code {code} has been updated")
                return None

        print("Flight not found. Please input a correct code.")

    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """
        Suppport the str() function to provide a string representation of the queue.
        """
        string = "["
        for flight in self.queue:
            string += str(flight)  # This uses the __str__ from the Flight class
            string += ", "
        string += "]"
        return string

# Test cases
airport = Airport_Departures()
airport.enqueue_flight('GTJH', '09/18/22 11:55')
airport.enqueue_flight('RTKJ', '07/09/22 22:55')
airport.enqueue_flight('ER34', '05/12/22 09:55')
airport.enqueue_flight('VFT9', '04/29/22 05:55')
airport.enqueue_flight('VFT9', '04/29/22 05:55') # Flight already in the queue
airport.enqueue_flight('V56Y', '02/20/19 01:55') # Invalid flight departure time
print(airport) # [Flight code GTJH. Departure time: 09/18/22 11:55, Flight code RTKJ. Departure time: 07/09/22 22:55, Flight code ER34. Departure time: 05/12/22 09:55, Flight code VFT9. Departure time: 04/29/22 05:55, ]
airport.dequeue_flight() # Flight code VFT9 has been successfuly dequeued and it is ready to depart on 04/29/22 05:55.
airport.dequeue_flight() # Flight code ER34 has been successfuly dequeued and it is ready to depart on 05/12/22 09:55.
print(airport) #[Flight code GTJH. Departure time: 09/18/22 11:55, Flight code RTKJ. Departure time: 07/09/22 22:55, ]
airport.reschedule('GTJH', '11/02/22 13:55') # Departure time of flight code GTJH has been updated
print(airport) # [Flight code GTJH. Departure time: 11/02/22 13:55, Flight code RTKJ. Departure time: 07/09/22 22:55, ]
               