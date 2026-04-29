from collections import deque
from models import Process, calculate_metrics, print_table, print_gantt_chart

def round_robin(processes: list[Process], quantum: int = 2):
    """
    Implementation of Round Robin (RR) scheduling algorithm.
    """
    n = len(processes)
    current_time = 0
    completed = 0
    ready_queue = deque()
    gantt_chart = []
    
    processes.sort(key=lambda x: x.arrival_time)
    added_to_queue = [False] * n
    
    def add_arrived_processes():
        for i in range(n):
            if not added_to_queue[i] and processes[i].arrival_time <= current_time:
                ready_queue.append(processes[i])
                added_to_queue[i] = True

    add_arrived_processes()

    while completed < n:
        if not ready_queue:
            next_arrival = min((p.arrival_time for p in processes if not added_to_queue[processes.index(p)]), default=None)
            if next_arrival is not None:
                gantt_chart.append((current_time, next_arrival, "IDLE"))
                current_time = next_arrival
                add_arrived_processes()
            continue

        process = ready_queue.popleft()
        execution_time = min(process.remaining_time, quantum)
        
        gantt_chart.append((current_time, current_time + execution_time, f"P{process.pid}"))
        
        for _ in range(execution_time):
            current_time += 1
            add_arrived_processes()

        process.remaining_time -= execution_time

        if process.remaining_time == 0:
            process.completion_time = current_time
            completed += 1
        else:
            ready_queue.append(process)

    avg_wt, avg_tat = calculate_metrics(processes)
    print_table(processes)
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print_gantt_chart(gantt_chart)
