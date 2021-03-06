"""Exercise from https://exercism.io/my/tracks/python."""


def flatten(iterable):
    """Returns a flattened list of non-list-like objects from `iterable` in DFS
    traversal order.
    """
    return list(items_from(iterable))


def items_from(iterable):
    """Genertor that yields every non-list-like objects from `iterable` in DFS
    traversal order.
    """
    # This function iterate the input `iterable` in DFS order starting from the root
    # (`iterable`) and going from the left-most item (``iterable[0]``) to the right-most
    # item (``iterable[-1]``). During traversal, two kinds of node will be met,
    # list-like (`sub_iterable`) objects and simple `item`s.
    #
    # PRE   When the traversal gets to a sub-iterable (a subtree), a new cursor is
    #       pused to `cursor_stack`.
    # IN    When a simple `item` is traversed it's yield.
    # POST  When a sub-iterable is consumed (the subtree has completely traversed),
    #       the cursor goes back to the root of the corresponding subtree.
    #
    #       iterable = [0, [1,2], 3, 4]
    #
    #                    L
    #                    |
    #           -------------------
    #           |     |     |     |
    #           0   --A--   3     4
    #               |   |
    #               1   2
    #
    # This tree contains two `sub_iterables` ('L', 'A') and five items ('0', '1', '2', '3', '4').
    cursor_stack = [iter(iterable)]
    while cursor_stack:
        sub_iterable = cursor_stack[-1]
        try:
            item = next(sub_iterable)
        except StopIteration:   # post-order
            cursor_stack.pop()
            continue
        try:                    # pre-order
            cursor_stack.append(list_like_iter(item))
        except TypeError:
            if item is not None:
                yield item      # in-order


def list_like_iter(item):
    """Returns an iterator of `item` if `item` is considered list-like (non-string iterable)"""
    if isinstance(item, str):
        raise TypeError("String are not considered list-like objects.")
    return iter(item)
