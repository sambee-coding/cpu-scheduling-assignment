# OS Algorithms Simulator

A modular Python implementation of core Operating Systems algorithms, including various CPU Scheduling techniques and the Banker's Algorithm for deadlock avoidance.

## Team Contribution — Group 6
- **BDU1602358** - SAMRAWIT Bitew
- **BDU1602362** - SAMRAWIT Yirga
- **BDU1602390** - SEID TILAHUN
- **BDU1602442** - SIMRET ABEBE
- **BDU1602454** - SISAY TEMESGEN
- **BDU1602459** - SIYADLE DUBALE
- **BDU1602479** - SOSINA SHEGAW
- **BDU1602482** - SUNAN ALI

## Features

### CPU Scheduling Algorithms
All scheduling algorithms are implemented in a preemptive/non-preemptive manner with visual Gantt chart outputs and detailed performance metrics (CT, TAT, WT).
- **First Come First Served (FCFS)**: Non-preemptive scheduling based on arrival time.
- **Shortest Job First (SJF)**: Non-preemptive scheduling picking the shortest burst time.
- **Shortest Remaining Time First (SRTF)**: Preemptive version of SJF.
- **Round Robin (RR)**: Preemptive scheduling with a fixed time quantum.

### Deadlock Avoidance
- **Banker's Algorithm**: Determines system safety and finds safe execution sequences for resource allocation.

## Project Structure

- `src/main.py`: The central entry point for running all simulations (Requirement 4).
- `src/fcfs.py`, `src/sjf.py`, `src/srtf.py`, `src/round_robin.py`: Individual scheduling algorithm implementations.
- `src/bankers.py`: Banker's algorithm logic (Requirement 5).

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sambee-coding/cpu-scheduling-assignment.git
   cd cpu-scheduling-assignment
   ```

2. **Run the simulator**:
   ```bash
   python src/main.py
   ```

3. **Follow the on-screen prompts** to use sample data or enter your own process details.

## Sample Output (Scheduling)
```text
PID   | Arrival  | Burst  | CT    | TAT   | WT   
--------------------------------------------------
1     | 0        | 8      | 17    | 17    | 9    
2     | 1        | 4      | 5     | 4     | 0    
...
Average Waiting Time: 6.50
Average Turnaround Time: 13.00

--- Gantt Chart ---
|  P1  |  P2  |  P4  |  P1  |  P3  |
0       1       5       10      17      26
```

---
*Developed for the Operating Systems Course Assignment (Section 4).*
