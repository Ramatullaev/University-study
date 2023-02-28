import json

with open("data.json", "r") as read_file:
    data = json.load(read_file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("------------------------------------------------- --------------------  ------   ------")

for x in range(3):
    attributes = data["imdata"][x]["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print("{:<71} {:<10} {:<10}".format(dn,speed, mtu))

# I used ChatGPT to write it 