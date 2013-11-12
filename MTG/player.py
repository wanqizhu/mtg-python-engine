class Player(object):
    hand = []
    library = []
    
    def draw():
        hand.append(library.pop())
