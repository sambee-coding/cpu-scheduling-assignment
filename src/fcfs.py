from models import Process, calculate_metrics, print_table, print_gantt_chart

def fcfs(processes: list[Process]):
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
        
    # Calculate metrics and display
    avg_wt, avg_tat = calculate_metrics(processes)
    print_table(processes)
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print_gantt_chart(gantt_chart)