import numpy as np
import random
from collections import defaultdict
from src.racetrack import RaceTrack

class MonteCarloControl:
    """
    Monte Carlo Control with Weighted Importance Sampling for off-policy learning.
    
    This class implements the off-policy every-visit Monte Carlo Control algorithm
    using weighted importance sampling to estimate the optimal policy for a given
    environment.
    """
    def __init__(self, env: RaceTrack, gamma: float = 1.0, epsilon: float = 0.1, Q0: float = 0.0, max_episode_size : int = 1000):
        """
        Initialize the Monte Carlo Control object.

        Q, C, and policies are defaultdicts that have keys representing environment states.  
        Defaultdicts (search up the docs!) allow you to set a sensible default value 
        for the case of Q[new state never visited before] (and likewise with C/policies).  
        

        Hints: 
        - Q/C/*_policy should be defaultdicts where the key is the state
        - each value in the dict is a numpy vector where position is indexed by action
        - That is, these variables are setup like Q[state][action]
        - state key will be the numpy state vector cast to string (dicts require hashable keys)
        - Q should default to Q0, C should default to 0
        - *_policy should default to equiprobable (random uniform) actions
        - store everything as a class attribute:
            - self.env, self.gamma, self.Q, etc...

        Args:
            env (racetrack): The environment in which the agent operates.
            gamma (float): The discount factor.
            Q0 (float): the initial Q values for all states (e.g. optimistic initialization)
            max_episode_size (int): cutoff to prevent running forever during MC
        
        Returns: none, stores data as class attributes
        """
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = defaultdict(lambda: np.zeros(env.n_actions)+Q0)
        self.C = defaultdict(lambda: np.zeros(env.n_actions))
        self.target_policy = defaultdict(lambda: np.ones(env.n_actions)/env.n_actions) # random uniform default
        self.behavior_policy = defaultdict(lambda: np.ones(env.n_actions)/env.n_actions) # random uniform default
        self.max_episode_size = max_episode_size


    def create_target_greedy_policy(self):
        """
        Loop through all states in the self.Q dictionary. 
        1. determine the greedy policy for that state
        2. create a probability vector that is all 0s except for the greedy action where it is 1
        3. store that probability vector in self.target_policy[state]

        Args: none
        Returns: none, stores new policy in self.target_policy
        """
        for state in self.Q.keys():
            action = np.argmax(self.Q[state])
            prob = np.zeros(self.env.n_actions)
            prob[action] = 1.0
            self.target_policy[state] = prob

    def create_behavior_egreedy_policy(self):
        """
        Loop through all states in the self.target_policy dictionary. 
        Using that greedy probability vector, and self.epsilon, 
        calculate the epsilon greedy behavior probability vector and store it in self.behavior_policy[state]
        
        Args: none
        Returns: none
        """
        for state, prob in self.target_policy.items():
            soft = prob.copy()
            for index, element in enumerate(soft):
                assert element in [0.0, 1.0]
                if element == 0.0:
                    soft[index] = 1/self.env.n_actions * self.epsilon
                else:
                    soft[index] = 1/self.env.n_actions * self.epsilon + (1. - self.epsilon)
                
            self.behavior_policy[state] = soft
        
    def egreedy_selection(self, state):
        """
        Select an action proportional to the probabilities of epsilon-greedy encoded in self.behavior_policy
        HINT: check out https://www.w3schools.com/python/ref_random_choices.asp

        Args: state (string): the current state in which to choose an action
        Returns: action (int): an action index between 0 and self.env.n_actions
        """
        probs = self.behavior_policy[state]
        actions = [n for n in range(self.env.n_actions)]
        return random.choices(actions, weights=probs)[0]

    def generate_egreedy_episode(self):
        """
        Generate an episode using the epsilon-greedy behavior policy. Will not go longer than self.max_episode_size
        
        Returns:
            list: The generated episode, which is a list of (state, action, reward) tuples.
        """
        # setup
        episode = []
        self.env.reset()                        # reset to the beginning of a race
        self.create_target_greedy_policy()      # take current Q, make target policy
        self.create_behavior_egreedy_policy()   # take current target policy, make behavior policy
        
        # start the race
        while len(episode)<self.max_episode_size:
            state = self.env.get_state()
            statekey = str(state) # dictionary needs a hashable key, won't work with the numpy array
            action = self.egreedy_selection(statekey) 
            reward = self.env.take_action( action )

            episode.append((state, action, reward))

            if self.env.is_terminal_state():
                break

        return episode
    
    def generate_greedy_episode(self):
        """
        Generate an episode using the greedy target policy. Will not go longer than self.max_episode_size
        Note: this function is not used during learning, its only for evaluating the target policy
        
        Returns:
            list: The generated episode, which is a list of (state, action, reward) tuples.
        """
        # setup
        episode = []
        self.env.reset()                        # reset to the beginning of a race
        pi = self.get_greedy_policy()
        
        # start the race
        while len(episode)<self.max_episode_size:
            state = self.env.get_state()
            statekey = str(state) # dictionary needs a hashable key, won't work with the numpy array
            
            if statekey in pi:
                action = (int)(pi[statekey]) # cast necessary because it comes out as np.int64 which breaks downstream code 
            else:
                action = random.choice(range(self.env.n_actions))
            
            reward = self.env.take_action( action )

            episode.append((state, action, reward))

            if self.env.is_terminal_state():
                break

        return episode
    
    def update_offpolicy(self, episode):
        """
        Update the Q-values using every visit weighted importance sampling. 
        See Figure 5.9, p. 134 of Sutton and Barto 2nd ed.
        
        Args: episode (list): An episode generated by the behavior policy; a list of (state, action, reward) tuples.
        Returns: none
        """
        G = 0
        W = 1.0
        for t in reversed(range(len(episode))):
            state, action, reward = episode[t]
            statekey = str(state) # dictionary needs a hashable key, won't work with the numpy array
            G = self.gamma * G + reward
            self.C[statekey][action] += W
            self.Q[statekey][action] += (W / self.C[statekey][action]) * (G - self.Q[statekey][action])
            W *= self.target_policy[statekey][action] / self.behavior_policy[statekey][action]
            if W==0.0:
                break

    
    def update_onpolicy(self, episode):
        """
        Update the Q-values using first visit epsilon-greedy. 
        See Figure 5.6, p. 127 of Sutton and Barto 2nd ed.
        
        Args: episode (list): An episode generated by the behavior policy; a list of (state, action, reward) tuples.
        Returns: none
        """
        G = 0
        W = 1.0
        visited={}

        for t in range(len(episode)):
            state, action, reward = episode[t]
            statekey = str(state) # dictionary needs a hashable key, won't work with the numpy array
            visitkey = str(state) + str(action)

            G = self.gamma * G + reward

            if visitkey not in visited.keys():
                self.C[statekey][action] += W
                self.Q[statekey][action] += (W / self.C[statekey][action]) * (G - self.Q[statekey][action])
                visited[visitkey] = True


    def train_offpolicy(self, num_episodes):
        """
        Train the agent over a specified number of episodes.
        
        Args:
            num_episodes (int): The number of episodes to train the agent.
        """
        for _ in range(num_episodes):
            episode = self.generate_egreedy_episode()
            self.update_offpolicy(episode)

   


    def get_greedy_policy(self):
        """
        Retrieve the learned target policy.
        
        Returns:
            dict: The learned target policy.
        """
        policy = {}
        for state, actions in self.Q.items():
            policy[state] = np.argmax(actions)
        return policy