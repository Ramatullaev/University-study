import json

with open("data.json", "r") as read_file:
    data = json.load(read_file)

print("Interface Status")
print("=" * 80)
print("DN".ljust(51) + "Description".ljust(24) + "Speed".ljust(8) + "MTU")
print("-" * 80)

for x in range(3):
    for i, k in data["imdata"][x]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k.ljust(51), end="")
        if i == "descr":
            print(k.ljust(24), end="")
        if i == "speed":
            print(k.ljust(8), end="")
        if i == "mtu":
            print(k)
