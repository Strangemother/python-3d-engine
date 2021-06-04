from godot import exposed, export, Node
from godot.bindings import *


import cake

@exposed
class autoload(Node):

    def _ready(self):
        print('autoload _ready')

    def hi(self, to):
        return 'autoload_py.hi: Hello %s from Python !' % to
