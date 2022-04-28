"""base class for all enemies"""

class Enemy:
    imgs = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
        win.blit(self.img, (self.x, self.y))

    def collide(self, x, y):
        """
        Returns if position has hit enemy
        :param x:
        :param y:
        :return:
        """
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

