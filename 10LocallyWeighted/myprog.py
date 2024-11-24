import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

# Load data
data = pd.read_csv('data10_tips.csv')
bill = data['total_bill'].to_numpy()
tip = data['tip'].to_numpy()

# Apply lowess
smoothed = lowess(tip, bill, frac=0.3)  # `frac` controls the smoothing parameter

# Extract smoothed values
smoothed_x, smoothed_y = smoothed[:, 0], smoothed[:, 1]

# Plot the results
plt.scatter(bill, tip, color='green')
plt.plot(smoothed_x, smoothed_y, color='red', linewidth=6)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
# plt.legend()
# plt.show()
