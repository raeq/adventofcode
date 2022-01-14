data = (*((*line,) for line in open("day23.txt")),)
print(data)
typeCost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms = {'A': 3, 'B': 5, 'C': 7, 'D': 9}


def extend(state):
    return (*state[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *state[3:],)


def roomSize(state):
    return len(state) - 3


def field(state, x, y):
    return state[y][x]


def stoppableFields(state):
    return tuple(i for i in range(1, len(state[0]) - 1) if i not in rooms.values())


def isInOwnRoom(state, x, y):
    if not isAmphipod(state, x, y):
        return False
    if x == rooms[field(state, x, y)]:
        return True
    return False


def isInAnyRoom(state, x, y):
    return y > 1


def isRoomComplete(state, x):
    for y in range(2, 2 + roomSize(state)):
        if not isInOwnRoom(state, x, y):
            return False
    return True


def roomsComplete(state):
    for room in rooms.values():
        if not isRoomComplete(state, room): return False
    return True


def isAmphipod(state, x, y):
    val = field(state, x, y)
    return val if val in rooms.keys() else False


def isEmpty(state, x, y):
    return field(state, x, y) == '.'


def isRoomEmpty(state, x):
    for y in range(2, 2 + roomSize(state)):
        if not isEmpty(state, x, y):
            return False
    return True


def hasRoomAvailable(state, x, y):
    amphipod = field(state, x, y)
    room = rooms[amphipod]
    if isRoomEmpty(state, room): return True
    for y in range(2, 2 + roomSize(state)):
        if not isEmpty(state, room, y) and not isInOwnRoom(state, room, y):
            return False
    return True


def isPathEmpty(state, x, targetX):
    while x != targetX:
        if x > targetX:
            x -= 1
        if x < targetX:
            x += 1
        if not isEmpty(state, x, 1):
            return False
    return True


def isBlockingRoom(state, x, y):
    for j in range(y + 1, 2 + roomSize(state)):
        if isAmphipod(state, x, j) and not isInOwnRoom(state, x, j):
            return True
    return False


def isBlockedInRoom(state, x, y):
    if y < 3: return False
    return not isEmpty(state, x, y - 1)


def moveinPos(state, room):
    for y in range(1 + roomSize(state), 1, -1):
        if isEmpty(state, room, y):
            return y


def canMove(state, x, y):
    return (not isInOwnRoom(state, x, y) or isBlockingRoom(state, x, y)) and not isBlockedInRoom(state, x, y)


def moveCost(state, x, y, i, j):
    return ((y - 1) + abs(x - i) + (j - 1)) * typeCost[field(state, x, y)]


def move(d, x, y, i, j):
    newData = (*((*(((field(d, a, b), field(d, x, y))[a == i and b == j], field(d, i, j))[a == x and b == y] for a in
                    range(len(d[b]))),) for b in range(len(d))),)
    return (newData, moveCost(d, x, y, i, j))


def checkState(state, cache):
    cached = cache.get(state)
    if cached is not None:
        return cached
    if roomsComplete(state):
        return 0
    costs = []
    for y in range(1, len(state)):
        for x in range(1, len(state[y])):
            amphipod = isAmphipod(state, x, y)
            if not amphipod:
                continue
            if canMove(state, x, y):
                room = rooms[amphipod]
                if hasRoomAvailable(state, x, y) and isPathEmpty(state, x, room):
                    newState, newCost = move(state, x, y, room, moveinPos(state, room))
                    cost = checkState(newState, cache)
                    if cost != -1:
                        costs.append(cost + newCost)
                elif isInAnyRoom(state, x, y):
                    for i in stoppableFields(state):
                        if not isPathEmpty(state, x, i):
                            continue
                        newState, newCost = move(state, x, y, i, 1)
                        cost = checkState(newState, cache)
                        if cost != -1:
                            costs.append(cost + newCost)
    cache[state] = min(costs) if costs else -1
    return cache[state]


print(checkState(data, {}), checkState(extend(data), {}))
