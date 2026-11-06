import numpy as np
import random
from collections import defaultdict
from src.racetrack import RaceTrack


class TDLearning:
    """
    TD control (SARSA, on-policy) on the RaceTrack environment.
    Unlike Monte Carlo, it updates Q after every step instead of waiting for the episode to end.
    """
    def __init__(self, env: RaceTrack, gamma: float = 1.0, alpha: float = 0.1, epsilon: float = 0.1,
                 Q0: float = 0.0, max_episode_size: int = 1000):
        """
        Args:
            env: RaceTrack environment.
            gamma: discount factor.
            alpha: learning rate.
            epsilon: probability of a random action.
            Q0: initial Q value for unseen states.
            max_episode_size: cutoff so an episode can't run forever.
        """
        self.env = env
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.max_episode_size = max_episode_size
        self.Q = defaultdict(lambda: np.zeros(env.n_actions) + Q0)

    def egreedy_selection(self, statekey):
        """With probability epsilon pick a random action, otherwise the best-known one."""
        if random.random() < self.epsilon:
            return random.randrange(self.env.n_actions)
        return int(np.argmax(self.Q[statekey]))

    def run_episode(self):
        """
        Play one epsilon-greedy episode, updating Q after every step (SARSA).
 
        Hints:
        - The state key is str(self.env.get_state()).
        - Q is indexed as self.Q[statekey][action].
        - Update Q after every step, not at the end of the episode.
        - SARSA update: target = reward + gamma * Q[next state][next action], where next action
          is chosen by self.egreedy_selection() and is the same action taken on the next step.
        - Choose the first action before the loop, then carry the next action into the next step.
        - At the finish line there is no next state, so don't bootstrap: target = reward.
        - Stop at self.env.is_terminal_state() or self.max_episode_size.
        - Return (statekey, action, reward) tuples.
 
        Returns:
            list of (state, action, reward) tuples.
        """
        episode = []
        self.env.reset()
        statekey = str(self.env.get_state())

        # Your code here 

        return episode

    def generate_greedy_episode(self):
        """
        Play one episode always taking the best-known action (no learning). For evaluation comparison.
 
        Hints:
        - Don't update Q here.
        - Check `statekey in self.Q` before using Q: looking up an unseen key in a defaultdict
          silently creates it. If the state is unseen, pick a random action.
        - Stop at self.env.is_terminal_state() or self.max_episode_size.
        - Return (statekey, action, reward) tuples.
        """
        episode = []
        self.env.reset()

        # Your code here 

        return episode