# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def move(self, direction):
        next_room = self.current_room.move_direction(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print("You're going the wrong way you dunce!")