"""
Shortest Job First (SJF) CPU Scheduling Algorithm
Non-preemptive: once a process starts, it runs to completion.
Among ready processes, the one with the shortest burst time is selected.
"""

def sjf(processes):
    """
    Runs SJF (non-preemptive) scheduling.

    Args:
        processes: list of dicts with keys:
            - pid, arrival_time, burst_time

    Returns:
        list of dicts with scheduling results.
    """
    procs = [p.copy() for p in processes]
    n = len(procs)
    completed = []
    current_time = 0
    done = [False] * n

    while len(completed) < n:
        # Find all processes that have arrived and are not done
        ready = [
            procs[i] for i in range(n)
            if not done[i] and procs[i]["arrival_time"] <= current_time
        ]

        if not ready:
            # CPU idle — jump to next arrival
            next_arrival = min(
                procs[i]["arrival_time"] for i in range(n) if not done[i]
            )
            current_time = next_arrival
            continue

        # Pick the process with the shortest burst time (ties broken by arrival)
        selected = min(ready, key=lambda p: (p["burst_time"], p["arrival_time"]))
        idx = next(i for i in range(n) if procs[i]["pid"] == selected["pid"] and not done[i])

        start_time = current_time
        finish_time = current_time + selected["burst_time"]
        turnaround_time = finish_time - selected["arrival_time"]
        waiting_time = turnaround_time - selected["burst_time"]

        completed.append({
            "pid": selected["pid"],
            "arrival_time": selected["arrival_time"],
            "burst_time": selected["burst_time"],
            "start_time": start_time,
            "finish_time": finish_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time,
        })

        done[idx] = True
        current_time = finish_time

    return completed


def print_results(results):
    print("\n===== SJF Scheduling (Non-Preemptive) =====")
    print(f"{'PID':<6} {'Arrival':<10} {'Burst':<8} {'Start':<8} {'Finish':<9} {'TAT':<7} {'WT':<6}")
    print("-" * 56)
    for r in sorted(results, key=lambda x: x["start_time"]):
        print(f"{r['pid']:<6} {r['arrival_time']:<10} {r['burst_time']:<8} "
              f"{r['start_time']:<8} {r['finish_time']:<9} "
              f"{r['turnaround_time']:<7} {r['waiting_time']:<6}")

    avg_tat = sum(r["turnaround_time"] for r in results) / len(results)
    avg_wt = sum(r["waiting_time"] for r in results) / len(results)
    print("-" * 56)
    print(f"Average Turnaround Time : {avg_tat:.2f}")
    print(f"Average Waiting Time    : {avg_wt:.2f}")
