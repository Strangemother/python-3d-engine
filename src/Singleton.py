from godot import exposed, export, Node
from godot.bindings import *


import cake

@exposed
class Singleton(Node):

    def _ready(self):
        print('Singleton _ready')

    def hi(self, to):
        return 'Single return Hello %s from Python !' % to
