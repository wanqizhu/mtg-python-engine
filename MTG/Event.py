__author__ = 'Michael'


class Event(object):
    def apply(self, game):
        raise NotImplementedError()

class ZoneChangeEvent(Event):
    def __init__(self,
                 start_zone,
                 start_zone_owner,
                 final_zone,
                 final_zone_owner,
                 obj):
        self.start_zone = start_zone
        self.final_zone = final_zone
        self.obj = obj

    def apply(self, game):
        start_zone = game.get_zone(self.start_zone, self.obj.owner)
        final_zone = game.get_zone(self.final_zone, self.obj.owner)
        if start_zone.remove(self.ob):
            final_zone.add(self.obj)