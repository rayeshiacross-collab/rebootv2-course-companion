tasks = ["collect data", "process data", "send report"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
