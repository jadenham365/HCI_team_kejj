import matplotlib.pyplot as plt

# Data
weird_times = {
    'Lorenzo': [25.48, 16.031, 12.399, 11.09, 15.32],
    'Kevin': [33.86, 20.406, 23.445, 16.08, 15.816],
    'Lester': [66.737, 37.199, 30.864, 30.355, 31.56],
    'Jason': [19.342, 10.939, 10.86, 10.337, 15.163],
    'Mai': [70.903, 39.232, 64.167, 50.416, 36.082],
    'Bailey': [42.471, 29.451, 32.994, 39.333, 41.573],
    'Vincent': [34.878, 31.171, 26.297, 24.548, 27.307],
    'Younghun': [38.098, 28.5, 21.072, 21.311, 37.568],
}

# Find the worst trials for each participant
worst_trials = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
best_trials = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for times in weird_times.values():
    worst_trial_index = times.index(max(times)) + 1  # +1 because trial indices start at 1
    worst_trials[worst_trial_index] += 1
    best_trial_index = times.index(min(times)) + 1  # +1 because trial indices start at 1
    best_trials[best_trial_index] += 1

# Plot of worst
fig, ax = plt.subplots()
ax.bar(worst_trials.keys(), worst_trials.values(), color='cyan')
ax.set_title('Number of Participants with Worst Performance on Trial')
ax.set_xlabel('Trial Number')
ax.set_ylabel('Number of Participants')
ax.set_xticks(list(worst_trials.keys()))

plt.tight_layout()
plt.show()

# Plot of best
fig, ax = plt.subplots()
ax.bar(best_trials.keys(), best_trials.values(), color='cyan')
ax.set_title('Number of Participants with Best Performance on Trial')
ax.set_xlabel('Trial Number')
ax.set_ylabel('Number of Participants')
ax.set_xticks(list(best_trials.keys()))

plt.tight_layout()
plt.show()