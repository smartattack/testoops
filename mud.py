"""
Test MUD oop idea
"""

from player import Player
from location import Location
from log import Log

class Mud():
    """This is where the magic happens
    Rather than having globals for all the game object lists,
    embed them here.  Let's see if we can call them from 
    inside other classes"""

    def __init__(self):
        """Set up containers for lists"""
        self.log = Log()
        self.players = []
        self.locations = []
        self.log('Initializing Mud')
        self.server = Server()
        """
        player = Player('testplayer1')
        player._mud = self
        self.players.append(Player('testplayer1'))
        self.locations.append(Location('room A'))
        """

    def start(self):
        """Start the game"""
        self.log.info('Start() called')
        self.server.start()



