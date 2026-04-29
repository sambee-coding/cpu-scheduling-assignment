import copy
from models import Process
from fcfs import fcfs
from sjf import sjf
from srtf import srtf
from round_robin import round_robin
# Import Banker's algorithm from friend's file
try:
    import bankers
except ImportError:
    bankers = None

def get_scheduling_data():
    """Returns sample process data for scheduling."""
    return [
        Process(pid=1, arrival_time=0, burst_time=8),
        Process(pid=2, arrival_time=1, burst_time=4),
        Process(pid=3, arrival_time=2, burst_time=9),
        Process(pid=4, arrival_time=3, burst_time=5),
    ]

def run_bankers():
    """Runs the Banker's algorithm simulation if the module exists."""
    if not bankers:
        print("\n[!] banker's algorithm module not found.")
        return

    print("\n" + "=" * 60)
    print("         BANKER'S ALGORITHM (Deadlock Avoidance)")
    print("=" * 60)

    # Sample Data from your friend's implementation
    n = 5 # Processes
    m = 3 # Resources
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    available = [3, 3, 2]

    # Use your friend's function to run the logic
    # Note: We assume their function is named 'bankers_algorithm' or similar
    try:
        if hasattr(bankers, 'bankers_algorithm'):
            result = bankers.bankers_algorithm(n, m, allocation, max_need, available)
            if hasattr(bankers, 'print_results'):
                bankers.print_results(n, m, allocation, max_need, available, result)
            else:
                print(f"Safe sequence: {result}")
        else:
            print("[!] Could not find 'bankers_algorithm' function in bankers.py")
    except Exception as e:
        print(f"[!] Error running Banker's algorithm: {e}")

def main():
    print("=" * 60)
    print("        OS ALGORITHMS INTEGRATED SIMULATOR")
    print("=" * 60)
    
    # 1. RUN SCHEDULING ALGORITHMS
    print("\n>>> Part 1: CPU Scheduling Simulation")
    original_processes = get_scheduling_data()
    
    algorithms = [
        ("FIRST COME FIRST SERVED (FCFS)", fcfs),
        ("SHORTEST JOB FIRST (SJF)", sjf),
        ("SHORTEST REMAINING TIME FIRST (SRTF)", srtf),
        ("ROUND ROBIN (RR) - Q=2", round_robin),
    ]

    for name, func in algorithms:
        print(f"\n{'#' * 15} {name} {'#' * 15}")
        proc_copy = copy.deepcopy(original_processes)
        func(proc_copy)
        print("-" * 60)

    # 2. RUN BANKER'S ALGORITHM
    print("\n>>> Part 2: Deadlock Avoidance")
    run_bankers()

    print("\n" + "=" * 60)
    print("ALL SIMULATIONS COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    main()
