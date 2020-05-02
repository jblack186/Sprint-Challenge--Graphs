from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.

# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"


room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
world.print_rooms()
player = Player("Name", world.starting_room)


# FILL THIS IN
traversal_path = []

directions = {'n':'s', 's':'n', 'e':'w', 'w':'e' }

previous_direction = [None]
rooms = {}
visited = {}

rooms[0] = player.current_room.get_exits()
print(rooms[0])
visited[0] = player.current_room.get_exits()

while len(rooms) < len(room_graph) - 1:
    # print(player.current_room, player.current_room.id)
    # print(previous_direction)
    # print(rooms)
    # print(player.current_room)
    if player.current_room.id not in rooms:
        rooms[player.current_room.id] = player.current_room.get_exits()
        visited[player.current_room.id] = player.current_room.get_exits()
        last_direction = previous_direction[-1]
        # print(player.current_room)
        # print(previous_direction)
        visited[player.current_room.id].remove(last_direction)
        # print(rooms)
        # print(visited)
    
    # print(f"id: {visited[player.current_room.id]}")
    while len(visited[player.current_room.id]) < 1:
        reverse = previous_direction.pop()
        traversal_path.append(reverse)
        player.travel(reverse)

    exit_direction = visited[player.current_room.id].pop(0)
    # print(exit_direction)
    # print(traversal_path)
    traversal_path.append(exit_direction)
    # print(traversal_path)
    previous_direction.append(directions[exit_direction])
    player.travel(exit_direction)

    # print(len(room_graph) - len(rooms))
    # if len(room_graph) - len(rooms) == 1:
    #     rooms[player.current_room.id] = player.current_room.get_exits()
    #     print(f"exits: {rooms[player.current_room.id]}")

# world.print_rooms()

# print(rooms)
# print(visited)
# print(traversal_path)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")# You may uncomment the smaller graphs for development and testing purposes.

