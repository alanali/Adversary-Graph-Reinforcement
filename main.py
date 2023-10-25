from qlearning import QAgent
from plot import PlotData
from game import ManipulationAgent as MAgent

"""
Example matrix representation
r = np.array([[0,1,1,1,0,0,0,0,0,0],
				[0,0,0,0,1,0,0,0,0,0],
				[0,1,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,1,1,0,0,0],
				[0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,1,1,0],
				[0,0,0,0,0,0,0,0,0,1],
				[0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,1,0,0],
				[0,0,0,0,0,0,0,0,0,0]])
Example dictionary representation
g = {1:[2, 3, 4], 2:[5], 3:[2], 4:[6, 7], 5:[], 6:[8, 9], 7:[10], 8:[], 9:[8], 10:[]}
"""

alpha = 0.9 # Learning rate
gamma = 0.8 # Discount factor

g = {1:[1, 2, 10, 11], 2: [2, 3, 4, 5, 6, 7], 3: [3, 8, 9], 4: [4, 8, 9], 5: [5, 8, 9], 6: [6, 8, 9], 7: [7, 8, 9], 8: [8], 9: [9, 13], 10: [10], 11: [11, 12, 13], 12: [12], 13: [13, 14], 14: [14, 15, 16, 17, 18, 19], 15: [15, 20], 16: [16, 20], 17: [17, 21], 18: [18, 21], 19: [19, 21], 20: [20, 22], 21: [21, 22], 22: [22, 23, 24, 25], 23: [23], 24: [24, 27], 25: [25, 26, 27], 26: [26], 27: [27, 28], 28: [27, 28, 29], 29: [28, 29, 30, 32], 30: [29, 30, 31], 31: [30, 31], 32: [32]}

many_runs = list(range(1000, 30001, 1000))
test_runs = list(range(1000, 10001, 1000))

# PlotData.generate_graphs(g, alpha, gamma, test_runs, show=True, save=False)
# PlotData.compare_graphs(g, alpha, gamma, test_runs, show=True, save=False)

testing = QAgent(alpha, gamma, g, consequence=0, random=True)
rewards = testing.rewards
risks = testing.risks

# No Manipulation
test = testing.training(1, 31, 10000)
success = test[0]
reward = test[1]
path = test[2]
testing.print_helper(1, 31, path, success)

MAgent.manipulate(rewards, risks, testing.consequence)