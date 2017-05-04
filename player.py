from .lib import telnetcmd
from .lib import phaser

class Player(telnetcmd.TelnetRequestHandler):
    def handle(self):
        while not self.server.is_shut_down:
            encounter=self.server.currentEncounter
            phase=encounter.phaser.currentPhase
            role=encounter.getRole(self)
            self.invokePowers(encounter, phase, role)
            if phase==PLANNING_SELECT and self in encounter.mainplayers:
                encounter.card[role]=self.selectCard(CardType.ENCOUNTER)
            elif phase==Phase.ALLIANCE_INVITATION and role in Role.MAIN_PLAYERS:
                players=self.selectPlayers('Invite players to your alliance')o
                
            
        
