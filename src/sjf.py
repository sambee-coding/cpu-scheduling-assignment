def sjf(processes):
    processes = sorted(processes, key=lambda p: p["arrival_time"])
    
    current_time = 0
    ready_queue = []
    results = []

    while processes or ready_queue:
        # Add arrived processes to ready queue
        while processes and processes[0]["arrival_time"] <= current_time:
            ready_queue.append(processes.pop(0))

        # If no process is ready → CPU idle
        if not ready_queue:
            current_time = processes[0]["arrival_time"]
            continue

        # Pick process with shortest burst time
        ready_queue.sort(key=lambda p: p["burst_time"])
        proc = ready_queue.pop(0)

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

    if not results:
        return [], 0, 0

    avg_tat = sum(r["turnaround_time"] for r in results) / len(results)
    avg_wt = sum(r["waiting_time"] for r in results) / len(results)

    return results, avg_wt, avg_tat
