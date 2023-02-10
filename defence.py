history = {
    "hero3" : {
        "ID" : 21861514,
        "name" : "Steve",
        "surname" : "Jobs"
    },
    "hero1" : {
        "ID" : 18346587,
        "name" : "Nelson",
        "surname" : "Mandela"
    },
    "hero2" : {
        "ID" : 20893456,
        "name" : "Richard",
        "surname" : "Feynman"
    }
    }
x = history.items()
print(x)

'''
from operator import itemgetter
sorted_x = dict(sorted(x , key = itemgetter(0) ))
sorted(x)
print(*x , sep = '\n')'''


# sorted_rooms = dict(sorted(rooms.items(), key=lambda item: item[1]))

#>>> from operator import itemgetter
#>>> sorted_rooms = dict(sorted(rooms.items(), key=itemgetter(1)))
