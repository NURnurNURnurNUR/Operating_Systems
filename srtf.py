from process import Process
from memory_manager import MemoryManager

def srtf(process_list, memory_manager):
    t = 0
    gantt = []
    burst_times = {}
    for p in process_list:
        burst_times[p.pid] = p.burst_time
    completed = {}
    while process_list:
        available = [p for p in process_list if p.arrival_time <= t]
        if not available:
            gantt.append("Idle")
            t += 1
            continue

        available.sort(key=lambda p: p.burst_time)
        process = available[0]
        if not memory_manager.first_fit_allocate(process):
            print(f"Not enough memory for process {process.pid}")
            continue

        gantt.append(process.pid)
        process.burst_time -= 1
        if process.burst_time == 0:
            t += 1
            ct = t
            tt = ct - process.arrival_time
            wt = tt - burst_times[process.pid]
            completed[process.pid] = [ct, tt, wt]
            memory_manager.deallocate_memory(process.pid)
            process_list.remove(process)
        else:
            t += 1

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
    memory_manager = MemoryManager(size=10)
    srtf(process_list, memory_manager)
