from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """ An item of interest.

    The responsibility of an Artifact is to provide score for the game.

    Attributes:
        _points (int): The score of the game.
    """
    def __init__(self):
        """ Construct a new Artifact."""

        super().__init__()
        self._points = 0
    
    def get_points(self):
        """ Gets the points.
        
        Returns:
            int: The points earned by the player.
        """
        if (self.get_text() == '*'):
            self._points = 1
        else:
            self._points = -1
        
        return self._points
    
    