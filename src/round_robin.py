"""
Round Robin (RR) CPU Scheduling Algorithm
Preemptive: each process gets a fixed time slice (quantum).
If not finished, it goes back to the end of the ready queue.
"""

from collections import deque


def round_robin(processes, quantum):
    """
    Runs Round Robin scheduling.

    Args:
        processes: list of dicts with keys:
            - pid, arrival_time, burst_time
        quantum: time slice for each process

    Returns:
        list of dicts with scheduling results per process.
    """
    procs = sorted([p.copy() for p in processes], key=lambda p: p["arrival_time"])
    n = len(procs)

    remaining = {p["pid"]: p["burst_time"] for p in procs}
    start_times = {}
    finish_times = {}

    queue = deque()
    current_time = 0
    idx = 0          # pointer into sorted arrival list
    in_queue = set()

    # Add processes that arrive at time 0
    while idx < n and procs[idx]["arrival_time"] <= current_time:
        queue.append(procs[idx])
        in_queue.add(procs[idx]["pid"])
        idx += 1

    while queue or idx < n:
        if not queue:
            # CPU idle — jump to next arrival
            current_time = procs[idx]["arrival_time"]
            while idx < n and procs[idx]["arrival_time"] <= current_time:
                queue.append(procs[idx])
                in_queue.add(procs[idx]["pid"])
                idx += 1

        proc = queue.popleft()
        pid = proc["pid"]

        # Record first time this process touched the CPU
        if pid not in start_times:
            start_times[pid] = current_time

        # Execute for min(quantum, remaining)
        exec_time = min(quantum, remaining[pid])
        remaining[pid] -= exec_time
        current_time += exec_time

        # Enqueue newly arrived processes during this slice
        while idx < n and procs[idx]["arrival_time"] <= current_time:
            queue.append(procs[idx])
            in_queue.add(procs[idx]["pid"])
            idx += 1

        if remaining[pid] == 0:
            finish_times[pid] = current_time
        else:
            # Re-queue the process
            queue.append(proc)

    results = []
    for p in procs:
        pid = p["pid"]
        finish = finish_times[pid]
        tat = finish - p["arrival_time"]
        wt = tat - p["burst_time"]
        results.append({
            "pid": pid,
            "arrival_time": p["arrival_time"],
            "burst_time": p["burst_time"],
            "quantum": quantum,
            "start_time": start_times.get(pid, p["arrival_time"]),
            "finish_time": finish,
            "turnaround_time": tat,
            "waiting_time": wt,
        })

    return results


def print_results(results, quantum):
    print(f"\n===== Round Robin Scheduling (Quantum = {quantum}) =====")
    print(f"{'PID':<6} {'Arrival':<10} {'Burst':<8} {'Start':<8} {'Finish':<9} {'TAT':<7} {'WT':<6}")
    print("-" * 56)
    for r in sorted(results, key=lambda x: x["arrival_time"]):
        print(f"{r['pid']:<6} {r['arrival_time']:<10} {r['burst_time']:<8} "
              f"{r['start_time']:<8} {r['finish_time']:<9} "
              f"{r['turnaround_time']:<7} {r['waiting_time']:<6}")

    avg_tat = sum(r["turnaround_time"] for r in results) / len(results)
    avg_wt = sum(r["waiting_time"] for r in results) / len(results)
    print("-" * 56)
    print(f"Average Turnaround Time : {avg_tat:.2f}")
    print(f"Average Waiting Time    : {avg_wt:.2f}")
