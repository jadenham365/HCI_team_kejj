import numpy as np
import matplotlib.pyplot as plt

# Data
misses = {
    'Lorenzo': {'key': [5, 3, 3, 1, 1], 'weird': [3, 4, 2, 4, 0]},
    'Kevin': {'key': [0, 3, 1, 0, 0], 'weird': [0, 2, 2, 2, 1]},
    'Lester': {'key': [1, 2, 1, 2, 0], 'weird': [0, 0, 1, 1, 2]},
    'Jason': {'key': [0, 0, 1, 2, 1], 'weird': [4, 2, 5, 2, 3]},
    'Mai': {'key': [1, 1, 1, 0, 3], 'weird': [0, 0, 0, 0, 2]},
    'Bailey': {'key': [2, 2, 5, 2, 4], 'weird': [1, 10, 18, 20, 11]},
    'Vincent': {'key': [3, 2, 3, 3, 3], 'weird': [7, 7, 3, 4, 1]},
    'Younghun': {'key': [2, 1, 1, 1, 0], 'weird': [2, 1, 1, 2, 3]},
}

averages = {'key': [], 'weird': []}
std_devs = {'key': [], 'weird': []}

# Calculate average and standard deviation for each participant
for m in misses.values():
    for kind in ['key', 'weird']:
        avg_miss = np.mean(m[kind])
        std_miss = np.std(m[kind])
        averages[kind].append(avg_miss)
        std_devs[kind].append(std_miss)

# Plot
bar_width = 0.35
indices = np.arange(len(misses))
fig, ax = plt.subplots()

bar1 = ax.bar(indices - bar_width/2, averages['key'], bar_width, label='Key Input', yerr=std_devs['key'], capsize=5, color='cyan')
bar2 = ax.bar(indices + bar_width/2, averages['weird'], bar_width, label='Weird Input', yerr=std_devs['weird'], capsize=5, color='r')

ax.set_xlabel('Participant Number')
ax.set_ylabel('Average Number of Missed Grabs')
ax.set_title('Average Number of Missed Grabs per Participant for Key and Weird Inputs')
ax.set_xticks(indices)
ax.set_xticklabels([str(i+1) for i in range(len(misses))])
ax.legend()


plt.tight_layout()
plt.show()
