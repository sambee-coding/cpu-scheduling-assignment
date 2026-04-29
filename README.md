# CPU Scheduling & Deadlock Avoidance Simulator

A professional, integrated Python simulation tool for exploring Operating System algorithms, including various CPU scheduling policies and the Banker's Algorithm for deadlock avoidance.

## 🚀 Features

### 1. CPU Scheduling Algorithms
The simulator implements the following scheduling policies with full Gantt chart visualization and performance metrics (Wait Time, Turnaround Time):
- **FCFS** (First Come First Served)
- **SJF** (Shortest Job First - Non-preemptive)
- **SRTF** (Shortest Remaining Time First - Preemptive)
- **Round Robin** (Time Quantum based)

### 2. Deadlock Avoidance
- **Banker's Algorithm**: Determines system safety and finds safe execution sequences based on resource allocation, maximum demand, and available resources.

## 📂 Project Structure
```text
src/
├── main.py          # Integrated simulation entry point
├── models.py        # Shared data structures (Process class)
├── fcfs.py          # FCFS implementation
├── sjf.py           # SJF implementation
├── srtf.py          # SRTF implementation
├── round_robin.py   # Round Robin implementation
└── bankers.py       # Banker's Algorithm implementation
```

## 🛠️ Usage

### Prerequisites
- Python 3.x

### Running the Simulator
To run the full integrated simulation suite, execute:
```bash
python src/main.py
```

## 📊 Sample Output
The simulator provides:
- Formatted tables showing Arrival, Burst, Completion, TAT, and Wait times for each process.
- Visual Gantt Charts representing the CPU execution timeline.
- Average Wait Time and Turnaround Time calculations.
- Safe Sequence identification for the Banker's Algorithm.

---
*Developed as part of the OS Algorithms Project.*