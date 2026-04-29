from models import Process, calculate_metrics, print_table, print_gantt_chart

def srtf(processes: list[Process]):
    """
    Implementation of Shortest Remaining Time First (SRTF) scheduling algorithm (Preemptive).
    """
    n = len(processes)
    current_time = 0
    completed = 0
    gantt_chart = []
    
    last_pid = None
    start_time = 0

    while completed < n:
        available_processes = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]

        if not available_processes:
            if last_pid is not None:
                gantt_chart.append((start_time, current_time, f"P{last_pid}"))
                last_pid = None
            
            next_arrival = min((p.arrival_time for p in processes if p.remaining_time > 0), default=None)
            if next_arrival is not None:
                gantt_chart.append((current_time, next_arrival, "IDLE"))
                current_time = next_arrival
            continue

        # Pick process with shortest remaining time
        current_process = min(available_processes, key=lambda x: (x.remaining_time, x.arrival_time))

        if last_pid != current_process.pid:
            if last_pid is not None:
                gantt_chart.append((start_time, current_time, f"P{last_pid}"))
            start_time = current_time
            last_pid = current_process.pid

        current_process.remaining_time -= 1
        current_time += 1

        if current_process.remaining_time == 0:
            current_process.completion_time = current_time
            completed += 1
            gantt_chart.append((start_time, current_time, f"P{current_process.pid}"))
            last_pid = None

    avg_wt, avg_tat = calculate_metrics(processes)
    print_table(processes)
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print_gantt_chart(gantt_chart)
