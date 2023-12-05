#!/usr/bin/python3

"""
Module for the canUnlockAll function to determine if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list of lists where each inner list represents
                             a box. Each box may contain keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 0:
        return False

    keys = [0]  # Start with the keys from box 0
    visited = set()  # To keep track of visited boxes

    while keys:
        box = keys.pop()
        if box not in visited:
            visited.add(box)
            keys.extend(boxes[box])

    return len(visited) == len(boxes)
