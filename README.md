# 🧩 8 Puzzle Game with A* Solver

## 📌 Overview

This project implements the classic **8 Puzzle Game** using Python with a graphical user interface.
The game consists of a **3×3 grid** with numbered tiles from **1 to 8** and one empty space. The player can slide tiles into the empty space to rearrange them and reach the correct order.

In addition to manual gameplay, the system includes an **automatic solver** that uses the **A* (A-Star) search algorithm** with the **Manhattan Distance heuristic** to find the optimal solution efficiently.

---

## 🎯 Project Features

* Interactive **GUI built with Tkinter**
* Ability to **move tiles by clicking**
* **Shuffle** the puzzle randomly
* **Reset** the board to the goal state
* **Automatic solving** of the puzzle using A* algorithm
* Visualization of the solution step-by-step

---

## 🧠 Algorithm Used

The project uses the **A* Search Algorithm**, a widely used pathfinding and graph traversal algorithm in Artificial Intelligence.

### Heuristic Function

The solver uses **Manhattan Distance** to estimate how far each tile is from its goal position.

**Formula:**

```
h(n) = |x1 - x2| + |y1 - y2|
```

Where:

* `(x1, y1)` = current position of the tile
* `(x2, y2)` = goal position of the tile

---

## 🖥️ Technologies Used

* **Python**
* **Tkinter** (for GUI)
* **Heap Queue (heapq)** for priority queue
* **A* Algorithm**
* **Manhattan Distance Heuristic**

---

## 🎮 How to Run the Project

1. Make sure Python is installed on your computer.
2. Clone the repository:

```
git clone https://github.com/your-username/8-puzzle-game.git
```

3. Navigate to the project folder:

```
cd 8-puzzle-game
```

4. Run the game:

```
python puzzle.py
```

---

## 🎮 Game Controls

| Button  | Function                              |
| ------- | ------------------------------------- |
| Shuffle | Randomizes the puzzle                 |
| Reset   | Returns the board to the solved state |
| Solve   | Automatically solves the puzzle       |

You can also **click on tiles next to the empty space** to move them.

---

## 📷 Screenshots

Add screenshots of the game interface here.

Example:

```
images/game-start.png
images/game-solved.png
```

---

## 📚 Educational Purpose

This project demonstrates how **Artificial Intelligence search algorithms** can be applied to solve classical problems such as the **8 Puzzle Problem**.

It is useful for learning:

* Search algorithms
* Heuristic functions
* Problem solving in AI
* GUI development in Python

---

## 👩‍💻 Author

**Kholod Khaled**
Computer Science Student
