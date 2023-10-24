import matplotlib.pyplot as plt

# Data
participants = {
    '1': [25.48, 16.031, 12.399, 11.09, 15.32],
    '2': [33.86, 20.406, 23.445, 16.08, 15.816],
    '3': [66.737, 37.199, 30.864, 30.355, 31.56],
    '4': [19.342, 10.939, 10.86, 10.337, 15.163],
    '5': [70.903, 39.232, 64.167, 50.416, 36.082],
    '6': [42.471, 29.451, 32.994, 39.333, 41.573],
    '7': [34.878, 31.171, 26.297, 24.548, 27.307],
    '8': [38.098, 28.5, 21.072, 21.311, 37.568],
}

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

trial_indices = [1, 2, 3, 4, 5]

for participant, times in participants.items():
    ax.plot(trial_indices, times, '-o', label=f'Participant {participant}', lw=2)

ax.set_title('Time Taken Over Trials (Weird Inputs)')
ax.set_xlabel('Trial Number')
ax.set_ylabel('Time (seconds)')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.tight_layout()
plt.show()
