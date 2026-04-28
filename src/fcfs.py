def fcfs(processes):
    sorted_procs = sorted(processes, key=lambda p: p["arrival_time"])

    current_time = 0
    results = []

    for proc in sorted_procs:
        if current_time < proc["arrival_time"]:
            current_time = proc["arrival_time"]

        start_time = current_time
        finish_time = current_time + proc["burst_time"]
        turnaround_time = finish_time - proc["arrival_time"]
        waiting_time = turnaround_time - proc["burst_time"]

        results.append({
            "pid": proc["pid"],
            "arrival_time": proc["arrival_time"],
            "burst_time": proc["burst_time"],
            "start_time": start_time,
            "finish_time": finish_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time,
        })

        current_time = finish_time

    avg_tat = sum(r["turnaround_time"] for r in results) / len(results)
    avg_wt = sum(r["waiting_time"] for r in results) / len(results)

    return results, avg_wt, avg_tat