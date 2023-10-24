import numpy as np
import matplotlib.pyplot as plt

# Data
presses = {
    'Lorenzo': {'key': [34, 24, 25, 27, 31], 'weird': [46, 35, 25, 27, 22]},
    'Kevin': {'key': [46, 33, 30, 22, 25], 'weird': [38, 34, 47, 36, 39]},
    'Lester': {'key': [51, 39, 51, 40, 34], 'weird': [63, 38, 39, 34, 40]},
    'Jason': {'key': [35, 32, 31, 28, 32], 'weird': [77, 36, 34, 37, 46]},
    'Mai': {'key': [61, 58, 48, 36, 40], 'weird': [75, 43, 96, 53, 45]},
    'Bailey': {'key': [80, 77, 51, 42, 37], 'weird': [87, 78, 93, 107, 97]},
    'Vincent': {'key': [96, 51, 35, 55, 36], 'weird': [89, 58, 51, 44, 60]},
    'Younghun': {'key': [44, 35, 44, 32, 30], 'weird': [56, 49, 35, 37, 64]},
}

averages = {'key': [], 'weird': []}
std_devs = {'key': [], 'weird': []}

# Calculate average and standard deviation for each participant
for m in presses.values():
    for kind in ['key', 'weird']:
        avg_press = np.mean(m[kind])
        std_press = np.std(m[kind])
        averages[kind].append(avg_press)
        std_devs[kind].append(std_press)

# Plot
bar_width = 0.35
indices = np.arange(len(presses))
fig, ax = plt.subplots()

bar1 = ax.bar(indices - bar_width/2, averages['key'], bar_width, label='Key Input', yerr=std_devs['key'], capsize=5, color='cyan')
bar2 = ax.bar(indices + bar_width/2, averages['weird'], bar_width, label='Weird Input', yerr=std_devs['weird'], capsize=5, color='r')

ax.set_xlabel('Participant Number')
ax.set_ylabel('Average Number of Inputs Pressed')
ax.set_title('Average Number of Inputs Pressed per Participant for Key and Weird Inputs')
ax.set_xticks(indices)
ax.set_xticklabels([str(i+1) for i in range(len(presses))])
ax.legend()


plt.tight_layout()
plt.show()
