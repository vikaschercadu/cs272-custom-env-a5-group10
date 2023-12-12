# Hospital Resource Management

## Project Summary
This project simulates a hospital environment where an agent must manage resources such as doctors and beds to treat patients efficiently. We use reinforcement learning to learn optimal resource allocation strategies.

## Environment
The `HospitalEnv` is a custom gymnasium environment encapsulating the challenges of hospital management, including patient intake and resource allocation.

### State Space
The HospitalEnv boasts a comprehensive state space, encapsulating vital parameters for efficient hospital management:

Waiting Patients: The number of patients currently awaiting treatment.
Available Doctors: The count of doctors ready for patient care.
Available Beds: The number of beds ready for patient occupancy.
Average Waiting Time: The average time patients spend waiting for treatment.
Current Hour: The ongoing hour within the hospital environment.
### Action Space
Navigating through hospital resource allocation, the agent has three distinct actions at its disposal:

No Action: The agent refrains from taking any immediate action.

Allocate More Doctors: A decision to increase the number of available doctors for patient care.

Allocate More Beds: An action aimed at increasing the number of beds available for patient occupancy.

### Rewards
Rewards are given based on reducing patient waiting times and efficient resource usage.

## Training
We use Ray RLlib and PPO, DQN and APPO to train our agent. The `train_agent.py` script handles the training process and saves the best model.

### Configuration
- **Framework**: TensorFlow
- **Workers**: 1
- **GPUs**: 0 (CPU training)

### Stopping Criteria
- **Iterations**: 50
- **Target Reward**: 10000

## Results
reward Max and Reward mean plots are included for all the 3 models trained.

##Proximal Policy Optimization (PPO)

<img width="402" alt="image" src="https://github.com/vikaschercadu/cs272-custom-env-a5-group10/assets/40718425/2811acd0-b2b3-4bcc-ad81-da1180488f9d">

<img width="402" alt="image" src="https://github.com/vikaschercadu/cs272-custom-env-a5-group10/assets/40718425/a8cfc332-c562-4e30-8cd2-6b0cf8aa8883">

##Asynchronous Proximal Policy Optimization (APPO)

<img width="402" alt="image" src="https://github.com/vikaschercadu/cs272-custom-env-a5-group10/assets/40718425/b0e34985-7cb7-4cda-b1fe-cbe6d4641cd2">

<img width="402" alt="image" src="https://github.com/vikaschercadu/cs272-custom-env-a5-group10/assets/40718425/2946fcb4-e964-413c-ba2a-4f28d2db6866">

##Deep Q Networks (DQN)

<img width="402" alt="image" src="https://github.com/vikaschercadu/cs272-custom-env-a5-group10/assets/40718425/1e8fbfe5-55e1-4683-b16b-8e87f44e8f9a">

<img width="402" alt="image" src="https://github.com/vikaschercadu/cs272-custom-env-a5-group10/assets/40718425/0adee7a4-1269-40b9-8a85-2028f804a35a">

### Metrics
- **Episode Reward Mean**
- **Episode Reward Max**

## Usage
To run the training, execute `python train_agent.py` in the terminal.

