import matplotlib.pyplot as plt

def calculate_cycle_time(stages):
    total_time = sum(stages.values())
    bottleneck = max(stages, key=stages.get)
    return total_time, bottleneck

def plot_cycle_time(stages):
    plt.bar(stages.keys(), stages.values(), color='orange')
    plt.title('Cycle Time Analysis')
    plt.xlabel('Stage')
    plt.ylabel('Time (minutes)')
    plt.show()

stages = {
    "Stage 1": 15,
    "Stage 2": 20,
    "Stage 3": 25,
    "Stage 4": 30
}

total_time, bottleneck = calculate_cycle_time(stages)
print(f"Total Cycle Time: {total_time} minutes")
print(f"Bottleneck Stage: {bottleneck}")

plot_cycle_time(stages)
