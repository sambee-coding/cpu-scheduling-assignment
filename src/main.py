import copy
from models import Process, print_table
# Import the scheduling algorithms
# Note: These imports will work once the files exist in your branch
try:
    from fcfs import fcfs
    from sjf import sjf
except ImportError:
    # Placeholders if files aren't merged yet
    def fcfs(p): print("\n[!] FCFS implementation missing in this branch")
    def sjf(p): print("\n[!] SJF implementation missing in this branch")

from srtf import srtf
from round_robin import round_robin

def get_user_input():
    """
    Reads process data from the user.
    Format: ID ArrivalTime BurstTime (e.g., P1 0 7)
    Enter 'done' to finish.
    """
    processes = []
    print("\n--- Enter Process Data ---")
    print("Format: <ID> <Arrival_Time> <Burst_Time> (e.g., P1 0 7)")
    print("Type 'done' when finished.")
    
    while True:
        line = input("> ").strip()
        if line.lower() == 'done':
            break
        
        try:
            parts = line.split()
            if len(parts) != 3:
                print("Invalid format. Please use: ID Arrival Burst")
                continue
            
            pid, at, bt = parts[0], int(parts[1]), int(parts[2])
            # Store as dictionaries as per team agreement
            processes.append({
                'id': pid,
                'at': at,
                'bt': bt
            })
        except ValueError:
            print("Invalid input. Arrival and Burst times must be integers.")
            
    return processes

def convert_to_models(process_dicts):
    """Converts dictionaries to Process objects for the algorithms."""
    return [Process(pid=p['id'], arrival_time=p['at'], burst_time=p['bt']) for p in process_dicts]

def main():
    print("=" * 40)
    print("   CPU SCHEDULING ALGORITHM SIMULATOR   ")
    print("=" * 40)
    
    # Input Data
    # For quick testing, you can uncomment the sample data below:
    # raw_processes = [
    #     {'id': 'P1', 'at': 0, 'bt': 8},
    #     {'id': 'P2', 'at': 1, 'bt': 4},
    #     {'id': 'P3', 'at': 2, 'bt': 9},
    #     {'id': 'P4', 'at': 3, 'bt': 5},
    # ]
    
    raw_processes = get_user_input()
    
    if not raw_processes:
        print("No processes entered. Exiting.")
        return

    algorithms = [
        ("First Come First Served (FCFS)", fcfs),
        ("Shortest Job First (SJF)", sjf),
        ("Shortest Remaining Time First (SRTF)", srtf),
    ]

    for name, func in algorithms:
        print(f"\n{'#' * 10} {name} {'#' * 10}")
        # Always pass a deep copy to avoid one algorithm affecting the next
        proc_copy = convert_to_models(copy.deepcopy(raw_processes))
        func(proc_copy)
        print("-" * 50)

    # Round Robin handled separately due to Quantum
    print(f"\n{'#' * 10} Round Robin (Quantum = 2) {'#' * 10}")
    rr_proc = convert_to_models(copy.deepcopy(raw_processes))
    round_robin(rr_proc, quantum=2)
    print("-" * 50)

    print("\nSimulation Complete.")

if __name__ == "__main__":
    main()
