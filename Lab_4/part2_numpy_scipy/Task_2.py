import numpy as np


def calculate_way(lengths_str, speeds_str, k, p):


    lengths = np.array(list(map(float, lengths_str.split())))
    speeds = np.array(list(map(float, speeds_str.split())))


    k_idx = k - 1
    p_idx = p - 1


    selected_lengths = lengths[k_idx:p_idx + 1]
    selected_speeds = speeds[k_idx:p_idx + 1]


    total_distance = np.sum(selected_lengths)
    times = selected_lengths / selected_speeds
    total_time = np.sum(times)
    average_speed = total_distance / total_time

    return total_distance, total_time, average_speed



lengths = "20 8 9 18 5 12 16 16 6 7"
speeds = "44 70 44 66 46 38 38 37 66 67"
k = 4
p = 7

S, T, V = calculate_way(lengths, speeds, k, p)

print(f"S = {S:.2f} км")
print(f"T = {T:.2f} час")
print(f"V = {V:.2f} км/ч")