from simulation import TicketCounterSimulation


def main():
    numMin = int(raw_input("Number of minutes to simulate: "))
    numAgent = int(raw_input("Number of ticket agents: "))
    serviceTime = int(raw_input("Average service time per passenger: "))
    arrivalTime = int(raw_input("Average time between passenger arrival:"))

    sim = TicketCounterSimulation(numAgent, numMin, arrivalTime, serviceTime)

    sim.run() 
    sim.printResults()




main()
