import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
M = 5.972e24  # Mass of Earth (kg) (Change to black hole mass if needed)

# Function to calculate time dilation
def time_dilation(r, M):
    rs = 2 * G * M / c**2  # Schwarzschild radius
    if r <= rs:
        return None  # Inside the event horizon, time stops for an outside observer
    return np.sqrt(1 - rs / r)

# Generate data points
r_values = np.linspace(1.1 * (2 * G * M / c**2), 10**7, 1000)  # From just outside Schwarzschild radius to far away
time_dilation_factors = [time_dilation(r, M) for r in r_values]

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(r_values, time_dilation_factors, label="Time Dilation Factor", color='blue')
plt.axvline(x=2 * G * M / c**2, color='red', linestyle='--', label="Schwarzschild Radius")
plt.xlabel("Distance from Massive Object (m)")
plt.ylabel("Time Dilation Factor")
plt.title("Gravitational Time Dilation Near a Massive Object")
plt.legend()
plt.grid()
plt.show()
