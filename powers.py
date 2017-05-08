from abc import ABCMeta, abstractmethod
import cmd

def PowerAction(mandatory = None, ):
    def decorator(func):
        if mandatory is None:
            mandatory = not func.__name__.startswith('do_')
        func.mandatory=mamdatory
        
    
    @abstractmethod
    @property
    def isMandatory(self):
        return False
    

class Power(cmd.Cmd):
    def __init__(self, powerlist, name):
        self.powerlist=powerlist
        self.name=name
    
    def bind(self, player):
        self.player=player
        setattr(player, 'do_'+self.name, self.onecmd) # bind a command on the player to self
        cmd.Cmd.__init__(self, player.completekey, player.stdin, player.stdout)
        self.use_rawinput=player.use_rawinput
        player._call_chain.append(self)
        self.hidden = player.server.rules.hidden_powers
    
    
