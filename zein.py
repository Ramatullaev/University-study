import numpy as np
import matplotlib.pyplot as plt

# Constants
gamma = 1.4  # Specific heat ratio for an ideal diatomic gas
R = 8.314   # Gas constant (J/(mol*K))
n = 1       # Number of moles of the gas

# Temperature range
T = np.linspace(100, 1000, 100)  # Range of temperature values in Kelvin

# Calculate pressure values for the adiabatic curve
P = (n * R * T) ** (1 / gamma)

# Plotting
plt.plot(T, P)
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (Pa)')
plt.title('Adiabatic Curve on PT Graph')
plt.grid(True)
plt.show()
