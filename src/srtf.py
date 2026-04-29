from models import Process, calculate_metrics, print_table, print_gantt_chart

def srtf(processes: list[Process]):
    """
    Implementation of Shortest Remaining Time First (SRTF) scheduling algorithm.
    SRTF is the preemptive version of Shortest Job First (SJF).
    """
    n = len(processes)
    current_time = 0
    completed = 0
    gantt_chart = []
    
    # Sort processes by arrival time initially
    processes.sort(key=lambda x: x.arrival_time)
    
    last_pid = None
    start_time = 0

    while completed < n:
        # Filter processes that have arrived and are not finished
        available_processes = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]

        if not available_processes:
            # CPU is idle
            if last_pid is not None:
                gantt_chart.append((start_time, current_time, f"P{last_pid}"))
                last_pid = None
            
            # Find next arrival time to skip ahead
            next_arrival = min((p.arrival_time for p in processes if p.remaining_time > 0), default=None)
            if next_arrival is not None:
                if last_pid == "IDLE":
                     pass # Already idle
                else:
                    gantt_chart.append((current_time, next_arrival, "IDLE"))
                current_time = next_arrival
            continue

        # Pick process with shortest remaining time
        current_process = min(available_processes, key=lambda x: (x.remaining_time, x.arrival_time))

        # Handle Gantt Chart logic for preemption
        if last_pid != current_process.pid:
            if last_pid is not None:
                gantt_chart.append((start_time, current_time, f"P{last_pid}"))
            start_time = current_time
            last_pid = current_process.pid

        # Execute for 1 unit of time
        current_process.remaining_time -= 1
        current_time += 1

        # Check if process is finished
        if current_process.remaining_time == 0:
            current_process.completion_time = current_time
            completed += 1
            # Close the last segment in Gantt Chart
            gantt_chart.append((start_time, current_time, f"P{current_process.pid}"))
            last_pid = None

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
        Process(pid=1, arrival_time=0, burst_time=8),
        Process(pid=2, arrival_time=1, burst_time=4),
        Process(pid=3, arrival_time=2, burst_time=9),
        Process(pid=4, arrival_time=3, burst_time=5),
    ]
    
    print("Executing SRTF Scheduling...")
    srtf(sample_processes)
