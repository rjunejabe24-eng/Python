import numpy as np

# Load CSV (skip header, handle spaces)
data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, dtype=float, autostrip=True)

# Split into columns
timestamp = data[:,0]
temperature = data[:, 1]
distance    = data[:, 2]
battery     = data[:, 3]
humidity    = data[:, 4]

# --- Calculations ---
# Averages, min, max
avg_temp, min_temp, max_temp = np.mean(temperature), np.min(temperature), np.max(temperature)
avg_dist, min_dist, max_dist = np.mean(distance), np.min(distance), np.max(distance)
avg_batt, min_batt, max_batt = np.mean(battery), np.min(battery), np.max(battery)
avg_hum,  min_hum,  max_hum  = np.mean(humidity), np.min(humidity), np.max(humidity)

# Time when temperature was highest
max_temp_index = np.argmax(temperature)
time_of_max_temp = data[max_temp_index, 0]   # timestamp column

# Battery below 30%
battery_below_30 = np.sum(battery < 30)

# --- Save results ---
results = np.array([
    ["Sensor", "Average", "Minimum", "Maximum"],
    ["Temperature", avg_temp, min_temp, max_temp],
    ["Distance", avg_dist, min_dist, max_dist],
    ["Battery", avg_batt, min_batt, max_batt],
    ["Humidity", avg_hum, min_hum, max_hum],
    ["---", "---", "---", "---"],
    ["Time of Max Temp", time_of_max_temp, "-", max_temp],
    ["Battery <30% Count", battery_below_30, "-", "-"]
], dtype=object)

np.savetxt("sensor_results.csv", results, fmt="%s", delimiter=",")

# --- Print Summary ---
print("Results saved to sensor_results.csv")
print(results)