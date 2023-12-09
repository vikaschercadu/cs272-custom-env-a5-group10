# Project Name
## Project Summary
<!-- Around 200 Words -->
<!-- Cover (1) What problem you are solving, (2) Who will use this RL module and be happy with the learning, and (3) a brief description of the results -->

## State Space
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

## Action Space
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

## Rewards
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

## RL Algorithm 

## Starting State [if applicable]
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

## Episode End [if applicable]
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

## Results

# Hospital Resource Management

## Project Summary
This project simulates a hospital environment where an agent must manage resources such as doctors and beds to treat patients efficiently. We use reinforcement learning to learn optimal resource allocation strategies.

## Environment
The `HospitalEnv` is a custom gymnasium environment encapsulating the challenges of hospital management, including patient intake and resource allocation.

### State Space
The state includes the number of waiting patients, available doctors, available beds, average waiting time, and current hour.

### Action Space
The agent can take three actions: no action, allocate more doctors, or allocate more beds.

### Rewards
Rewards are given based on reducing patient waiting times and efficient resource usage.

## Training
We use Ray RLlib and PPO to train our agent. The `train_agent.py` script handles the training process and saves the best model.

### Configuration
- **Framework**: TensorFlow
- **Workers**: 1
- **GPUs**: 0 (CPU training)

### Stopping Criteria
- **Iterations**: 50
- **Target Reward**: 200

## Results
Training outputs include episode rewards, episode lengths, and episodes per iteration. The CLIReporter provides live metrics during training. The best model's checkpoint path is printed upon completion.

### Metrics
- **Episode Reward Mean**: The average reward per episode.
- **Episode Length Mean**: The average number of steps taken per episode.
- **Episodes This Iter**: The number of episodes run in the current iteration.

### Evaluation
Post-training evaluation metrics will be added upon running the evaluation script (coming soon).

## Usage
To run the training, execute `python train_agent.py` in the terminal.

