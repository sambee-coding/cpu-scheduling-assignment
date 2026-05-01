"""
Banker's Algorithm — Deadlock Avoidance
"""

def bankers_algorithm(num_processes, num_resources, allocation, max_need, available):
    """Computes system safety and returns a safe sequence if one exists."""
    # Need[i][j] = Max[i][j] - Allocation[i][j]
    need = [
        [max_need[i][j] - allocation[i][j] for j in range(num_resources)]
        for i in range(num_processes)
    ]

    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True
                break

        if not found:
            return {"safe": False, "safe_sequence": [], "need": need}

    return {"safe": True, "safe_sequence": safe_sequence, "need": need}

def input_bankers_data():
    """Reads Banker's Algorithm data from terminal."""
    print("\n--- Banker's Algorithm Input ---")
    try:
        n = int(input("Number of processes: "))
        m = int(input("Number of resource types: "))
        
        print(f"Enter Allocation Matrix:")
        allocation = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]
            
        print(f"Enter Max Need Matrix:")
        max_need = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]
            
        print(f"Enter Available Resources:")
        available = list(map(int, input("> ").split()))
        
        return n, m, allocation, max_need, available
    except:
        return None

def print_results(num_processes, num_resources, allocation, max_need, available, result):
    """Displays the Banker's algorithm results."""
    need = result["need"]
    print("\n" + "=" * 20 + " Banker's Algorithm " + "=" * 20)
    print(f"\n{'PID':<4} {'Allocation':<{num_resources * 4}} {'Max':<{num_resources * 4}} {'Need':<{num_resources * 4}}")
    print("-" * (12 + num_resources * 12))
    
    for i in range(num_processes):
        a = " ".join(map(str, allocation[i]))
        m = " ".join(map(str, max_need[i]))
        n = " ".join(map(str, need[i]))
        print(f"P{i:<3} {a:<{num_resources * 4}} {m:<{num_resources * 4}} {n:<{num_resources * 4}}")

    print(f"\nAvailable Resources: {' '.join(map(str, available))}")
    if result["safe"]:
        print(f"[SAFE] Sequence: {' -> '.join(f'P{p}' for p in result['safe_sequence'])}")
    else:
        print("[UNSAFE] Potential deadlock detected.")
    print("=" * 60)

