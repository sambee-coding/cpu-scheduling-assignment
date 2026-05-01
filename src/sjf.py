def sjf_non_preemptive(processes):
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
            # Find the next arrival time to jump current_time
            not_completed = [p.arrival_time for i, p in enumerate(processes) if not is_completed[i]]
            if not_completed:
                next_arrival = min(not_completed)
                gantt_chart.append((current_time, next_arrival, "IDLE"))
                current_time = next_arrival
            continue
            
        # Select process with minimum burst time
        idx, p = min(available_processes, key=lambda x: (x[1].burst_time, x[1].arrival_time))
        
        start_time = current_time
        current_time += p.burst_time
        p.completion_time = current_time
        is_completed[idx] = True
        completed_count += 1
        
        gantt_chart.append((start_time, current_time, f"P{p.pid}"))
        
    return gantt_chart
