class Rectangle:
    def __init__(self, x, y, w, h):
        self.ul = (x, y)
        self.ud = (x, y + h)
        self.dr = (x + w, y + h)
        self.ur = (x + w, y)


D = [[l.split()] for l in open("input/3.in").read().splitlines()]
