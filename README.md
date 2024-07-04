# Operating_Systems
## Process Scheduling and Memory Management Simulator
### Overview
This project simulates process scheduling and memory management using three algorithms:
- First-Come, First-Served (FCFS)
- Shortest Remaining Time First (SRTF)
- Round Robin (RR)
It also includes contiguous memory allocation techniques.

### Features
Simulates scheduling of processes with random or user-defined attributes.
Implements memory management with First-Fit allocation.
Displays metrics such as average waiting time, average turnaround time, CPU utilization, and memory utilization.

### Prerequisites
Python 3.6 or higher


Run the simulator:
python cli.py


### Follow the prompts to enter:
- Number of processes
- Maximum arrival time, burst time, and memory size for processes
- Time quantum for Round Robin
- Total memory size for the Memory Manager
Select a scheduling algorithm:
- 1 for FCFS
- 2 for SRTF
- 3 for RR
View the simulation results, including Gantt charts and performance metrics.

### File Structure
- cli.py: Command-line interface to interact with the simulator.
- process.py: Defines the Process class.
- memory_manager.py: Defines the MemoryManager class.
- fcfs.py: Implements the FCFS scheduling algorithm.
- srtf.py: Implements the SRTF scheduling algorithm.
- round_robin.py: Implements the Round Robin scheduling algorithm.
