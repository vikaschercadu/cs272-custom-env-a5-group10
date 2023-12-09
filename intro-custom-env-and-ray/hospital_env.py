import gymnasium as gym
from gymnasium.spaces import Discrete, Box
import numpy as np
import random

class HospitalEnv(gym.Env):
    """
    Custom environment for simulating hospital resource management in a reinforcement learning context.
    The agent needs to manage the allocation of doctors and beds to treat patients and minimize waiting times.
    """
    metadata = {'render.modes': ['console']}

    def __init__(self):
        """
        Initialization of the Hospital environment.
        """
        super(HospitalEnv, self).__init__()
        # observation space: number of patients waiting, available doctors, available beds, average waiting time, and current hour.
        self.observation_space = Box(low=np.array([0, 0, 0, 0, 0]), high=np.array([np.inf, 30, 100, np.inf, 24]), dtype=np.float32)
        self.action_space = Discrete(3)
        self.reset()

    def step(self, action):
        """
        Step function to update the environment's state based on the action taken.
        """
        if action == 1:
            self.available_doctors = min(self.available_doctors + 1, 30)
        elif action == 2:
            self.available_beds = min(self.available_beds + 5, 100)

        # Simulate patient flow, update waiting time, and calculate the reward.
        self._simulate_patient_flow()
        self.avg_waiting_time = self._calculate_avg_waiting_time()
        reward = self._calculate_reward()
        
        # An episode is done if the current hour reaches or exceeds 20 (closing time).
        done = self.current_hour >= 20
        
        # Update the state with the current values.
        self.state = np.array([self.num_patients_waiting, self.available_doctors, self.available_beds, self.avg_waiting_time, self.current_hour])
        info = self._get_metrics()
        
        return self.state, reward, done, info

    def reset(self):
        """
        Reset the environment to the initial state for a new episode.
        """
        self.num_patients_waiting = random.randint(0, 10)
        self.available_doctors = 10
        self.available_beds = 20
        self.avg_waiting_time = 0
        self.current_hour = 8

        self.state = np.array([self.num_patients_waiting, self.available_doctors, self.available_beds, self.avg_waiting_time, self.current_hour])
        return self.state

    def _simulate_patient_flow(self):
        """
        Simulate the flow of patients arriving and being treated.
        """
        patients_arrived = random.randint(0, 5)
        self.num_patients_waiting += patients_arrived
        treated_patients = min(self.num_patients_waiting, self.available_doctors)
        self.num_patients_waiting -= treated_patients
        
        # Advance the simulation by one hour.
        self.current_hour += 1

    def _calculate_avg_waiting_time(self):
        """
        Calculate the average waiting time based on the number of patients and available doctors.
        """
        # Increase waiting time based on excess patients not treated.
        waiting_factor = (self.num_patients_waiting - self.available_doctors) * 5
        return max(0, self.avg_waiting_time + waiting_factor)

    def _calculate_reward(self):
        """
        Calculate the reward from the current state of the environment.
        """
        # Negative reward for patient waiting time, positive reward for resource utilization.
        waiting_penalty = -self.avg_waiting_time
        resource_utilization_reward = self.available_doctors * 2 + self.available_beds
        return waiting_penalty + resource_utilization_reward

    def _get_metrics(self):
        """
        Gather metrics for evaluating the environment's performance.
        """
        # Metrics include the number of patients treated, waiting, and resource utilization rates.
        metrics = {
            'num_patients_treated': self.available_doctors,  # Assuming each doctor treats one patient
            'num_patients_waiting': self.num_patients_waiting,
            'utilization_rate_doctors': self.available_doctors / 30,  # Assuming 30 as max doctors
            'utilization_rate_beds': self.available_beds / 100,  # Assuming 100 as max beds
            'avg_waiting_time': self.avg_waiting_time
        }
        return metrics

    def render(self, mode='console'):
        """
        Render the environment to the console for monitoring.
        """
        if mode == 'console':
            metrics = self._get_metrics()
            for key, value in metrics.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

    def close(self):
        print("Closing Hospital Environment.")


if __name__ == "__main__":
    env = HospitalEnv()
    for episode in range(10):  # Run 10 episodes for demonstration
        state = env.reset()
        done = False
        while not done:
            action = env.action_space.sample()  # Choose a random action
            state, reward, done, info = env.step(action)
            env.render()  # Render the state of the environment
    env.close()
