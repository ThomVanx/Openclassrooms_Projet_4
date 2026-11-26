"""Match"""


class Match:

    def __init__(self, player1, player2):
        self.match_result = ([player1, 0],
                             [player2, 0])

    def set_match_result(self, winner):
        if winner == self.match_result[0][0]:
            self.match_result[0][1] = 1
            self.match_result[1][1] = 0
        elif winner == self.match_result[1][0]:
            self.match_result[0][1] = 0
            self.match_result[1][1] = 1
        elif winner == "draw":
            self.match_result[0][1] = 0.5
            self.match_result[1][1] = 0.5
        else:
            raise ValueError("Résultat non valide, "
                             "le joueur entré n'existe pas dans ce match, "
                             "en cas de match nul il faut écrire 'draw'")
