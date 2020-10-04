class Snake:

    def __init__(self, game, posx, posy):
        self.game = game
        self.pos = [[posx, posy]]
        self.vel = 1
        self.direction = "HORIZONTAL"

    def update_length(self):
        if self.direction == "HORIZONTAL":
            self.pos.append([5, 5])
        if self.direction == "VERTICAL":
            self.pos.append([5, 5])

    def check_collision(self):
        # Check collision with edges
        if self.pos[0][0] == 0 or self.pos[0][0] == self.game.WIN_WIDTH or self.pos[0][1] == 0 or self.pos[0][1] == self.game.WIN_HEIGHT:
            print("Score is ", len(self.pos))
            return self.game.endgame()
        # Check collision with self
        if self.pos[0] in self.pos[1:]:
            print("Score is ", len(self.pos))
            return self.game.endgame()
        # Check collision with fruit
        if self.pos[0] == [self.game.fruit.posx, self.game.fruit.posy]:
            # print("Collided with fruit")
            self.update_length()
            self.game.new_fruit()

    def update_direction(self, direction):
        if direction == "RIGHT":
            self.direction = "HORIZONTAL"
            self.vel = abs(self.vel)
        if direction == "LEFT":
            self.direction = "HORIZONTAL"
            self.vel = -abs(self.vel)
        if direction == "UP":
            self.direction = "VERTICAL"
            self.vel = -abs(self.vel)
        if direction == "DOWN":
            self.direction = "VERTICAL"
            self.vel = abs(self.vel)

    def move(self):
        for i in range(1, len(self.pos)):
            self.pos[-i] = self.pos[-i-1]
        if self.direction == "HORIZONTAL":
            self.pos[0] = [self.pos[0][0] + self.vel, self.pos[0][1]]
        if self.direction == "VERTICAL":
            self.pos[0] = [self.pos[0][0], self.pos[0][1] + self.vel]
