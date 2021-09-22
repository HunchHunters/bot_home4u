import pandas as pd
import numpy as np

tbl = pd.read_excel('questions.xlsx')

ans1 = tbl.loc[2]
ans2 = tbl.loc[4]

# print(ans1[0])


def ban_check(ans1, ans2):

    # Gender check

    gender_important = ans1[2] ^ ans2[2]
    different_gender = ans1[1] ^ ans2[1]
    if gender_important and different_gender:
        print('Ban for gender\n')
        return False

    # Smoke check.

    only_one_of_them_smokes = ans1[7] ^ ans2[7]
    if only_one_of_them_smokes:
        print('Ban for smoking\n')
        return False

    # Budget check.
    different_budget = (ans1[5] != ans2[5])
    if different_budget:
        print('Ban for budget\n')
        return False

    # COVID check.
    if ans1[4]:
        first_is_ok = ans2[3]
    else:
        first_is_ok = True
    if ans2[4]:
        second_is_ok = ans1[3]
    else:
        second_is_ok = True

    if not (first_is_ok and second_is_ok):
        print('Ban for COVID\n')
        return False

    # Dishes check.
    if ans1[6] ^ ans2[6]:
        print('Ban for dishes\n')
        return False

    # Guests check.
    if ans1[8] < 3 and ans2[8] > 3:
        print('Ban for guests\n')
        return False

    if ans2[9] < 3 and ans1[8] > 3:
        print('Ban for guests\n')
        return False

    return True


# print(ban_check(ans1,ans2))

ans1 = ans1[9:]
ans2 = ans2[9:]


def psycho_compatibility(ans1, ans2):
    sz = len(ans1)
    i = np.arange(sz)
    i = np.reshape(i, (1, sz))
    j = i.T
    weights = 1 / np.sqrt(2 * np.pi * sz) * np.exp(-(i - j)**2 / 2 / sz)
    ans1 = np.array(ans1)
    ans2 = np.array(ans2)
    ans1 = np.reshape(ans1, (1, sz))
    ans2 = ans1.T

    dist = np.linalg.norm((ans1 - ans2)**2 * weights)

    # Calculate max distance
    v1 = np.ones((1, sz))
    v2 = v1 * 5
    mx = np.linalg.norm((v1 - v2)**2 * weights)

    return (1 - dist / mx) * 100


dist = psycho_compatibility(ans1, ans2)
print(dist)
