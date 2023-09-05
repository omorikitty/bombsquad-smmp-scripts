import bs
from settings import get_setting
from prefix import PermissionEffect

settings = get_setting()
roles = settings['serverAdmin']['roles']


def main(spaz, source):
    Decorator(spaz, source)


class Decorator(object):
    def __init__(self, spaz, source):
        self.spaz = spaz
        self.source = source
        accountid = self.source.get_account_id() if isinstance(
            self.source, bs.Player) else None
        if accountid is None:
            return
        if accountid in roles['owner']:
            PermissionEffect(self.spaz, prefix='OWNER', prefixAnimate=False)
