tasks = ["Collect form submission", "Validate email", "Send confirmation"]
with open("tasks.txt", "w", encoding="utf-8") as file:
    for task in tasks:
        file.write(task + "\n")
with open("tasks.txt", "r", encoding="utf-8") as file:
    print(file.read(), end="")
