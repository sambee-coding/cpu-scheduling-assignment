from models import Process, calculate_metrics, print_table, print_gantt_chart

def sjf(processes: list[Process]):
    """
    Implementation of Shortest Job First (SJF) scheduling algorithm (Non-preemptive).
    """
    n = len(processes)
    current_time = 0
    completed_count = 0
    is_completed = [False] * n
    gantt_chart = []
    
    while completed_count < n:
        available_processes = [
            (i, p) for i, p in enumerate(processes) 
            if p.arrival_time <= current_time and not is_completed[i]
        ]
        
        if not available_processes:
            next_arrival = min(p.arrival_time for i, p in enumerate(processes) if not is_completed[i])
            gantt_chart.append((current_time, next_arrival, "IDLE"))
            current_time = next_arrival
            continue
            
        idx, p = min(available_processes, key=lambda x: (x[1].burst_time, x[1].arrival_time))
        
        start_time = current_time
        current_time += p.burst_time
        p.completion_time = current_time
        is_completed[idx] = True
        completed_count += 1
        
        gantt_chart.append((start_time, current_time, f"P{p.pid}"))
        
    avg_wt, avg_tat = calculate_metrics(processes)
    print_table(processes)
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print_gantt_chart(gantt_chart)
