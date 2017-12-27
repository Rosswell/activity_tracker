import numpy as np
import random
import pandas as pd
pd.set_option('expand_frame_repr', False)


def find_partition(pc_list, sample_list):
    "returns: An attempt at a partition of `int_list` into two sets of equal sum"
    A = []
    B = []
    pc_A_count = 0
    pc_B_count = 0
    pc_sum_mod = np.sum(pc_list)
    sample_sum_mod = np.sum(sample_list)
    pc_list = [x + pc_sum_mod for x in pc_list]
    sample_list = [x + sample_sum_mod for x in sample_list]
    for n in sorted(pc_list, reverse=True):
        if sum(A) < sum(B) and len(A) < 48:
            A.append(n - pc_sum_mod)
            pc_A_count += 1
        else:
            B.append(n - pc_sum_mod)
            pc_B_count += 1
    for n in sorted(sample_list, reverse=True):
        if sum(A) < sum(B) and len(A) < 48:
            A.append(n - sample_sum_mod)
        else:
            if len(B) == 48:
                A.append(n - sample_sum_mod)
            else:
                B.append(n - sample_sum_mod)
    return (len(A), len(B), np.sum(A), np.sum(B), pc_A_count, pc_B_count, abs(len(A) - len(B)), abs(np.sum(A) - np.sum(B)))

df = pd.DataFrame(columns = ['lenA', 'lenB', 'sumA', 'sumB', 'PCsInA', 'PCsInB', 'sizeDifference', 'totalVolumeDifference'])
actual_samples = pd.read_csv('/Users/ross/Desktop/Query Results.csv')
for _ in range(10000):
    pc_size = random.randint(2,5)
    sample_size = random.randint(80,96) - pc_size
    pc_volumes = actual_samples['udfvalue'].sample(pc_size).tolist()
    sample_volumes = actual_samples['udfvalue'].sample(sample_size).tolist()
    lenA, lenB, sumA, sumB, pc_A_count, pc_B_count, size_diff, sum_diff = find_partition(pc_volumes, sample_volumes)
    df = df.append({'lenA':lenA, 'lenB':lenB, 'sumA':sumA, 'sumB':sumB, 'PCsInA':pc_A_count, 'PCsInB':pc_B_count, 'sizeDifference':size_diff, 'totalVolumeDifference':sum_diff}, ignore_index=True)
print(df['sizeDifference'].value_counts()/1000)
print(df[['sizeDifference', 'totalVolumeDifference']].describe())
print(df.describe())


# print(A, np.sum(A))
#
# print(B, np.sum(B))

def find_partition(pc_list, sample_list):
    "returns: An attempt at a partition of `int_list` into two sets of equal sum"
    A = []
    B = []
    pc_sum_mod = np.sum(pc_list)
    sample_sum_mod = np.sum(sample_list)
    pc_list = [x + pc_sum_mod for x in pc_list]
    sample_list = [x + sample_sum_mod for x in sample_list]
    for n in sorted(pc_list, reverse=True):
        if sum(A) < sum(B) and len(A) < 48:
            A.append(n - pc_sum_mod)
        else:
            B.append(n - pc_sum_mod)
    for n in sorted(sample_list, reverse=True):
        if sum(A) < sum(B) and len(A) < 48:
            A.append(n - sample_sum_mod)
        else:
            if len(B) == 48:
                A.append(n - sample_sum_mod)
            else:
                B.append(n - sample_sum_mod)
    return (len(A), len(B), np.sum(A), np.sum(B), abs(len(A) - len(B)), abs(np.sum(A) - np.sum(B)))