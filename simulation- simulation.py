import matplotlib.pyplot as plt

V = 12

resistances = [1, 2, 3, 4, 5, 6, 8, 10, 12]
currents = [V / R for R in resistances]

plt.plot(resistances, currents, marker="o")

plt.title("Ohm's Law Simulation")
plt.xlabel("Resistance (Ω)")
plt.ylabel("Current (A)")
plt.grid(True)
