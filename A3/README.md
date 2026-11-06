# Assignment 3: Solving the Racetrack Problem using Dynamic Programming, Monte Carlo Control, and TD Learning

## Overview
You will implement **Dynamic Programming (DP)**, **Monte Carlo (MC) Control**, and **TD Learning** methods to solve the **Racetrack problem**. You will complete functions for **policy iteration, value iteration, off-policy MC control with weighted importance sampling, and on-policy TD learning (SARSA)**.

A Jupyter Notebook (`racecar.ipynb`) is provided to help you visualize the results of your implementation. You should use it to check if your policies are leading to optimal behavior.

## Instructions
### Part 1: Implementing Dynamic Programming

Complete the following functions in `src/dp.py`:

The comments in the functions provide more details on the expected behavior.

1. **Policy Evaluation (`policy_evaluation`)**
   - Iteratively update the **value function** given a fixed policy until convergence.
   - Stop when the maximum change in value function is **less than** `theta`.
   
2. **Policy Improvement (`policy_improvement`)**
   - Use the **updated value function** to improve the policy by selecting the best action.
   - Return `True` if the policy is stable (unchanged), otherwise return `False`.
   
3. **Policy Iteration (`policy_iteration`)**
   - Alternates between **policy evaluation** and **policy improvement** until convergence.
   
4. **Value Iteration (`value_iteration`)**
   - Iteratively update the **value function** by selecting the best action at each state.
   - Extract the optimal policy from the final value function.

### Part 2: Implementing Monte Carlo Control

Complete the following functions in `src/montecarlo.py`:

1. **Initializing State-Action Values (`__init__`)**
   - Store Q-values (`self.Q`), cumulative weights (`self.C`), and policies.
   - Initialize them as **default dictionaries**.
   
2. **Target Policy (`create_target_greedy_policy`)**
   - Construct a **greedy policy** based on Q-values.
   
3. **Epsilon-Greedy Policy (`create_behavior_egreedy_policy`)**
   - Convert the greedy policy into an **epsilon-greedy policy**.
   
4. **Generating an Epsilon-Greedy Episode (`generate_egreedy_episode`)**
   - Simulate an episode using the epsilon-greedy behavior policy.
   
5. **Updating Q-values (`update_offpolicy`)**
   - Use **weighted importance sampling** to update Q-values.
   - Implement according to **Sutton & Barto's Algorithm (Figure 5.9)**.

### Part 3: Implementing TD Learning (SARSA, on-policy)

Complete the following functions in `src/td.py`:

1. **SARSA episode (`run_episode`)**
   - Generate one episode using epsilon-greedy action selection, updating Q after every step with the SARSA update (using the next action actually taken, not the max).

2. **Greedy episode (`generate_greedy_episode`)**
   - Generate one episode always taking the best-known action. No exploration and no Q updates; this is only for evaluating what was learned.

### Submission

After you're done, run the Jupyter Notebook (`racecar.ipynb`) to visualize the results of your implementation.

Submit:
* `dp.py` 
* `montecarlo.py`
* `td.py` 
* `racecar.ipynb`

**Make sure to run all cells in `racecar.ipynb`, and produce all plots prior to submitting.** 

You are free to add any additional code to help you visualize the results of your implementation. But at the minimum, it should include all the plots that were provided in the starter code.

