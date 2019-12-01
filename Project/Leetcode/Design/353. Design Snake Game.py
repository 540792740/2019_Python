import collections
class snakeGame(object):
    # Space O(n)
    def __init__(self, width, height, food):
        self.width, self.height = width, height
        self.food = collections.deque(food)
        o_pos = (0, 0)
        self.snake_pos = set([o_pos])
        self.snake = collections.deque([o_pos])
        self.direction = {'U':(-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def move(self, direction):
        # Space O(1)
        # Time O(1)
        head = self.snake[0]
        next_pos = (head[0] + self.direction[direction][0], head[1] + self.direction[direction][1])

        # Remove tail, since move to direction
        tail = self.snake.pop()
        self.snake_pos.remove(tail)

        # next position cannot be snake itself or out the range.
        if next_pos in self.snake_pos or not (0 <= next_pos[1] < self.width and 0 <= next_pos[0] < self.height):
            return -1

        # Food position, popleft()
        cur_food = (-1, -1)
        if len(self.food) > 0:
            cur_food = tuple(self.food[0])

        self.snake.appendleft(next_pos)
        self.snake_pos.add(next_pos)

        # When snake ate the food, add tail into snake[]
        if cur_food == next_pos:
            self.food.popleft()
            self.snake.append(tail)
            self.snake_pos.add(tail)

        # Return length of snake
        return len(self.snake) - 1



if __name__ == '__main__':
    S = snakeGame(3,2,[[1,2],[0,1]])
    S.move("R")
    S.move("D")
    S.move("R")
    S.move("U")
    S.move("L")
    S.move("U")
