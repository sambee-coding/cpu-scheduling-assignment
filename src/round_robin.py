from collections import deque
from models import Process, calculate_metrics, print_table, print_gantt_chart

def round_robin(processes: list[Process], quantum: int):
    """
    Implementation of Round Robin (RR) scheduling algorithm.
    """
    n = len(processes)
    current_time = 0
    completed = 0
    ready_queue = deque()
    gantt_chart = []
    
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    
    # Track which processes have entered the queue
    added_to_queue = [False] * n
    
    # Helper to add arrived processes to queue
    def add_arrived_processes():
        for i in range(n):
            if not added_to_queue[i] and processes[i].arrival_time <= current_time:
                ready_queue.append(processes[i])
                added_to_queue[i] = True

    # Initial check
    add_arrived_processes()

    while completed < n:
        if not ready_queue:
            # CPU is idle
            next_arrival = min((p.arrival_time for p in processes if not added_to_queue[processes.index(p)]), default=None)
            if next_arrival is not None:
                gantt_chart.append((current_time, next_arrival, "IDLE"))
                current_time = next_arrival
                add_arrived_processes()
            continue

        process = ready_queue.popleft()
        execution_time = min(process.remaining_time, quantum)
        
        # Update Gantt Chart
        gantt_chart.append((current_time, current_time + execution_time, f"P{process.pid}"))
        
        # Execute the process
        for _ in range(execution_time):
            current_time += 1
            # Check for new arrivals during execution unit by unit (to ensure correct queue order)
            add_arrived_processes()

        process.remaining_time -= execution_time

        if process.remaining_time == 0:
            process.completion_time = current_time
            completed += 1
        else:
            # Process still has work, put it back in queue
            ready_queue.append(process)

    # Calculate metrics
    avg_wt, avg_tat = calculate_metrics(processes)
    
    # Final Output
    print_table(processes)
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print_gantt_chart(gantt_chart)

if __name__ == "__main__":
    # Sample Input
    sample_processes = [
        Process(pid=1, arrival_time=0, burst_time=5),
        Process(pid=2, arrival_time=1, burst_time=3),
        Process(pid=3, arrival_time=2, burst_time=1),
        Process(pid=4, arrival_time=3, burst_time=2),
        Process(pid=5, arrival_time=4, burst_time=3),
    ]
    
    TIME_QUANTUM = 2
    print(f"Executing Round Robin Scheduling (Quantum = {TIME_QUANTUM})...")
    round_robin(sample_processes, TIME_QUANTUM)
