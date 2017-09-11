from enum import Enum
import random

from MTG import gameobject
from MTG import cards
from MTG import card
from MTG import permanent
from MTG import triggers


class ZoneType(Enum):
    LIBRARY = 0
    HAND = 1
    BATTLEFIELD = 2
    GRAVEYARD = 3
    STACK = 4
    EXILE = 5
    # COMMAND = 6


class Zone():
    is_library = False
    is_battlefield = False

    def __init__(self, controller=None, elements: list=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = elements
            for ele in elements:
                ele.controller = controller
        self.controller = controller
        if controller:
            self.game = self.controller.game

    def __repr__(self):
        return 'zone.Zone %r controlled by %r len=%s\n%r' % (self.__class__.__name__,
                                                             self.controller, len(self), self.elements)

    def __str__(self):
        return '%s\'s %s (%s cards)\n%s' % (self.controller, 
                                            self.__class__.__name__,
                                            len(self), 
                                            [ele.name for ele in self.elements])


    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return bool(self.elements)

    def __getitem__(self, pos):
        return self.elements[pos]

    def add(self, obj):
        if type(obj) is str:  # convert string (card's name) to a Card object
            obj = cards.card_from_name(obj)

        if type(obj) is list:
            for o in obj:
                o.zone = self
                if not isinstance(self, Stack):
                    assert isinstance(o, gameobject.GameObject)
                o.controller = self.controller
            self.elements.extend(obj)
            return obj

        if not isinstance(self, Stack):
            assert isinstance(obj, gameobject.GameObject)
            obj.controller = self.controller
            obj.game = self.controller.game

        obj.zone = self
        self.elements.append(obj)
        return obj

    def remove(self, obj):
        if type(obj) is list:
            return all([self.remove(o) for o in obj])

        try:
            self.elements.remove(obj)
            obj.zone = None
            return True
        except ValueError:
            return False

    def filter(self, characteristics=None, filter_func=None):
        found = set()
        if filter_func:
            for ele in self:
                if filter_func(ele):
                    found.add(ele)

        else:
            assert (characteristics is None
                    or isinstance(characteristics, gameobject.Characteristics))

            for ele in self:
                if ele.characteristics.satisfy(characteristics):
                    found.add(ele)

        return found

    def count(self, characteristics=None, filter_func=None):
        return len(self.filter(characteristics, filter_func))

    def get_card_by_name(self, name):
        cards = self.filter(gameobject.Characteristics(name=name))
        if cards:
            return list(cards)[0]
        else:
            return None

    def pop(self, pos=-1):
        return self.elements.pop(pos)


class Battlefield(Zone):
    zone_type = 'BATTLEFIELD'
    is_battlefield = True

    def add(self, obj):
        if type(obj) is str:  # convert string (card's name) to a Card object
            obj = cards.card_from_name(obj)
        obj.controller = self.controller

        if isinstance(obj, card.Card):  # convert card to Permanent
            obj = permanent.make_permanent(obj)  # this will call Battlefield.add(...) again
        else:
            obj.zone = self
            self.elements.append(obj)
            obj.status = permanent.Status()  # reset status upon entering battlefield
            obj.trigger('onEtB', obj)
            obj.controller.trigger('onControllerPermanentEtB', obj)
            obj.game.trigger('onPermanentEtB', obj)
            if obj.is_creature:
                obj.controller.trigger('onControllerCreatureEtB', obj)
                obj.game.trigger('onCreatureEtB', obj)


class Stack(Zone):
    zone_type = 'STACK'
    pass


class Hand(Zone):
    zone_type = 'HAND'
    pass


class Graveyard(Zone):
    zone_type = 'GRAVEYARD'
    pass


class Exile(Zone):
    zone_type = 'EXILE'
    pass


class Library(Zone):
    zone_type = 'LIBRARY'
    is_library = True

    def shuffle(self):
        random.shuffle(self.elements)

    def __init__(self, controller=None, elements: list=None):
        super(Library, self).__init__(controller, elements)
        for ele in self.elements:
            ele.zone = self
        self.shuffle()


    def add(self, obj, from_top=0, shuffle=True):
        """ Note: the library is reversed; i.e. self.elements[0] is the last card

        When you draw, you draw from self.pop(), or self.elements[-1]
        """
        assert isinstance(obj, gameobject.GameObject)
        obj.controller = self.controller
        obj.game = self.controller.game
        obj.zone = self

        if from_top == 0:
            self.elements.append(obj)
        elif from_top == -1:  # put on bottom
            self.elements = [obj] + self.elements
        else:
            self.elements = self.elements[:-from_top] + [obj] + self.elements[-from_top:]

        if shuffle:
            self.shuffle()

        return obj

    def remove(self, obj):
        super(Battlefield, self).remove(self, obj)


