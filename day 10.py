import random
import math
import copy
import numpy as np
import pandas as pd


def create(n):
    arr = []
    for i in range(n):
        arr.append({
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        })
    return arr


def change(arr, r):
    k = r % 3
    if k == 0:
        k = 1
    for i in range(len(arr)):
        if i % k == 0:
            val = arr[i]["marks"]
            arr[i]["marks"] = int(val + math.sqrt(val))
            arr[i]["attendance"] -= 5
            arr[i]["scores"][0] += 2
    return arr


def stats(a, b):
    x = [i["marks"] for i in a]
    y = [i["marks"] for i in b]
    m = np.mean(y)
    s = np.std(y)
    d = abs(np.mean(x) - m)
    mm = sum(y) / len(y)
    return m, s, d, mm


def result_check(d, t, a, s):
    if a != s:
        return "Copy Failure Detected"
    if d < t:
        return "Stable Data"
    if d < t * 2:
        return "Minor Drift"
    return "Critical Drift"


roll = 24110011606

data = create(12)
s1 = data.copy()
s2 = copy.deepcopy(data)

change(s1, roll)
change(s2, roll)

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(s1)
df3 = pd.DataFrame(s2)

nm = (df3["marks"] - df3["marks"].min()) / (df3["marks"].max() - df3["marks"].min())
df3["normalized_marks"] = nm

mean, std, drift, manual = stats(data, s2)
res = result_check(drift, 5, data, s1)
print(df1)
print(df2)
print(df3)
print(drift)
print((mean, drift, std))
print(res)