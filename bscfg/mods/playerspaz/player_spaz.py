import bs
from effects import EffectSpaz as effspaz


def modify_player_spaz(self, color=(1, 1, 1), highlight=(0.5, 0.5, 0.5),
                       character="Spaz", player=None, powerupsExpire=True):
    """
    Create a spaz for the provided bs.Player.
    Note: this does not wire up any controls;
    you must call connectControlsToPlayer() to do so.
    """
    # convert None to an empty player-ref
    if player is None:
        player = bs.Player(None)

    bs.Spaz.__init__(self, color=color, highlight=highlight,
                     character=character, sourcePlayer=player,
                     startInvincible=True, powerupsExpire=powerupsExpire)
    self.lastPlayerAttackedBy = None  # FIXME - should use empty player ref
    self.lastAttackedTime = 0
    self.lastAttackedType = None
    self.heldCount = 0
    self.lastPlayerHeldBy = None  # FIXME - should use empty player ref here
    self._player = player

    effspaz.main(self.node, self.sourcePlayer)

    # grab the node for this player and wire it to follow our spaz
    # (so players' controllers know where to draw their guides, etc)
    if player.exists():
        playerNode = bs.getActivity()._getPlayerNode(player)
        self.node.connectAttr('torsoPosition', playerNode, 'position')


def main():
    bs.PlayerSpaz.__init__ = modify_player_spaz
