

import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

control_group = pd.read_excel("datasets/ab_testing.xlsx", sheet_name = "Control Group")
control_group = control_group[["Impression", "Click", "Purchase", "Earning"]]
test_group = pd.read_excel("datasets/ab_testing.xlsx", sheet_name = "Test Group")
test_group = test_group[["Impression", "Click", "Purchase", "Earning"]]


control_group.describe().T
control_group.isnull().sum()
test_group.describe().T
test_group.isnull().sum()

control_group["Purchase_per_Click"] = control_group["Purchase"] / control_group["Click"] * 100
control_group["Earning_per_Click"] = control_group["Earning"] / control_group["Click"]
control_group["Purchase_per_Click"].mean()
control_group["Earning_per_Click"].mean()
control_group["Earning"].sum()

test_group["Purchase_per_Click"] = test_group["Purchase"] / test_group["Click"] * 100
test_group["Earning_per_Click"] = test_group["Earning"] / test_group["Click"]
test_group["Purchase_per_Click"].mean()
test_group["Earning_per_Click"].mean()
test_group["Earning"].sum()

control_group["Impression"].sum()
test_group["Impression"].sum()

control_group["Click"].sum()
test_group["Click"].sum()

control_group["Purchase"].sum()
test_group["Purchase"].sum()

control_to_test_earning_diff = ((test_group["Earning"].sum() - control_group["Earning"].
                                sum()) / control_group["Earning"].sum()) * 100


test_stat, pvalue = shapiro(control_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



test_stat, pvalue = levene(control_group["Purchase"],
                           test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



test_stat, pvalue = ttest_ind(control_group["Purchase"],
                              test_group["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



