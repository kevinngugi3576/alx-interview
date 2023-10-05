 #!/usr/bin/python3`
def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # Keep track of visited boxes
    visited[0] = True  # Start with the first box unlocked
    stack = [0]  # Stack to keep track of boxes to visit

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes are visited
    return all(visited)

# Example usage
boxes1 = [[1], [2], [3], [4], []]
boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

print(canUnlockAll(boxes1))  
print(canUnlockAll(boxes2))  
print(canUnlockAll(boxes3))  

