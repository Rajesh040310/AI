{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0304db7d-ce84-4a35-90ee-20334abf105b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#PRACTICAL2- Implement bfs,dfs,uniform cost search on graph or maze problem ; compare search cost and path quality"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bb3a1044-08e6-41c8-a50f-678cdcd91497",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " hello let's find the goal together\n",
      "start the mission\n"
     ]
    }
   ],
   "source": [
    "print(\" hello let's find the goal together\")\n",
    "print(\"start the mission\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "09018f16-5967-4d2a-b05f-77c18fae2025",
   "metadata": {},
   "outputs": [],
   "source": [
    "map_rooms = {\n",
    "    'A': ['B', 'C'],\n",
    "    'B': ['D'],\n",
    "    'C': ['G'],\n",
    "    'D': [],\n",
    "    'G': []\n",
    "}\n",
    "\n",
    "START_robot = 'A'\n",
    "goal = 'G'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1f2ce8de-160e-4237-bc0b-008c6e2fe321",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "START_robot A\n",
      "goal G\n",
      "map rooms :  {'A': ['B', 'C'], 'B': ['D'], 'C': ['G'], 'D': [], 'G': []}\n",
      "       A       \n",
      "       / \\       \n",
      "      B   C       \n",
      "     /     \\      \n",
      "    D      G     \n"
     ]
    }
   ],
   "source": [
    "print(\"START_robot\",START_robot)\n",
    "print(\"goal\",goal)\n",
    "print(\"map rooms : \", map_rooms)\n",
    "print( \"       A       \")\n",
    "print(\"       / \\       \")\n",
    "print(\"      B   C       \")\n",
    "print(\"     /     \\      \")\n",
    "print(\"    D      G     \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1ac09ed5-d97b-4bdd-bdde-76c942d9a7b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A', 'B', 'C', 'D', 'G']\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "def bfs(start,goal):\n",
    "    queue = [start]\n",
    "    visited =[]\n",
    "    order=[]\n",
    "    while queue:\n",
    "        room=queue.pop(0)\n",
    "        if room in visited:\n",
    "            continue\n",
    "        visited.append(room)\n",
    "        order.append(room)\n",
    "        if room == goal:\n",
    "            return order\n",
    "        for next in map_rooms[room]:\n",
    "            queue.append(next)\n",
    "    return order \n",
    "order = bfs(\"A\",\"G\")\n",
    "print(order)\n",
    "print(len(order))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2bc9784c-4883-471e-8b4f-6a207ad43d0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A', 'C', 'G']\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "def dfs(start,goal):\n",
    "    stack = [start]\n",
    "    visited =[]\n",
    "    order=[]\n",
    "    while stack:\n",
    "        room=stack.pop()\n",
    "        if room in visited:\n",
    "            continue\n",
    "        visited.append(room)\n",
    "        order.append(room)\n",
    "        if room == goal:\n",
    "            return order\n",
    "        for next in map_rooms[room]:\n",
    "            stack.append(next)\n",
    "    return order \n",
    "order = dfs(\"A\",\"G\")\n",
    "print(order)\n",
    "print(len(order))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e1606128-16c2-4e84-9ba0-7f650b4c6f96",
   "metadata": {},
   "outputs": [],
   "source": [
    "door_cost = {\n",
    "    'A': {'B': 2, 'C': 3},\n",
    "    'B': {'D': 4},\n",
    "    'C': {'D': 2},\n",
    "    'D': {'G':1},\n",
    "    \n",
    "}\n",
    "\n",
    "def pathcost(path):\n",
    "    total = 0\n",
    "\n",
    "    for i in range(len(path) - 1):\n",
    "        room = path[i]\n",
    "        next_room = path[i + 1]\n",
    "\n",
    "        total = total + door_cost[room][next_room]\n",
    "\n",
    "    return total\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2cece240-3840-4068-9bbd-88e63f04cbe7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Path 1: ['A', 'B', 'D', 'G']\n",
      "Cost 1: 7\n",
      "Path 2: ['A', 'C', 'D', 'G']\n",
      "Cost 2: 6\n"
     ]
    }
   ],
   "source": [
    "path1 = ['A', 'B', 'D', 'G']\n",
    "path2 = ['A', 'C','D', 'G']\n",
    "\n",
    "cost1 = pathcost(path1)\n",
    "cost2 = pathcost(path2)\n",
    "\n",
    "print(\"Path 1:\", path1)\n",
    "print(\"Cost 1:\", cost1)\n",
    "\n",
    "print(\"Path 2:\", path2)\n",
    "print(\"Cost 2:\", cost2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6677b0cb-4e43-4cac-9d70-1c6fc3c13ec3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Path: ['A', 'C', 'D', 'G']\n",
      "Best Cost: 6\n"
     ]
    }
   ],
   "source": [
    "if cost1 < cost2:\n",
    "    print(\"Best Path:\", path1)\n",
    "    print(\"Best Cost:\", cost1)\n",
    "else:\n",
    "    print(\"Best Path:\", path2)\n",
    "    print(\"Best Cost:\", cost2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acf17d9b-b951-44b3-8d8b-df2e90029565",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
