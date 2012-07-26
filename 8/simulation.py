# Implementation of the main simulation class.
from array import Array
from llistqueue import Queue
from simpeople import TicketAgent, Passenger
import random

class TicketCounterSimulation :
# Create a simulation object.
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
# Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

# Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)
        random.seed(4500)

# Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

# Run the simulation using the parameters supplied earlier.
    def run( self ):
        for curTime in range(self._numMinutes + 1) :
            if (random.random() <= self._arriveProb):
               self._handleArrival( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )
            self._passengerQ.show()

# Print the simulation results.
    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
        len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )

# The remaining methods that have yet to be implemented.
    def _handleArrival(self, curTime ): # Handles simulation rule #1.
        self._numPassengers += 1
        passanger = Passenger(self._numPassengers, curTime)
        self._passengerQ.enqueue(passanger)
        print "Time  %2d: Passeger %2d arrived." % \
                (curTime, self._numPassengers)
        return

    def _handleBeginService(self, curTime ): # Handles simulation rule #2.
        while not self._passengerQ.isEmpty():
            free = 0

            for i in range(len(self._theAgents)):
                if self._theAgents[i].isFree():
                    passanger = self._passengerQ.dequeue()
                    self._theAgents[i].startService(passanger, \
                    curTime + self._serviceTime) 
                    free = 1
                    print "Time  %2d: Agent %2d started serving passenger %2d." % \
                        (curTime, self._theAgents[i]._idNum, passanger._idNum) 
                    self._totalWaitTime += curTime - passanger._arrivalTime
                    break;

            # no free
            if free == 0:
                return

    def _handleEndService(self, curTime ): # Handles simulation rule #3.
        for i in range(len(self._theAgents)):
            if self._theAgents[i].isFinished(curTime):
               passanger = self._theAgents[i].stopService()
               print "Time  %2d: Agent %2d stopped serving passenger %2d." % \
                        (curTime, self._theAgents[i]._idNum, passanger._idNum) 
 
