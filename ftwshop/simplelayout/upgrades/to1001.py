from ftw.upgrade import UpgradeStep


class AddBlockAction(UpgradeStep):

    def __call__(self):
        self.setup_install_profile(
            'profile-ftwshop.simplelayout.upgrades:1001')
