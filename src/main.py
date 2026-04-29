import copy
from models import Process
from fcfs import fcfs
from sjf import sjf
from srtf import srtf
from round_robin import round_robin

def get_sample_data():
    """Returns a predefined list of Process objects for simulation."""
    return [
        Process(pid=1, arrival_time=0, burst_time=8),
        Process(pid=2, arrival_time=1, burst_time=4),
        Process(pid=3, arrival_time=2, burst_time=9),
        Process(pid=4, arrival_time=3, burst_time=5),
    ]

def get_user_input():
    """Reads process data from the terminal."""
    processes = []
    print("\n--- Manual Process Entry ---")
    print("Format: <PID_as_integer> <Arrival_Time> <Burst_Time> (e.g., 1 0 7)")
    print("Type 'done' to finish.")
    
    while True:
        line = input("> ").strip().lower()
        if line == 'done':
            break
        try:
            parts = list(map(int, line.split()))
            if len(parts) == 3:
                processes.append(Process(pid=parts[0], arrival_time=parts[1], burst_time=parts[2]))
            else:
                print("Invalid format. Use: PID AT BT")
        except ValueError:
            print("Invalid input. Please enter integers only.")
    return processes

def run_simulation():
    print("=" * 60)
    print("        OS CPU SCHEDULING ALGORITHM SIMULATOR")
    print("=" * 60)
    
    # Choose input method
    choice = input("Use sample data? (y/n): ").strip().lower()
    if choice == 'y':
        original_processes = get_sample_data()
    else:
        original_processes = get_user_input()
        
    if not original_processes:
        print("No processes to schedule. Exiting.")
        return

    # List of algorithms to run
    # Format: (Display Name, Function, [optional extra args])
    algorithms = [
        ("FIRST COME FIRST SERVED (FCFS)", fcfs),
        ("SHORTEST JOB FIRST (SJF)", sjf),
        ("SHORTEST REMAINING TIME FIRST (SRTF)", srtf),
        ("ROUND ROBIN (RR) - Quantum = 2", round_robin),
    ]

    for name, func in algorithms:
        print(f"\n\n{'#' * 15} {name} {'#' * 15}")
        
        # CRITICAL: Deep copy to prevent mutation of original arrival/burst times
        # and to ensure each algorithm starts with a fresh list of Process objects.
        process_list_copy = copy.deepcopy(original_processes)
        
        # Execute the algorithm
        # All algorithms are now standardized to call their own print_table and print_gantt_chart
        func(process_list_copy)
        
        print(f"\n{'=' * 60}")

    print("\nSimulation completed successfully.")

if __name__ == "__main__":
    run_simulation()
