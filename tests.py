from Avl import Avl
from Bst import Bst
import numpy as np
import matplotlib.pyplot as plt
import random
import time


def generate_random_list(maxi, length):
    rand = list(range(10, maxi))
    random.shuffle(rand)

    return rand[:length]


# Adjustable
n_range = [100, 200, 400, 600, 800, 1000, 2000, 4000, 6000, 8000, 10000, 12000, 14000]
n_times = 10

avl_construct = []
avl_find_min = []
avl_balance = []
avl_error_construct = []
avl_error_find_min = []
avl_error_balance = []

bst_construct = []
bst_find_min = []
bst_balance = []
bst_error_construct = []
bst_error_find_min = []
bst_error_balance = []

for n in n_range:
    input_list = generate_random_list(n, 15)

    print(f"n = {n}")
    # AVL
    construct_time = []
    find_min_time = []
    balance_time = []
    for _ in range(n_times):
        avl = Avl(input_list)

        start = time.time()
        for i in range(n):
            avl.construct()
        construct_time.append(time.time() - start)

        start = time.time()
        for i in range(n):
            avl.construct()
        find_min_time.append(time.time() - start)

        start = time.time()
        for i in range(n):
            avl.construct()
        balance_time.append(time.time() - start)

    avl_construct.append(sum(construct_time) / n_times)
    avl_find_min.append(sum(find_min_time) / n_times)
    avl_balance.append(sum(balance_time) / n_times)
    avl_error_construct.append(np.std(construct_time))
    avl_error_find_min.append(np.std(find_min_time))
    avl_error_balance.append(np.std(balance_time))

    # BST
    construct_time = []
    find_min_time = []
    balance_time = []
    for _ in range(n_times):
        bst = Bst(input_list)

        start = time.time()
        for i in range(n):
            bst.construct()
        construct_time.append(time.time() - start)

        start = time.time()
        for i in range(n):
            bst.construct()
        find_min_time.append(time.time() - start)

        start = time.time()
        for i in range(n):
            bst.construct()
        balance_time.append(time.time() - start)

    bst_construct.append(sum(construct_time) / n_times)
    bst_find_min.append(sum(find_min_time) / n_times)
    bst_balance.append(sum(balance_time) / n_times)
    bst_error_construct.append(np.std(construct_time))
    bst_error_find_min.append(np.std(find_min_time))
    bst_error_balance.append(np.std(balance_time))

# Plots
# Comparing plot for construction function
plt.figure(figsize=(10, 6))
plt.plot(n_range, avl_construct, label='Avl construct')
plt.errorbar(n_range, avl_construct, yerr=avl_error_construct, label='Avl construct', fmt='none', ecolor='black', capsize=1)
plt.plot(n_range, bst_construct, label='Bst construct')
plt.errorbar(n_range, bst_construct, yerr=bst_error_construct, label='Bst construct', fmt='none', ecolor='black', capsize=1)
plt.title('BST and AVL construction')
plt.xlabel('Size of sequence (n)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/construct.png')
plt.show()

# Comparing plot for find min function
plt.figure(figsize=(10, 6))
plt.plot(n_range, avl_find_min, label='Avl find min')
plt.errorbar(n_range, avl_find_min, yerr=avl_error_find_min, label='Avl find min', fmt='none', ecolor='black', capsize=1)
plt.plot(n_range, bst_find_min, label='Bst find min')
plt.errorbar(n_range, bst_find_min, yerr=bst_error_find_min, label='Bst find min', fmt='none', ecolor='black', capsize=1)
plt.title('BST and AVL find min')
plt.xlabel('Size of sequence (n)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/findmin.png')
plt.show()

# BST plot for balance function
plt.figure(figsize=(10, 6))
plt.plot(n_range, bst_balance, label='BST balance')
plt.errorbar(n_range, bst_balance, yerr=bst_error_balance, label='BST balance', fmt='none', ecolor='black', capsize=1)
plt.title('BST balance')
plt.xlabel('Size of sequence (n)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/balance.png')
plt.show()
