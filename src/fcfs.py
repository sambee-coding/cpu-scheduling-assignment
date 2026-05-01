def fcfs(processes):
    """
    Implementation of First Come First Served (FCFS) scheduling algorithm.
    """
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    
    current_time = 0
    gantt_chart = []
    
    for p in processes:
        if current_time < p.arrival_time:
            # CPU is idle
            gantt_chart.append((current_time, p.arrival_time, "IDLE"))
            current_time = p.arrival_time
            
        start_time = current_time
        current_time += p.burst_time
        p.completion_time = current_time
        
        gantt_chart.append((start_time, current_time, f"P{p.pid}"))
        
    return gantt_chart