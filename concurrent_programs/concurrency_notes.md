# 🧠 Concurrency

> **Concurrency = doing multiple things at the same time (or appearing to).**  
> Goal: **better CPU usage, less waiting, faster programs**.

---

## 1️⃣ Why Concurrency Exists (Reality Check)

### ❌ Sequential programs are dumbly slow

Task A → Task B → Task C → Done
````

Problems:

* Uses **only one CPU core**
* Wastes time **waiting for I/O** (network, disk, DB)
* Modern CPUs have **multiple cores** sitting idle

### ✅ Concurrency fixes this

```text
Task A ┐
Task B ├→ Done faster
Task C ┘
```

---

## 2️⃣ CPU-bound vs I/O-bound (CRITICAL DISTINCTION)

### CPU-bound

* Heavy calculations
* Math, compression, ML, cryptography
* **Needs more CPU cores**

### I/O-bound

* Waiting for network, disk, DB, APIs
* CPU mostly idle
* **Needs better scheduling**

> **This distinction decides which concurrency model to use.**

---

## 3️⃣ Multiprocessing 🧩 (True Parallelism)

### What it is

* Multiple **processes**
* Each process has:

  * Its **own memory**
  * Its **own Python interpreter**
  * Runs on **different CPU cores**

### Mental Model

```text
CPU Core 1 → Process A
CPU Core 2 → Process B
CPU Core 3 → Process C
CPU Core 4 → Process D
```

### Characteristics

* ✅ True parallel execution
* ❌ Heavy memory usage
* ❌ Inter-process communication is slow
* ❌ Process creation is expensive

### When to use

✔ CPU-bound work
✔ Data processing
✔ ML training
✔ Image/video processing

### Python example (conceptual)

```python
from multiprocessing import Process

def work():
    print("Heavy computation")

p1 = Process(target=work)
p2 = Process(target=work)

p1.start()
p2.start()
```

### Brutal truth

> Multiprocessing is **powerful but expensive**.
> Use only when CPU is your bottleneck.

---

## 4️⃣ Multithreading 🧵 (Illusion of Parallelism in Python)

### What it is

* Multiple **threads** inside one process
* **Shared memory**
* Lightweight compared to processes

### Mental Model

```text
Process
 ├─ Thread 1 (shared memory)
 ├─ Thread 2 (shared memory)
 └─ Thread 3 (shared memory)
```

### Python’s ugly truth: **GIL**

* **Global Interpreter Lock**
* Only **ONE thread executes Python bytecode at a time**

```text
Thread A ─┐
Thread B ─┼─ GIL ─ CPU
Thread C ─┘
```

### So why threads exist at all?

Because while one thread is **waiting for I/O**, another can run.

### When threading works

✔ I/O-bound tasks
✔ Network calls
✔ DB queries
✔ File operations

### When threading FAILS

❌ CPU-bound work (GIL kills parallelism)

### Example

```python
import threading

def fetch_data():
    print("Waiting for API")

t1 = threading.Thread(target=fetch_data)
t2 = threading.Thread(target=fetch_data)

t1.start()
t2.start()
```

### Danger zone

* Race conditions
* Deadlocks
* Shared state bugs

> Threads are **easy to start** and **hard to debug**.

---

## 5️⃣ Asynchronous Programming ⚡ (Smart Waiting)

### What async actually means

> **Single thread, single process, multiple tasks cooperatively sharing time**

No parallel execution.
Just **non-blocking waiting**.

### Mental Model

```text
Event Loop
 ├─ Task A (waiting for network)
 ├─ Task B (runs)
 ├─ Task C (waiting for DB)
```

### Key idea

> Don’t block.
> **Yield control when waiting.**

### ASCII Diagram

```text
┌─────────────┐
│ Event Loop  │
└─────┬───────┘
      │
  ┌───▼───┐   ┌───▼───┐
  │ Task1 │   │ Task2 │
  └───┬───┘   └───┬───┘
      │ await     │ await
      └──────┬───┘
             ▼
         Network / DB
```

### Example

```python
import asyncio

async def fetch():
    await asyncio.sleep(1)
    print("Fetched")

async def main():
    await asyncio.gather(fetch(), fetch(), fetch())

asyncio.run(main())
```

### Why async is powerful

* Handles **thousands of connections**
* Minimal memory
* No thread locks
* Perfect for servers

### When async SUCKS

❌ CPU-heavy tasks
❌ Blocking libraries
❌ Complex logic (callback hell if abused)

---

## 6️⃣ Comparison Table (Memorize This)

| Model           | Parallel?  | Best For    | Bad For     |
| --------------- | ---------- | ----------- | ----------- |
| Multiprocessing | ✅ Yes      | CPU-bound   | Memory, IPC |
| Multithreading  | ⚠️ Limited | I/O-bound   | CPU-bound   |
| Async           | ❌ No       | Massive I/O | CPU work    |

---

## 7️⃣ Web Server Example (FastAPI Mental Model)

### Bad (Blocking)

```text
Request → DB wait → Response
(others wait)
```

### Threaded

```text
Req1 ─┐
Req2 ─┼─ Threads
Req3 ─┘
```

### Async (Best)

```text
Req1 (waiting)
Req2 (running)
Req3 (waiting)
```

> This is why **FastAPI + async** scales insanely well.

---

## 8️⃣ Common Fallacies (Critical Thinking)

### ❌ “Async is faster”

Wrong.
Async is **less wasteful**, not faster at computation.

### ❌ “Threads use multiple cores”

In Python? Mostly **NO**.

### ❌ “Multiprocessing is always better”

No.
IPC + memory overhead can make it slower.

---

## 9️⃣ Decision Rule (Tattoo This)

```text
Is it CPU heavy?
  → Multiprocessing

Is it I/O heavy but simple?
  → Threading

Is it I/O heavy and scalable?
  → Async
```

---

## 10️⃣ Summary

* **Concurrency ≠ Parallelism**
* Python threads are **fake parallel**
* Async is **about waiting smartly**
* Multiprocessing is **real power, real cost**
* Choosing wrong model = wasted performance

---

