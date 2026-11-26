"""Player"""


class Player:

    def __init__(self,
                 last_name: str,
                 first_name: str,
                 birth_date: str,
                 national_chess_id: str,
                 ):
        """Has a last and first name, a birth date and a national chess id"""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_chess_id = national_chess_id
