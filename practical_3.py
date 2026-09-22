def astar(start, goal, get_neighbours, guess):
    # The to-do list. Each note is [f, g, place, path_so_far].
    frontier = [[guess(start), 0, start, [start]]]
    visited = []            # places we already explored
    explored_count = 0      # how many places we explored (for comparing)

    while len(frontier) > 0:
        # 1) Find the note with the SMALLEST f by looking through the list.
        best = 0
        for i in range(len(frontier)):
            if frontier[i][0] < frontier[best][0]:
                best = i
        note = frontier.pop(best)     # take that note out of the list

        f, g, place, path = note      # 

        # 2) If we already explored this place, skip it.
        if place in visited:
            continue
        visited.append(place)
        explored_count = explored_count + 1

        # 3) Did we reach the goal? Then we are done.
        if place == goal:
            return path, explored_count

        # 4) Add each neighbour to the to-do list as a new note.
        for nxt in get_neighbours(place):
            if nxt not in visited:
                new_g = g + 1                       # one more step
                new_f = new_g + guess(nxt)          # f = g + h
                frontier.append([new_f, new_g, nxt, path + [nxt]])


    return None, explored_count     # no path found

print("A* is ready. ✅")
