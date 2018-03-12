import gym
from naive import *
import numpy as np

EPISODES = 500
MAX_STEPS = 1000
FN = random_step
RENDER = False
PRINT_EVERY = 100

if PRINT_EVERY is None:
	PRINT_EVERY = EPISODES + 1

env = gym.make('CartPole-v0')

a_reward = [] # total summed rewards of every episode
a_t = []      # step before ending of an episode 
for episode in range(EPISODES):
	if episode%PRINT_EVERY == 0:
		print(f'{episode} episodes completed')
	e_reward = 0
	observation = env.reset()
	for t in range(MAX_STEPS):	
		if RENDER:
			env.render()
		step = FN(observation)
		observation , reward, done, info = env.step(step)
		e_reward += reward
		if done:
			if episode%PRINT_EVERY == 0:
				print(f'Ended at timestep {t}')
			a_t.append(t)
			break
	a_reward.append(e_reward)


print(f' The mean over {EPISODES} for average {np.mean(a_t)} steps is {np.mean(a_reward)}.')
print(f' STD: {np.std(a_t)} steps , {np.std(a_reward)} rewards')
print(f' MAX: {np.max(a_t)} steps , MIN:  {np.min(a_t)} steps')




