import scipy.stats as st
import numpy as np

observed = np.array([22, 17, 20, 26, 22, 15])

# Expected frequencies for a fair die
expected = np.array([20, 20, 20, 20, 20, 20])

# Chi-square statistic
chi_cal = np.sum((observed - expected)**2 / expected)

# Critical value
alpha = 0.05
df = len(observed) - 1
chi_table = st.chi2.ppf(1 - alpha, df)

print("Chi-square statistic =", chi_cal)
print("Critical value =", chi_table)

if chi_cal > chi_table:
    print("Reject H0 : Die is not fair")
else:
    print("Fail to reject H0 : Die appears fair")



