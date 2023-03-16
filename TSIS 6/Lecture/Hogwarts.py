
students = []
with open("magic.txt", "r") as file:
    names = file.readlines()
for name in names:
    print(f"{name}")
    # for name in names.split(","):
    #     print(f"{name}")




students = []
oppo =  open("magic.txt", "r")
    #names = file.readline()
for x in oppo:
    print(x)
    # for name in names.split(","):
    #     print(f"{name}")





students = []
with open("magic.txt", "r") as file:
    names = file.readlines()

for name in names:
    print(name.rstrip())
    # for name in names.split(","):
    #     print(f"{name}")