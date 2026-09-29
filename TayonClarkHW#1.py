from collections import deque


def BFS_Search(start_1, goal_11):
    queue = deque([(start_1, [start_1])])
    Order_expand = []

    while queue:
        position, path = queue.popleft()
        Order_expand.append(position)

        if position == goal_11:
            return path, Order_expand
        lft_chl = 2 * position
        rht_chl = 2 * position + 1
        queue.append((lft_chl, path + [lft_chl]))
        queue.append((rht_chl, path + [rht_chl]))
    return None, Order_expand

Start = 1
Goal = 11

shortest_path, Order = BFS_Search(Start, Goal)

print(f"{Order}")
print(f" {Goal}: {shortest_path}")

