import json
with open("data.json" , "r") as read_file:
    data = json.load(read_file)


print("""Interface Status
================================================================================""")
print("""DN                                             Description          Speed                    MTU """)
print("----------------------------------------------- ------------------  ------                  -----")
for x in range(3):
    for i, k in data["imdata"][x]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k.ljust(51), end="")
        if i == "descr":
            print(k.ljust(0), end="")
        if i == "speed":
            print(k.ljust(8), end="")
        if i == "mtu":
            print(k)









# for x in range(3):
#     for i, k in data["imdata"][x]['l1PhysIf']["attributes"].items():
#         if i == 'dn':
#             print(k, end="                          ")
#         if i == "speed":
#             print(k, end="                                         ")
#         if i == "mtu":
#             print(k, end="                   ")

