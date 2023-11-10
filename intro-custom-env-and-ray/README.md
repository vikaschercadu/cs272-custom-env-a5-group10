# Installation
- ray rllib
  - [Instruction](https://docs.ray.io/en/latest/ray-overview/installation.html)
  - pip example ```pip install -U "ray[rllib]"```
- tensorflow2
  - [Instruction](https://www.tensorflow.org/install?hl=en)

# ray rllib Configurations
- [Key concepts](https://docs.ray.io/en/latest/rllib/key-concepts.html)
- [Configuration options](https://docs.ray.io/en/latest/rllib/rllib-training.html#configuring-rllib-algorithms)
  - training options
  - environment options
  - deep learning framework options
  - rollout worker options
  - evaluation options
  - exploration options
  - options for training with offline data
  - options for training multiple agents
  - debugging options
  - options for experimental features


# ray rllib Environment Configuration
- [```register_env``` function](https://docs.ray.io/en/latest/rllib/rllib-env.html)

# ray rllib Results
- By default, all the training results are stored under ```~/ray_results```

# Visualization via tensorboard
```tensorboard --logdir=~/ray_results```


# Custom Env Reference
- [Farama gymnasium](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/)