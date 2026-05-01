import copy
from dataclasses import dataclass
from fcfs import fcfs
from sjf import sjf_non_preemptive
from srtf import srtf
from round_robin import round_robin
from bankers import bankers_algorithm, print_results, input_bankers_data

@dataclass
class Process:
    """Represents a process for CPU scheduling."""
    pid: str
    arrival_time: int
    burst_time: int
    remaining_time: int = 0
    completion_time: int = 0
    turnaround_time: int = 0
    waiting_time: int = 0

    def __post_init__(self):
        self.remaining_time = self.burst_time

def calculate_metrics(processes):
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

def print_table(processes):
    """Prints the process metrics in a formatted table."""
    print(f"\n{'PID':<5} | {'Arrival':<8} | {'Burst':<6} | {'CT':<5} | {'TAT':<5} | {'WT':<5}")
    print("-" * 50)
    # Sort by PID for consistent output
    for p in sorted(processes, key=lambda x: x.pid):
        print(f"{p.pid:<5} | {p.arrival_time:<8} | {p.burst_time:<6} | {p.completion_time:<5} | {p.turnaround_time:<5} | {p.waiting_time:<5}")

def print_gantt_chart(gantt_chart):
    """Prints a visual Gantt chart representation."""
    print("\n--- Gantt Chart ---")
    for _, _, label in gantt_chart:
        print(f"|  {label}  ", end="")
    print("|")
    for start, _, _ in gantt_chart:
        print(f"{start:<8}", end="")
    if gantt_chart:
        print(gantt_chart[-1][1])

def get_scheduling_data():
    """Returns sample process data for scheduling from the assignment example."""
    return [
        Process(pid="P1", arrival_time=0, burst_time=7),
        Process(pid="P2", arrival_time=2, burst_time=4),
        Process(pid="P3", arrival_time=4, burst_time=1),
        Process(pid="P4", arrival_time=5, burst_time=4),
    ]

def input_processes():
    """Reads process data from terminal as required by Section 4."""
    processes = []
    try:
        n_str = input("\nEnter number of processes: ").strip()
        if not n_str: return []
        n = int(n_str)
        
        print("Enter data for each process: <ID> <Arrival_Time> <Burst_Time> (e.g., P1 0 7)")
        for _ in range(n):
            line = input("> ").strip()
            parts = line.split()
            if len(parts) >= 3:
                pid = parts[0]
                at = int(parts[1])
                bt = int(parts[2])
                processes.append(Process(pid=pid, arrival_time=at, burst_time=bt))
            else:
                print("Invalid format. Skipping.")
    except ValueError:
        print("Invalid input.")
    return processes

def run_bankers():
    """Runs the Banker's algorithm simulation with manual or sample data."""
    print("\n>>> Part 2: Deadlock Avoidance (Banker's Algorithm)")
    print("1. Use Assignment Sample Data")
    print("2. Enter data manually")
    choice = input("Choice: ").strip()

    if choice == '2':
        data = input_bankers_data()
        if not data: return
        n, m, alloc, max_n, avail = data
    else:
        # Sample Data from instructions
        n, m = 5, 3
        alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
        max_n = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
        avail = [3, 3, 2]

    result = bankers_algorithm(n, m, alloc, max_n, avail)
    print_results(n, m, alloc, max_n, avail, result)

def main():
    """Main orchestrator satisfying Requirement 4."""
    print("=" * 60)
    print("        OS ALGORITHMS INTEGRATED SIMULATOR")
    print("=" * 60)
    
    print("\nHow would you like to provide scheduling data?")
    print("1. Use Assignment Sample Data")
    print("2. Enter data manually")
    choice = input("Choice: ").strip()

    if choice == '2':
        original_processes = input_processes()
    else:
        original_processes = get_scheduling_data()
        
    if not original_processes:
        print("No processes found.")
        return

    # Scheduling algorithms execution
    algorithms = [
        ("FIRST COME FIRST SERVED (FCFS)", fcfs),
        ("NON-PREEMPTIVE SJF", sjf_non_preemptive),
        ("SHORTEST REMAINING TIME FIRST (SRTF)", srtf),
        ("ROUND ROBIN (RR) - Q=2", round_robin),
    ]

    for name, func in algorithms:
        print(f"\n{'#' * 15} {name} {'#' * 15}")
        proc_copy = copy.deepcopy(original_processes)
        gantt = func(proc_copy)
        
        # Calculate and display common metrics
        avg_wt, avg_tat = calculate_metrics(proc_copy)
        print_table(proc_copy)
        print(f"\nAverage Waiting Time: {avg_wt:.2f}")
        print(f"Average Turnaround Time: {avg_tat:.2f}")
        print_gantt_chart(gantt)
        print("-" * 60)

    # Banker's algorithm execution
    run_bankers()

    print("\n" + "=" * 60)
    print("ALL SIMULATIONS COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    main()
