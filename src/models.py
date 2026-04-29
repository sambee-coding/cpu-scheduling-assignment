from dataclasses import dataclass

@dataclass
class Process:
    pid: int
    arrival_time: int
    burst_time: int
    remaining_time: int = 0
    completion_time: int = 0
    turnaround_time: int = 0
    waiting_time: int = 0

    def __post_init__(self):
        self.remaining_time = self.burst_time

def calculate_metrics(processes: list[Process]):
    """Calculates TAT and WT for a list of completed processes."""
    total_wt = 0
    total_tat = 0
    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
    
    avg_wt = total_wt / len(processes) if processes else 0
    avg_tat = total_tat / len(processes) if processes else 0
    return avg_wt, avg_tat

def print_table(processes: list[Process]):
    """Prints the process metrics in a formatted table."""
    print(f"\n{'PID':<5} | {'Arrival':<8} | {'Burst':<6} | {'CT':<5} | {'TAT':<5} | {'WT':<5}")
    print("-" * 50)
    for p in sorted(processes, key=lambda x: x.pid):
        print(f"{p.pid:<5} | {p.arrival_time:<8} | {p.burst_time:<6} | {p.completion_time:<5} | {p.turnaround_time:<5} | {p.waiting_time:<5}")

def print_gantt_chart(gantt_chart: list[tuple[int, int, str]]):
    """
    Prints a visual Gantt chart.
    gantt_chart: List of (start_time, end_time, label)
    """
    print("\n--- Gantt Chart ---")
    for _, _, label in gantt_chart:
        print(f"|  {label}  ", end="")
    print("|")
    for start, _, _ in gantt_chart:
        print(f"{start:<8}", end="")
    if gantt_chart:
        print(gantt_chart[-1][1])
