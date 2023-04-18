from typing import Dict, List
from random import Random

# the Room class represents a room in the game
class Room:
    # each room has a name, description, list of items, and dictionary of exits
    name: str
    description: str
    items: list
    exits: dict
    
    def __init__(self, name: str, description: str, items: list, exits: dict):
        self.name = name
        self.description = description
        self.items = items
        self.exits = exits
        
    def __str__(self):
        return self.description
        
    def remove_item(self, item: str):
        self.items.remove(item)
        
    def get_exit(self, direction: str):
        return self.exits[direction]
    
    def get_exits(self):
        return self.exits.keys()
    
    def get_items(self):
        return self.items

# the Player class represents the player in the game, and has a name, room, and inventory which is a list of items
class Player:
    def __init__(self, name: str, room: Room):
        self.name = name
        self.room = room
        self.inventory = []
    
    # the move method moves the player to a new room
    def move(self, new_room: Room):
        self.room = new_room
    
    # the get_item method adds an item to the player's inventory
    def get_item(self, item: str):
        if item in self.room.get_items() and item not in self.inventory:
           self.room.remove_item(item)
           self.inventory.append(item)
        print(f"You picked up {item}.")
   
# the TreasureRoom class is a subclass of the Room class, and has an additional method to unlock the chest
class TreasureRoom(Room):
    def __init__(self, name: str, description: str, items: list, exits: dict):
        super().__init__(name, description, items, exits)
        
    def __str__(self):
        return f"{self.description} You see a chest."
    
    def unlock_chest(self, player: Player):
        # if the player has the key in their inventory, remove the key and add the treasure to their inventory
        if "key" in player.inventory:
            player.inventory.remove("key")
            player.inventory.append("treasure")
            print("You open the chest and find a treasure!")
        else:
            print("The chest is locked. You need a key to open it.")
            
# TODO: implement a portal room which is a special room which teleports the player to a random room in the game
# class PortalRoom(Room): 
            
# the Dragon class represents the dragon in the game, and has a name, room, and a method to attack the player. 
# TODO: dragon moves around randomly, and attacks player if they are in the same room. Sword breaks after one use.
class Dragon:
    def __init__(self, name: str, room: Room):
        self.name = name
        self.room = room

    # the move method moves the dragon to a new room
    def move(self, new_room: Room):
        self.room = new_room
        
    # the attack method attacks the player if they are in the same room as the dragon
    def attack(self, player: Player):
        # if the player doesn't have a sword, they lose the game
        if player.room == self.room and "sword" not in player.inventory:
            print("The dragon attacks you! You lose!")
            game_over = {"game_over": True, "win": False}
            return True
        else:
            # if the player has a sword, they fend off the dragon and the sword breaks
            if player.room == self.room and "sword" in player.inventory:
                print("The dragon attacks you, but you fend it off with your sword! Your sword breaks.")
            return False
        
# the main game loop, which creates the rooms, player, and dragon, and then runs the game.
# TODO: randomize the rooms, items, and exits in each room, create procedural replayability
class Game:
    random = Random()
    rooms: List[Room]
    player: Player
    dragon: Dragon
    game_over: bool
    win: bool
    
    def __init__(self, rooms: List[Room], player: Player, dragon: Dragon):
        self.rooms = rooms
        self.player = player
        self.dragon = dragon
        self.game_over = False
        self.win = False
    
    # game loop
    def play(self):
        while not self.game_over:
            print(self.player.room)
            print(f"Exits: {self.player.room.get_exits()}")
            print(f"Items: {self.player.room.get_items()}")
            print(f"Inventory: {self.player.inventory}")
            print()
            command = input("What do you want to do? ")
            if command == "quit":
                self.game_over = True
            elif command == "help":
                print("Commands: quit, help, move, get, attack")
            elif command == "move":
                direction = input("Which direction? ")
                if direction in self.player.room.get_exits():
                    self.player.move(self.get_room(self.player.room.get_exit(direction)))
                    if self.dragon.attack(self.player):
                        self.game_over = True
                # if the treasure is in the room and the player has the key, unlock the chest
                if isinstance(self.player.room, TreasureRoom) and "key" in self.player.inventory:
                    self.player.room.unlock_chest(self.player)
                    self.game_over = True

                else:
                    print("You cannot go that way.")
            elif command == "get":
                item = input("Which item? ")
                if item in self.player.room.get_items():
                    self.player.get_item(item)
            else:
                print("Invalid command.")
                
    def get_room(self, name: str):
        for room in self.rooms:
            if room.name == name:
                return room
            
# main function which gives our particular game a name, creates the rooms, player, and dragon, and then runs the game
if __name__ == "__main__":
    # create rooms
    room1 = Room("Room 1", "You are in a dark room.", [], {"east": "Room 4", "south": "Room 2", "north": "Room 5"})
    room2 = Room("Room 2", "You are in a room with a table.", ["key"], {"east": "Room 3", "north": "Room 1"})
    room3 = TreasureRoom("Room 3", "You are in a room with a treasure chest.", [], {"north": "Room 2", "west": "Room 3"})
    room4 = Room("Room 4", "You are in a room with a dragon.", [], {"west": "Room 1", "south": "Room 3"})
    room5 = Room("Room 5", "You are in a room with a corpse.", ["sword"], {"south": "Room 1"})
    RoomDragon = Room("Room Dragon", "You are in a room with a dragon.", [], {"west": "Room 1", "south": "Room 3"})
    rooms = [room1, room2, room3, room4, room5]
    
    # create player
    player = Player("Player 1", room1)
    
    # create dragon
    dragon = Dragon("Dragon 1", room4)
    
    # create game
    game = Game(rooms, player, dragon)
    
    # play game
    game.play()