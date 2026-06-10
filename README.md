# Python Data Structures and Algorithms

This repository is a study collection for data structures and algorithms in Python. It contains sample code, exercises, lecture materials, and reference documents for topics such as linked lists, stacks, queues, trees, heaps, hashing, sorting, graphs, and shortest path algorithms.

The goal of the repo is to gather examples for reviewing core concepts such as linked lists, stacks, queues, trees, heaps, hashing, sorting, graphs, and shortest path, along with basic OOP examples used in class and exam practice.

## Overview

- Basic data structures such as Stack, Queue, and Singly Linked List
- Object-oriented programming concepts such as encapsulation, inheritance, overriding, static members, and properties
- Sample code used in the Data Structures & Algorithms course
- Lecture PDFs and images used as teaching materials
- Files that contain multiple experimental versions of the same topic, with older examples often kept in comments

## Folder Structure

```text
python-data-structures-and-algorithms/
├── Exams/
│   ├── BasicQueue.py
│   ├── BasicSinglyLinkedList.py
│   ├── BasicStack.py
│   ├── Lecture 2.py
│   ├── LinkedList.py
│   ├── PythonOop.py
│   ├── Queue.py
│   └── Student.py
└── Lectures/
    ├── 0Exercises/
    ├── Assignment 1 Linked List/
    ├── Assignment 2 Construct Binary Tree/
    ├── Assignment 3 Binary Heap/
    ├── Assignment 4 Shortest Path/
    ├── Lecture 1 Introduction/
    ├── Lecture 2 Review Python/
    ├── Lecture 3 Linked List/
    ├── Lecture 4 Stack/
    ├── Lecture 5 Tree/
    ├── Lecture 5.1 Binary Search Tree/
    ├── Lecture 5.2 Binary Search Tree Remove/
    ├── Lecture 7 Hashing/
    ├── Lecture 8 Priority Queue (Heap)/
    ├── Lecture 8.1 Priority Queue (Insert and deleteMin)/
    ├── Lecture 9 Sorting/
    ├── Lecture 10 Graph/
    ├── Lecture 11 Shortest path/
    ├── Data Structures & Algorithms in Python.pdf
    └── planstd060243106.pdf
```

## Main Folders

### `Exams/`

This folder contains short examples used for exams, practice, or quick demonstrations.

- `BasicStack.py` example of a stack implemented with a Python list
- `BasicQueue.py` basic queue example
- `BasicSinglyLinkedList.py` example of a singly linked list
- `LinkedList.py` multiple experimental versions of linked list code
- `Queue.py` another queue example with front/rear and size control
- `PythonOop.py` OOP examples such as encapsulation, property, static variable, inheritance, and overriding
- `Student.py` student class with properties and grade conversion methods
- `Lecture 2.py` basic lecture example such as the `Point` class

### `Lectures/`

This folder stores lecture and assignment materials organized by topic.

- Introduction and Python review
- Linked List, Stack, Tree, and Binary Search Tree
- Hashing and Priority Queue / Heap
- Sorting, Graph, and Shortest Path
- Exercises and assignments for each topic

Some folders may contain code files, PDFs, or supporting images to use alongside slides and lecture notes.

## How to Run Examples

Quick start:

1. Install Python 3.x
2. Open a terminal at the repository root
3. Run any example with `python`

This project does not use a complex framework or external dependencies. You can run it with standard Python.

1. Install Python 3.x
2. Open a terminal at the repository root
3. Run the file you want with the `python` command

Examples:

```bash
python Exams/BasicStack.py
python Exams/BasicQueue.py
python Exams/Student.py
```

On Windows, quote paths that contain spaces.

```bash
python "Exams/PythonOop.py"
```

## Notes Before Reading the Code

- Some files contain multiple versions of the same idea in one file, with older versions commented out.
- Many examples are written for teaching, so they may emphasize clarity over production-ready completeness.
- Some examples use slightly different method names or naming styles to reflect the course progression.
- PDF and image files are supporting documents, not executable code.

## How to Use This Repo

You can use this repository in several ways:

- Read it as a study summary before exams
- Run each example file to see output and data flow
- Modify the code to experiment with how each data structure behaves
- Use the files in `Lectures/` as references when doing assignments or writing your own notes

## Notes on the Example Code

The code in this repository is educational, so it may include the following:

- Some methods use simplified return or display behavior
- Some examples may not handle every edge case
- Some classes are experimental versions used to compare multiple implementation styles

If you want to reuse the code in another project, you should review validation, error handling, and performance.

## Suggested Next Steps

If you continue developing this repo, you can add:

- A README in each lecture folder with more detailed explanations
- A `requirements.txt` file if external dependencies are added later
- Tests for Stack, Queue, and LinkedList behavior
- Cleaner reference versions of the teaching code for comparison

## License

No license is currently specified in this repository. If you plan to publish or share it publicly, add a clear license first.