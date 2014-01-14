__author__ = 'Michael'

class OneShotEffect(object):
    def __init__(self, *targets):
        self.targets = targets

    def resolve(self, controller):
        raise NotImplementedError()

class DrawEffect(OneShotEffect):
    def resolve(self, controller):
        for target in self.targets[0]:
            try:
                target.draw()
            except AttributeError:
                raise ValueError("Targets for draw effects must be players")

class SequenceEffect(OneShotEffect, list):
    def resolve(self, controller):
        for (effect, target) in zip(self, self.targets):
            effect.resolve(controller, target)