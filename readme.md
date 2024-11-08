Vacuum
======

This lab provides the opportunity to create an autonomous agent to vacuum virtual houses.

![A robotic vacuum cleaner cleaning a carpet (Stable Diffusion)](media/vacuum.jpg)

Learning Objectives
-------------------

After completing this lab, students will be able to:

1. Use dictionaries for accessing structured data
2. Implement turn-based agents

Task
----

Your task is to implement the vacuuming agent such that it is able to successfully vacuum at least houses 0 through 5. Additional houses are provided for an extra challenge and to better measure agent performance in complex environments.

Warning 🔥: The vacuum hardware is somewhat limited and is unable to run continuously without overheating. There is a sensor to monitor the current `temp`. Make sure that you `rest` occasionally to prevent the device from catching fire.


Handout code [vacuum.py](vacuum.py) is provided and must be used as a starting point for this assignment. Your task is to provide an implementation for the `agent` function.

No code outside of the agent function should be modified in your final submission.

Houses
------

Houses are represented as plain text. The `*` character is used to represent a wall, the `.` is used to represent dirt, and a blank space is used to represent clean floor. Once clean, all dirt (`.`) should be removed from a house. Here's an example showing what house 4 looks like:

```
*********
*...*...*
*...*...*
**.**...*
*.......*
*********
```

Percepts and Actions
--------------------

![Agent environment diagram](https://upload.wikimedia.org/wikipedia/commons/3/3f/IntelligentAgent-SimpleReflex.png)

The vacuum `agent` processes data from sensors as `percepts` and uses this sensor data to select a valid `action`. The environment then updates based on the `action` and new `percepts` are returned from sensors so the agent can make its next decision.

Turns
-----

The `agent` function is called once per turn with the current percepts, state, and history of actions. It returns the `action` to be taken on the next turn.

Resources
---------

- [PY4E Chapters 2 through 9](https://www.py4e.com/html3/)
- [Intelligent Agents on Wikipedia](https://en.wikipedia.org/wiki/Intelligent_agent)
- It is not expected that your solution to this lab will be optimal, but there is scholarly work on [online coverage algorithms](https://scholar.google.com/scholar?hl=en&q=online+coverage+algorithm) if you have interest in thinking deeply about this subject.