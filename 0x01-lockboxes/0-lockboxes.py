#!/usr/bin/env python3
""" Lockbox Problem. """


def canUnlockAll(boxes):
    """ check if all boxes could open. """
    if len(boxes) == 0:
        return True
    else:
        # make opened boxes unique and preserve order
        openedBoxes = []
        [openedBoxes.append(box) for box in boxes[0] if box not in openedBoxes]
        idx = 0
        nextIdx = len(openedBoxes)
        new = not(nextIdx == idx)
        # loop while new box opened
        while new:
            newOpened = []
            [newOpened.append(boxes[key]) for key in openedBoxes[idx:]
             if key < len(boxes)]
            # flatten list
            newOpened = sum(newOpened, [])
            # concatnate only new opened boxes
            [openedBoxes.append(box) for box in newOpened
             if box not in openedBoxes]
            idx = nextIdx
            nextIdx = len(openedBoxes)
            # check if new box opened
            new = not(nextIdx == idx)

    return all(box in openedBoxes for box in list(range(1, len(boxes))))
