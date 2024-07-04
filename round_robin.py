from process import Process
from memory_manager import MemoryManager

def round_robin(process_list, memory_manager, time_quanta):
    t = 0
    gantt = []
    completed = {}
    queue = []

    process_list.sort(key=lambda p: p.arrival_time)
    while process_list or queue:
        while process_list and process_list[0].arrival_time <= t:
            queue.append(process_list.pop(0))

        if not queue:
            gantt.append("Idle")
            t += 1
            continue

        process = queue.pop(0)

        if not memory_manager.first_fit_allocate(process):
            print(f"Not enough memory for process {process.pid}")
            continue

        gantt.append(process.pid)
        if process.burst_time <= time_quanta:
            t += process.burst_time
            ct = t
            tt = ct - process.arrival_time
            wt = tt - process.burst_time
            completed[process.pid] = [ct, tt, wt]
        else:
            t += time_quanta
            process.burst_time -= time_quanta
            queue.append(process)

    print(f"Gantt Chart: {gantt}")
    print(f"Process Information:")
    for pid, (ct, tt, wt) in completed.items():
        print(f"Process {pid}: Completion Time = {ct}, Turnaround Time = {tt}, Waiting Time = {wt}")

    avg_wt = sum(wt for _, (_, _, wt) in completed.items()) / len(completed)
    avg_tt = sum(tt for _, (ct, tt, _) in completed.items()) / len(completed)

    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tt:.2f}")

if __name__ == "__main__":
    process_list = [Process("p1", 2, 6, 3), Process("p2", 5, 2, 2), Process("p3", 1, 8, 4), Process("p4", 0, 3, 1), Process("p5", 4, 4, 2)]
    time_quanta = 3
    memory_manager = MemoryManager(size=10)
    round_robin(process_list, memory_manager, time_quanta)
