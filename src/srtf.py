"""
Shortest Remaining Time First (SRTF) CPU Scheduling Algorithm
Preemptive version of SJF: at every time unit, the process with the
shortest remaining burst time is selected.
"""

def srtf(processes):
    """
    Runs SRTF (preemptive SJF) scheduling.

    Args:
        processes: list of dicts with keys:
            - pid, arrival_time, burst_time

    Returns:
        list of dicts with scheduling results per process.
    """
    procs = [p.copy() for p in processes]
    n = len(procs)

    remaining = {p["pid"]: p["burst_time"] for p in procs}
    start_times = {}
    finish_times = {}

    current_time = 0
    completed = 0
    total_time = sum(p["burst_time"] for p in procs)
    end_time = max(p["arrival_time"] for p in procs) + total_time

    while completed < n:
        # Get all arrived, not-yet-finished processes
        ready = [
            p for p in procs
            if p["arrival_time"] <= current_time and remaining[p["pid"]] > 0
        ]

        if not ready:
            current_time += 1
            continue

        # Pick process with least remaining time (ties: smallest arrival, then pid)
        selected = min(ready, key=lambda p: (remaining[p["pid"]], p["arrival_time"]))
        pid = selected["pid"]

        # Record first start time
        if pid not in start_times:
            start_times[pid] = current_time

        # Execute for 1 time unit
        remaining[pid] -= 1
        current_time += 1

        # Check if process finished
        if remaining[pid] == 0:
            finish_times[pid] = current_time
            completed += 1

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
            "start_time": start_times.get(pid, p["arrival_time"]),
            "finish_time": finish,
            "turnaround_time": tat,
            "waiting_time": wt,
        })

    return results


def print_results(results):
    print("\n===== SRTF Scheduling (Preemptive SJF) =====")
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
