class room():
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits


    def __repr__(self):
        seen_exits = ""
        for exit in self.exits:
            seen_exits = seen_exits + exit + "\n"
        if seen_exits == "":
            seen_exits = "None!"

        a = "This is:","\t" + self.name, self.description, "You can see the following exits:", seen_exits
        ret = ""
        for b in a:
            ret = ret + b + "\n"
        return ret


class locale():

    def __init__(self, rooms):
        self.rooms = rooms


    def __repr__(self):
        a = ""
        for new_room in self.rooms:
            a = a + new_room.name + "\n"
        return a


    def fetch_room(self, current_room, new_room):
        for room in self.rooms:
            if room.name.title() == new_room.title():
                return room
        return current_room

entrance = room("Entrance", "This is the entrance to the house.",["Sitting Room"])
sitting_room = room("Sitting Room", "This is the sitting room. Nice and cosey.",["Entrace"])
new_loc = locale([entrance, sitting_room])
print(new_loc)


def main(current_room):
    print(current_room)
    dest = input("Where would you like to go?")
    if dest.lower() == "quit":
        exit()
    new_room = new_loc.fetch_room(current_room,dest.title())
    main(new_room)



main(entrance)