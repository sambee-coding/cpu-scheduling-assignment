import copy
from models import Process
from fcfs import fcfs
from sjf import sjf_non_preemptive
from srtf import srtf
from round_robin import round_robin
# Import Banker's algorithm
try:
    import bankers
except ImportError:
    bankers = None

def get_scheduling_data():
    """Returns sample process data for scheduling from the assignment example."""
    return [
        Process(pid="P1", arrival_time=0, burst_time=7),
        Process(pid="P2", arrival_time=2, burst_time=4),
        Process(pid="P3", arrival_time=4, burst_time=1),
        Process(pid="P4", arrival_time=5, burst_time=4),
    ]

def input_processes():
    """
    Reads process data from the terminal.
    Matches the 'input_processes()' requirement in the assignment diagram.
    """
    processes = []
    try:
        n_str = input("\nEnter number of processes: ").strip()
        if not n_str: return []
        n = int(n_str)
        
        print("Enter data for each process: <ID> <Arrival_Time> <Burst_Time> (e.g., P1 0 7)")
        for _ in range(n):
            line = input("> ").strip()
            parts = line.split()
            if len(parts) == 3:
                pid = parts[0]
                at = int(parts[1])
                bt = int(parts[2])
                processes.append(Process(pid=pid, arrival_time=at, burst_time=bt))
            else:
                print("Invalid format. Skipping this entry.")
    except ValueError:
        print("Invalid input. Please use integers for Arrival/Burst.")
    return processes

def run_bankers():
    """Runs the Banker's algorithm simulation."""
    if not bankers:
        print("\n[!] banker's algorithm module not found.")
        return

    print("\n" + "=" * 60)
    print("         BANKER'S ALGORITHM (Deadlock Avoidance)")
    print("=" * 60)

    # Sample Data
    n = 5 # Processes
    m = 3 # Resources
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    available = [3, 3, 2]

    try:
        if hasattr(bankers, 'bankers_algorithm'):
            result = bankers.bankers_algorithm(n, m, allocation, max_need, available)
            if hasattr(bankers, 'print_results'):
                bankers.print_results(n, m, allocation, max_need, available, result)
            else:
                print(f"Safe sequence: {result}")
    except Exception as e:
        print(f"[!] Error running Banker's algorithm: {e}")

def main():
    """
    Main entry point. 
    Orchestrates the simulation as required by the assignment structure.
    """
    print("=" * 60)
    print("        OS ALGORITHMS INTEGRATED SIMULATOR")
    print("=" * 60)
    
    # Choose input method
    print("\nHow would you like to provide process data?")
    print("1. Use Assignment Sample Data (P1-P4)")
    print("2. Enter data manually (input_processes)")
    choice = input("Choice (1 or 2): ").strip()

    if choice == '2':
        original_processes = input_processes()
    else:
        print("\nUsing Assignment Sample Data...")
        original_processes = get_scheduling_data()
        
    if not original_processes:
        print("No processes to schedule. Exiting.")
        return

    # RUN SCHEDULING ALGORITHMS
    print("\n>>> Part 1: CPU Scheduling Simulation")
    
    algorithms = [
        ("FIRST COME FIRST SERVED (FCFS)", fcfs),
        ("SHORTEST JOB FIRST (SJF)", sjf_non_preemptive),
        ("SHORTEST REMAINING TIME FIRST (SRTF)", srtf),
        ("ROUND ROBIN (RR) - Q=2", round_robin),
    ]

    for name, func in algorithms:
        print(f"\n{'#' * 15} {name} {'#' * 15}")
        proc_copy = copy.deepcopy(original_processes)
        func(proc_copy)
        print("-" * 60)

    # RUN BANKER'S ALGORITHM
    print("\n>>> Part 2: Deadlock Avoidance")
    run_bankers()

    print("\n" + "=" * 60)
    print("ALL SIMULATIONS COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    main()
