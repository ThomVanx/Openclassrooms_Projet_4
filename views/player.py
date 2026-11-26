class PlayerView:

    def prompt_for_player(self):
        """Prompt for name"""
        name = input("Saisissez le prénom du joueur : ")
        if not name:
            return None
        last_name = input("Saisissez le nom du joueur")
        if not last_name:
            return None

