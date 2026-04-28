"""
Main entry point for the CPU Scheduling & Banker's Algorithm Assignment.
Runs all algorithms on sample data and prints results.
"""

import sys
import os

# Make sure src/ modules are importable when running from project root
sys.path.insert(0, os.path.dirname(__file__))

import fcfs
import sjf
import srtf
import round_robin
import bankers


# ─────────────────────────────────────────────
# Sample Processes for Scheduling Algorithms
# ─────────────────────────────────────────────
PROCESSES = [
    {"pid": "P1", "arrival_time": 0, "burst_time": 8},
    {"pid": "P2", "arrival_time": 1, "burst_time": 4},
    {"pid": "P3", "arrival_time": 2, "burst_time": 9},
    {"pid": "P4", "arrival_time": 3, "burst_time": 5},
]

QUANTUM = 3  # Time quantum for Round Robin


# ─────────────────────────────────────────────
# Sample Data for Banker's Algorithm
# ─────────────────────────────────────────────
NUM_PROCESSES = 5
NUM_RESOURCES = 3

ALLOCATION = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]

MAX_NEED = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
]

AVAILABLE = [3, 3, 2]


def run_scheduling_algorithms():
    print("=" * 60)
    print("       CPU SCHEDULING ALGORITHMS")
    print("=" * 60)
    print(f"\nProcesses: {[p['pid'] for p in PROCESSES]}")

    # FCFS
    fcfs_results = fcfs.fcfs(PROCESSES)
    fcfs.print_results(fcfs_results)

    # SJF
    sjf_results = sjf.sjf(PROCESSES)
    sjf.print_results(sjf_results)

    # SRTF
    srtf_results = srtf.srtf(PROCESSES)
    srtf.print_results(srtf_results)

    # Round Robin
    rr_results = round_robin.round_robin(PROCESSES, QUANTUM)
    round_robin.print_results(rr_results, QUANTUM)


def run_bankers_algorithm():
    print("\n" + "=" * 60)
    print("         BANKER'S ALGORITHM")
    print("=" * 60)

    result = bankers.bankers_algorithm(
        NUM_PROCESSES, NUM_RESOURCES,
        ALLOCATION, MAX_NEED, AVAILABLE
    )
    bankers.print_results(
        NUM_PROCESSES, NUM_RESOURCES,
        ALLOCATION, MAX_NEED, AVAILABLE,
        result
    )

    # Example: P1 requests [1, 0, 2]
    print("\n--- Resource Request Test ---")
    req_pid = 1
    request = [1, 0, 2]
    print(f"P{req_pid} requests: {request}")
    req_result = bankers.request_resources(
        req_pid, request,
        ALLOCATION, MAX_NEED, AVAILABLE,
        NUM_RESOURCES
    )
    print(f"Result: {req_result['message']}")


if __name__ == "__main__":
    run_scheduling_algorithms()
    run_bankers_algorithm()
