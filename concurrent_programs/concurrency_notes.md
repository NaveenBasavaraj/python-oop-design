

---


````md
# 🧠 Concurrency

**Concurrency = doing multiple things at the same time (or appearing to).**

**Goal:** better CPU usage, less waiting, faster programs.

---

## 1️⃣ Why Concurrency Exists (Reality Check)

### ❌ Sequential programs are dumbly slow

```text
Task A → Task B → Task C → Done
````

**Problems:**

* Uses only **one CPU core**
* Wastes time waiting for **I/O** (network, disk, DB)
* Modern CPUs have **multiple cores sitting idle**

---

### ✅ Concurrency helps

```text
Task A ┐
Task B ├──> Done faster
Task C ┘
```

---

## 2️⃣ CPU-bound vs I/O-bound (CRITICAL)

### CPU-bound

* Heavy computation
* Math, compression, ML
* CPU is the bottleneck

```text
CPU 100% busy
```

### I/O-bound

* Network calls, DB queries, disk
* CPU mostly idle, waiting

```text
CPU idle → waiting for response
```

> **This distinction decides the concurrency model.**

---

## 3️⃣ Multiprocessing (True Parallelism)

### What it is

* Multiple **processes**
* Each process:

  * Own memory
  * Own Python interpreter
  * Runs on a **separate CPU core**

```text
Core 1 → Process A
Core 2 → Process B
Core 3 → Process C
Core 4 → Process D
```

### Use when

* CPU-bound tasks
* Heavy computation

### Downsides

* High memory usage
* Slow inter-process communication

---

## 4️⃣ Multithreading (Fake Parallelism in Python)

### What it is

* Multiple threads in **one process**
* Shared memory

```text
Process
 ├─ Thread 1
 ├─ Thread 2
 └─ Thread 3
```

### The GIL problem

Only **one thread executes Python bytecode at a time**.

```text
Thread A ─┐
Thread B ─┼─ GIL ─ CPU
Thread C ─┘
```

### Works well for

* I/O-bound tasks
* Network, DB, file operations

### Fails for

* CPU-heavy work

---

## 5️⃣ Asynchronous Programming (Smart Waiting)

### Key idea

> Don’t block. Yield control while waiting.

```text
Event Loop
 ├─ Task A (waiting for network)
 ├─ Task B (running)
 └─ Task C (waiting for DB)
```

### Visual flow

```text
Task → await → I/O
     ← resume ←
```

### Strengths

* Handles thousands of connections
* Low memory
* Perfect for web servers

### Weaknesses

* Bad for CPU-heavy work
* Blocking code ruins everything

---

## 6️⃣ Comparison Table

| Model           | True Parallel | Best For    | Bad For     |
| --------------- | ------------- | ----------- | ----------- |
| Multiprocessing | ✅             | CPU-bound   | Memory      |
| Multithreading  | ❌             | I/O-bound   | CPU work    |
| Async           | ❌             | Massive I/O | Computation |

---

## 7️⃣ One Rule to Remember

```text
CPU-heavy?        → Multiprocessing
I/O-heavy?        → Async
Simple I/O tasks? → Threading
```

---

## 8️⃣ Brutal Truths

* Concurrency ≠ parallelism
* Async is not “faster” — it’s **less wasteful**
* Python threads don’t bypass the GIL
* Wrong model = fake performance gains

```

---

```
