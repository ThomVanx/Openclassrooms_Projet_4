"""Tournament"""


class Tournament:

    def __init__(self,
                 name: str,
                 place: str,
                 start_time,
                 end_time,
                 player_list: list,
                 description: str,
                 round_number_max: int = 4,
                 round_number_now: int = 1,
                 round_list: list = None,
                 ):
        self.name = name
        self.place = place
        self.start_time = start_time
        self.end_time = end_time
        self.player_list = player_list
        self.description = description
        self.round_number_max = round_number_max
        self.round_number_now = round_number_now
        self.round_list = round_list if round_list is not None else []
