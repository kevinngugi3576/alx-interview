#!/usr/bin/python3`
def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    keys = [0]
    for k in keys:
        for key in boxes[k]:
            if key not in keys:
                if key < len(boxes):
                    keys.append(key)

    if len(keys) == len(boxes):
        return True
    return False
