import random
from process import Process
from memory_manager import MemoryManager
from fcfs import fcfs
from srtf import srtf
from round_robin import round_robin

def generate_processes(n, max_arrival_time, max_burst_time, max_memory):
    processes = []
    for i in range(n):
        arrival_time = random.randint(0, max_arrival_time)
        burst_time = random.randint(1, max_burst_time)
        memory = random.randint(1, max_memory)
        pid = f'p{i+1}'
        processes.append(Process(pid, arrival_time, burst_time, memory))
    return processes

def main():
    print("Welcome to the Process Scheduling and Memory Management Simulator")

    num_processes = int(input("Enter the number of processes: "))
    max_arrival_time = 10 
    max_burst_time = 10  
    max_memory = 5  
    memory_size = int(input("Enter the total memory size for the Memory Manager: "))

    processes = generate_processes(num_processes, max_arrival_time, max_burst_time, max_memory)
    memory_manager = MemoryManager(size=memory_size)

    print("\nSelect Scheduling Algorithm:")
    print("1. First-Come, First-Served (FCFS)")
    print("2. Shortest Remaining Time First (SRTF)")
    print("3. Round Robin (RR)")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        fcfs(processes, memory_manager)
    elif choice == 2:
        srtf(processes, memory_manager)
    elif choice == 3:
        time_quanta = int(input("Enter the time quantum for Round Robin: "))
        round_robin(processes, memory_manager, time_quanta)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
