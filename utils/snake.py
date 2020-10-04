class Snake:

    def __init__(self, game, posx, posy):
        self.game = game
        self.pos = [[posx, posy]]
        self.vel = 1
        self.direction = None

    def update_length(self):
        if self.direction is "HORIZONTAL":
            self.pos.append([self.pos[-1][0]-self.velx, self.pos[-1][1]])
        if self.direction is "VERTICAL":
            self.pos.append([self.pos[-1][0], self.pos[-1][1]-self.vely])

    def check_collision(self):
        # Check collision with edges
        if self.pos[0][0] == 0 or self.pos[0][0] == self.game.WIN_WIDTH or self.pos[0][1] == 0 or self.pos[0][1] == self.game.WIN_HEIGHT:
            self.game.endgame()
        # Check collision with self
        if self.pos[0] in self.pos[1:]:
            self.game.endgame()
        # Check collision with fruit
        if self.pos[0] == [game.fruit.posx, game.fruit.posy]:
            self.update_length()
            self.game.new_fruit()

    def update_direction(self, direction):
        if direction == "RIGHT":
            self.direction = "HORIZONAL"
            self.vel = abs(self.vel)
        if direction == "LEFT":
            self.direction = "HORIZONAL"
            self.vel = -abs(self.vel)
        if direction == "UP":
            self.direction = "VERTICAL"
            self.vel = -abs(self.vel)
        if direction == "DOWN":
            self.direction = "VERTICAL"
            self.vel = abs(self.vel)

    def move(self):
        if self.direction == "HORIZONTAL":
            self.pos[0] = [self.pos[0][0] + vel, self.pos[0][1]]
        if self.direction == "VERTICAL":
            self.pos[0] = [self.pos[0][0], self.pos[0][1] + vel]
        for _, i in enumerate(self.pos[1:-1]):
            self.pos[i] = self.pos[i+1]
