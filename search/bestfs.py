from search._node import Node
import heapq


def best_first_search(start_node: Node):
    prev_marble_count = start_node.board.num_marbles

    # keep track of all the visited states ie Board
    closed = set()
    # queue to store all the states that haven't been visited
    open = []
    heapq.heappush(open, start_node)
    open_set = set([start_node.board])

    while len(open) != 0:
        parent = heapq.heappop(open)
        open_set.discard(parent.board)
        # remove from the head
        if parent.board.goal_test() is True:
            return parent.back_track()
        else:
            if prev_marble_count > parent.board.num_marbles:
                prev_marble_count = parent.board.num_marbles
                print(f"Marbles left: {parent.board.num_marbles}")

            closed.add(parent.board)
            children = parent.board.move_gen()
            # removing already visited states
            children = [
                child
                for child in children
                if child not in closed and child not in open_set
            ]
            for child in children:
                heapq.heappush(open, Node(child, parent))
                open_set.add(child)

    return None


def stepped_best_first_search(node: Node, open: list[Node] | None, open_set: set | None, closed: set):

    if open is None and open_set is None:
        open = []
        heapq.heappush(open, node)
        open_set = set([node.board])

    parent = heapq.heappop(open)
    open_set.discard(parent.board)

    if parent.board.goal_test():
        return True, parent, open, open_set, closed
    else:

        closed.add(parent.board)
        children: list = parent.board.move_gen()

        children = [child for child in children if child not in closed and child not in open_set]
        
        for child in children:
            heapq.heappush(open, Node(child, parent))
            open_set.add(child)

        return False, parent, open, open_set, closed
