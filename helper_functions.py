import random
from process import Process

def generate_random_processes(num_processes):
    processes = []
    for i in range(num_processes):
        pid = f"p{i+1}"
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 10)
        memory = random.randint(50, 200)
        processes.append(Process(pid, arrival_time, burst_time, memory))
    return processes

def add_to_queues(process_list):
    ready_queue = []
    waiting_queue = []
    current_time = 0
    for process in sorted(process_list, key=lambda p: p.arrival_time):
        if process.arrival_time <= current_time:
            ready_queue.append(process)
        else:
            waiting_queue.append(process)
    return ready_queue, waiting_queue

def calculate_metrics(completed):
    total_wt = sum(times[2] for times in completed.values())
    total_tt = sum(times[1] for times in completed.values())
    avg_wt = total_wt / len(completed)
    avg_tt = total_tt / len(completed)
    return avg_wt, avg_tt
