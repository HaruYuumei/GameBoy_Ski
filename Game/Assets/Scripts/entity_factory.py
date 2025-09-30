from Game.Assets.Scripts.background import Background
from Game.Assets.Scripts.entity import Entity
from Game.Assets.Scripts.tree import Tree


class Entity_Factory(Entity):

    def move(self, *args, **kwargs):
        pass

    @staticmethod
    def getentity(entity_type: str, entity_position: tuple):
        match entity_type:
            case 'tree':
                local_tree = Tree(entity_type, entity_position)
                return local_tree
            case 'tree2':
                local_tree = Tree(entity_type, entity_position)
                return local_tree
            case 'game_background0':
                local_background = Background(entity_type, entity_position)
                return local_background
        return None