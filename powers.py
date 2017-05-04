from abc import ABCMeta, abstractmethod
import cmd

class PowerAction(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, terminalArg):
        pass
    
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
    
    
