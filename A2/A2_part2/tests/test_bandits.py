import unittest
from src.bandits import update, greedy, egreedy, empirical_egreedy
import numpy as np
import pandas as pd


class TestBandits(unittest.TestCase):

    # Tests for update(q, r, k)
    def test_update_zero_q(self):
        self.assertAlmostEqual(update(0.0, 5.0, 0), 5.0)

    def test_update_nonzero_q(self):
        # q=2.0, r=4.0, k=1 => new_q=2.0 + 1/2*(4.0-2.0)=3.0
        self.assertAlmostEqual(update(2.0, 4.0, 1), 3.0)

    def test_update_negative_reward(self):
        # q=1.0, r=-1.0, k=2 => new_q=1.0 + 1/3*(-1.0-1.0)=1.0 + 1/3*(-2.0)=1.0 - 0.666...
        self.assertAlmostEqual(update(1.0, -1.0, 2), 1.0 - 2.0/3.0, places=4)

    # Tests for greedy(q_estimate)
    def test_greedy_single_action(self):
        self.assertEqual(greedy(np.array([10])), 0)

    def test_greedy_multiple_actions(self):
        arr = np.array([1, 3, 5, 7, 6])
        self.assertEqual(greedy(arr), 3)  # index of largest value (7)

    def test_greedy_tie(self):
        arr = np.array([5, 5, 3])
        # np.argmax returns first occurrence of max
        self.assertEqual(greedy(arr), 0)

    # Tests for egreedy(q_estimate, epsilon)
    def test_egreedy_zero_epsilon(self):
        arr = np.array([0.2, 0.5, 0.1])
        # With epsilon=0, always pick greedy (index of 0.5 => 1)
        self.assertEqual(egreedy(arr, 0.0), 1)

    def test_egreedy_full_epsilon(self):
        arr = np.array([0.2, 0.5, 0.1])
        # With epsilon=1, choose random action
        # We just check that it is a valid index
        choice = egreedy(arr, 1.0)
        self.assertIn(choice, [0, 1, 2])

    def test_egreedy_partial_epsilon(self):
        arr = np.array([10, 0, 0])
        # With epsilon=0.5, we can get either 0 or random among [1,2]
        choice = egreedy(arr, 0.5)
        self.assertIn(choice, [0, 1, 2])

    # Tests for empirical_egreedy(epsilon, n_trials, n_arms, n_plays)
    def test_empirical_egreedy_return_type(self):
        rewards = empirical_egreedy(0.1, 2, 3, 5)
        self.assertIsInstance(rewards, list)
        self.assertEqual(len(rewards), 2, "rewards should have 5 trails")
        self.assertEqual(len(rewards[0]), 5, "each trails should have 3 runs")

    def test_empirical_egreedy_dimensions(self):
        n_trials, n_plays = 2, 5
        rewards = empirical_egreedy(0.1, n_trials, 3, n_plays)
        self.assertEqual(len(rewards[0]) * len(rewards), n_trials * n_plays)

    def test_empirical_egreedy_vary_epsilon(self):
        df1 = empirical_egreedy(0.0, 2, 3, 5)
        df2 = empirical_egreedy(1.0, 2, 3, 5)
        # Just check we can run both extremes of epsilon without error
        self.assertEqual(len(df1), len(df2))

if __name__ == '__main__':
    unittest.main()
