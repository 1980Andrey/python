# Задание No 3

with open("task3.txt") as f:
    worker_list = [worker_line.split() for worker_line in f.readlines()]

worker_with_info = [
    {"name": woeker[0], "salary": float(worker[1])}
    for worker in worker_list
    if len(worker) > 1
]
