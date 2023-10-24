import numpy as np
import matplotlib.pyplot as plt

# Data
data = {
    'Lorenzo': {'key': [10.65, 8.027, 7.768, 9.004, 11.093], 'weird': [25.48, 16.031, 12.399, 11.09, 15.32]},
    'Kevin': {'key': [20.965, 11.931, 11.581, 12.307, 9.713], 'weird': [33.86, 20.406, 23.445, 16.08, 15.816]},
    'Lester': {'key': [43.791, 29.425, 32.703, 26.071, 22.746], 'weird': [66.737, 37.199, 30.864, 30.355, 31.56]},
    'Jason': {'key': [13.65, 10.784, 9.834, 9.887, 10.927], 'weird': [19.342, 10.939, 10.86, 10.337, 15.163]},
    'Mai': {'key': [38.315, 42.713, 26.97, 20.715, 22.749], 'weird': [70.903, 39.232, 64.167, 50.416, 36.082]},
    'Bailey': {'key': [45.533, 36.336, 26.064, 24.988, 21.543], 'weird': [42.471, 29.451, 32.994, 39.333, 41.573]},
    'Vincent': {'key': [31.254, 14.366, 9.53, 13.933, 9.471], 'weird': [34.878, 31.171, 26.297, 24.548, 27.307]},
    'Younghun': {'key': [22.305, 16.108, 17.018, 14.128, 11.905], 'weird': [38.098, 28.5, 21.072, 21.311, 37.568]},
}

averages = {'key': [], 'weird': []}
std_devs = {'key': [], 'weird': []}

# Calculate average and standard deviation for each participant
for times in data.values():
    for kind in ['key', 'weird']:
        avg_time = np.mean(times[kind])
        std_time = np.std(times[kind])
        averages[kind].append(avg_time)
        std_devs[kind].append(std_time)

# Plot
bar_width = 0.35
indices = np.arange(len(data))
fig, ax = plt.subplots()

bar1 = ax.bar(indices - bar_width/2, averages['key'], bar_width, label='Key Input', yerr=std_devs['key'], capsize=5, color='cyan')
bar2 = ax.bar(indices + bar_width/2, averages['weird'], bar_width, label='Weird Input', yerr=std_devs['weird'], capsize=5, color='r')

ax.set_xlabel('Participant Number')
ax.set_ylabel('Average Time (seconds)')
ax.set_title('Average Time per Participant for Key and Weird Inputs')
ax.set_xticks(indices)
ax.set_xticklabels([str(i+1) for i in range(len(data))])
ax.legend()


plt.tight_layout()
plt.show()
