import numpy as np
import matplotlib.pyplot as plt
import gym

# 0 -> left
# 1 -> down
# 2 -> right
# 3 -> up

#a random policy
policy = {0: 1, 1: 2, 2: 3, 3: 0, 4: 1, 6: 1, 8: 2, 10: 1, 13: 2, 14: 2}


env = gym.make('FrozenLake-v1')
n_games = 1000
win_pct = []
scores = []

for i in range(n_games): # looping through episodes
    # initializing at the begining of each episode
    done = False
    obs = env.reset()
    score = 0
    while not done:
        action = policy[obs]
        obs, reward, done, info = env.step(action) # preforming an action
        score += reward
    scores.append(score)

    if i % 10 == 0: # for each 10 episodes, we get the statistics
        average = np.mean(scores[-10:])
        win_pct.append(average)

plt.plot(win_pct)
plt.show()