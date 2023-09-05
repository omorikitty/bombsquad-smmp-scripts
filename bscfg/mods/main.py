from playerspaz import player_spaz
from features import turbo_punch
from lobby import bslobby


def launcher():
    player_spaz.main()
    turbo_punch.main()
    bslobby.main()


launcher()
