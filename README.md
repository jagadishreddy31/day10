# 🐍 Python Code2Xplore – 60 Days Challenge
## Day 10: User Profile Validation System

**Student:** N.M.S.Jagadiswara Reddy  
**Register Number:** AP24110011621  
**Course:** Hands on Python (CSE205)  
**Institution:** SRM University–AP, Department of Computer Science and Engineering  
**Concerned Teacher:** Dr. Yasir Afaq  
**Date of Submission:** 26-04-2026  

---

## 📌 Problem Statement

A university stores student data like marks, attendance, and scores. When this data is copied for analysis, an incorrect copy operation can cause changes in the copy to silently affect the original data — a phenomenon known as **data drift**.

This challenge requires:
- Generating student data randomly
- Making both a **shallow copy** and a **deep copy** of the data
- Modifying the copies using a personalized roll-number-based logic
- Checking whether the original data was affected
- Classifying the result as `Stable Data`, `Minor Drift`, `Critical Drift`, or `Copy Failure Detected`

---

## 🧠 Logic & Approach

1. **Data Generation** — 12 student records created with random `marks` (40–100), `attendance` (60–100), and `scores` (two values, 10–25 each)
2. **Copying** — One `shallow copy` (`list.copy()`) and one `deep copy` (`copy.deepcopy()`) are made
3. **Personalized Modification** — Roll number `24110011621 % 3 = 2`, so `k = 2`. Only students at **even indexes (0, 2, 4, 6, 8, 10)** — 6 out of 12 — are modified using:
   - `marks = int(marks + sqrt(marks))`
   - `attendance -= 5`
   - `scores[0] += 2`
4. **Statistical Analysis** — NumPy used for mean, standard deviation, and drift; manual mean also computed
5. **Data Normalization** — Min-max normalization applied to deep copy marks
6. **Result Classification** — Drift threshold used to classify data stability; shallow copy mutation detected as `Copy Failure`

---

## 🔢 Personalization

| Parameter | Value |
|-----------|-------|
| Roll Number | 24110011621 |
| k = roll % 3 | **2** |
| Indexes modified | 0, 2, 4, 6, 8, 10 (even indexes) |
| Students affected | 6 out of 12 |

---

## ✅ Test Cases

| Test Case | Expected Output | Actual Output |
|-----------|-----------------|---------------|
| Does shallow copy change original marks? | Yes — inner dicts are shared, original marks increase | Yes — original marks changed from 75 to 83 for student at index 0 |
| Does deep copy change original marks? | No — deep copy is fully independent | No — original marks untouched after deep copy modification |

---

