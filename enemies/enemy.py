"""base class for all enemies"""

class Enemy:
    imgs = []
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        # for collisions
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.img = None

    def draw(self, win):
        """
        Draws the enmey with the given images
        :param win:
        :return:
        """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        # reset animation
        if self.animation_count > len(self.imgs):
            self.animation_count = 0
        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param x:
        :param y:
        :return:
        """
        if X < self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return:
        """

    def hit(self):
        """
        Returns if an enemy has died and removes one health
        :return:
        """
        self.health -= 1
        if self.health <= 0:
            return True

