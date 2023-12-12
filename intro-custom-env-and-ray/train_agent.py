import ray
from ray import tune
from ray.rllib.algorithms.dqn import DQN
from ray.rllib.algorithms.ppo import PPO
from ray.rllib.algorithms.appo import APPO


from hospital_env import HospitalEnv 

def train_hospital_env():
    tune.register_env("HospitalEnv", lambda config: HospitalEnv())

    ray.init()

    config = {
        "env": "HospitalEnv",
        "num_gpus": 0,
        "num_workers": 1,
        "framework": "tf",
    }

    stop_criteria = {
        "training_iteration": 50,
        "episode_reward_mean": 10000,
    }

    results = tune.run(
        DQN, 
        # PPO,
        # APPO,
        config=config, 
        stop=stop_criteria, 
        progress_reporter=tune.CLIReporter(
            metric_columns=["episode_reward_mean", "episode_len_mean", "episodes_this_iter"]
        ),
    )


    # checkpoint_path = results.get_best_checkpoint(trial=results.get_best_trial("episode_reward_mean"))
    # print(f"Best model checkpoint saved at: {checkpoint_path}")

if __name__ == "__main__":
    train_hospital_env()
