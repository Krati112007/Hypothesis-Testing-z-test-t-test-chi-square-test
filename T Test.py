import scipy.stats as st
import numpy as np

s_x = 90      # sample mean
p_u = 82      # hypothesized population mean
s = 20        # sample standard deviation
n = 81        # sample size
ap = 0.05     # alpha

# critical t value (right-tailed test)
t_table = st.t.ppf(1 - ap, df=n-1)

# t statistic
t_cal = (s_x - p_u) / (s / np.sqrt(n))

print("t statistic =", t_cal)
print("critical t =", t_table)

# conclusion
if t_cal > t_table:
    print("Reject H0 (evidence for Ha)")
else:
    print("Fail to reject H0")