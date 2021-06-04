from godot import exposed, Spatial, Vector3

from pathlib import Path

# from . import Singleton

@exposed
class World(Spatial):
    z = 0.0

    def _ready(self):
        me = Path(__file__)
        print(f'World_py._ready: Hello from me: {me}')
        # print(Singleton.Singleton().hi('Cheese'))
        node = self.get_node('MeshInstance')
        node.rotation_degrees += Vector3(1,2,3)

    def _process(self, delta):
        self.z += 1
        node = self.get_node('MeshInstance')
        # node.rotation_degrees.z = self.z#Vector3(0,0,3)
        node.rotation_degrees += Vector3(0,0,.5)
        # print(self.z, dir(node.rotation_degrees.z))

