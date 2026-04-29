"""
Banker's Algorithm — Deadlock Avoidance
Determines whether the system is in a safe state by finding
a safe sequence of process execution.
"""


def bankers_algorithm(num_processes, num_resources, allocation, max_need, available):
    """
    Runs the Banker's Algorithm.

    Args:
        num_processes (int): number of processes
        num_resources (int): number of resource types
        allocation (list of list): currently allocated resources [process][resource]
        max_need (list of list): maximum resource need [process][resource]
        available (list): currently available resources [resource]

    Returns:
        dict with:
            - safe (bool): whether the system is in a safe state
            - safe_sequence (list): order of process execution (if safe)
            - need (list of list): calculated need matrix
    """
    # Calculate Need matrix: Need[i][j] = Max[i][j] - Allocation[i][j]
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
            if not finish[i]:
                # Check if need[i] <= work
                if all(need[i][j] <= work[j] for j in range(num_resources)):
                    # Process i can finish — release its resources
                    for j in range(num_resources):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True
                    break  # restart scan

        if not found:
            # No process could proceed — unsafe state
            return {
                "safe": False,
                "safe_sequence": [],
                "need": need,
            }

    return {
        "safe": True,
        "safe_sequence": safe_sequence,
        "need": need,
    }


def request_resources(process_id, request, allocation, max_need, available, num_resources):
    """
    Handles a resource request from a process using the Banker's Algorithm.

    Args:
        process_id (int): the requesting process index
        request (list): requested resources
        allocation, max_need, available: current system state
        num_resources (int): number of resource types

    Returns:
        dict with:
            - granted (bool): whether the request can be granted
            - message (str): explanation
            - new_state (dict): updated allocation/available if granted
    """
    num_processes = len(allocation)

    # Step 1: Check request <= need
    need = [
        [max_need[i][j] - allocation[i][j] for j in range(num_resources)]
        for i in range(num_processes)
    ]
    if any(request[j] > need[process_id][j] for j in range(num_resources)):
        return {
            "granted": False,
            "message": "Error: Process has exceeded its maximum claim.",
            "new_state": None,
        }

    # Step 2: Check request <= available
    if any(request[j] > available[j] for j in range(num_resources)):
        return {
            "granted": False,
            "message": "Resources not available. Process must wait.",
            "new_state": None,
        }

    # Step 3: Pretend to allocate and check safety
    new_available = available[:]
    new_allocation = [row[:] for row in allocation]
    new_max = [row[:] for row in max_need]

    for j in range(num_resources):
        new_available[j] -= request[j]
        new_allocation[process_id][j] += request[j]

    result = bankers_algorithm(num_processes, num_resources, new_allocation, new_max, new_available)

    if result["safe"]:
        return {
            "granted": True,
            "message": f"Request granted. Safe sequence: {result['safe_sequence']}",
            "new_state": {
                "allocation": new_allocation,
                "available": new_available,
            },
        }
    else:
        return {
            "granted": False,
            "message": "Request denied — would lead to an unsafe state.",
            "new_state": None,
        }


def print_results(num_processes, num_resources, allocation, max_need, available, result):
    need = result["need"]

    print("\n===== Banker's Algorithm =====")
    print(f"\nNumber of Processes : {num_processes}")
    print(f"Number of Resources : {num_resources}")

    print(f"\n{'':>4} {'Allocation':<{num_resources * 3}} {'Max':<{num_resources * 3}} {'Need':<{num_resources * 3}}")
    print("-" * (10 + num_resources * 9))
    for i in range(num_processes):
        alloc_str = " ".join(str(allocation[i][j]) for j in range(num_resources))
        max_str = " ".join(str(max_need[i][j]) for j in range(num_resources))
        need_str = " ".join(str(need[i][j]) for j in range(num_resources))
        print(f"P{i:<3} {alloc_str:<{num_resources * 3}} {max_str:<{num_resources * 3}} {need_str:<{num_resources * 3}}")

    avail_str = " ".join(str(v) for v in available)
    print(f"\nAvailable Resources : {avail_str}")

    if result["safe"]:
        seq = " -> ".join(f"P{p}" for p in result["safe_sequence"])
        print(f"\n✅ System is in a SAFE state.")
        print(f"Safe Sequence : {seq}")
    else:
        print("\n❌ System is in an UNSAFE state. Deadlock may occur.")
