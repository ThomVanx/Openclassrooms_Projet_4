"""Round"""


class Round:

    def __init__(self,
                 round_number: int,
                 start_time: str,
                 end_time: str,
                 match_list: list):
        self.round_number = round_number
        self.start_time = start_time
        self.end_time = end_time
        self.match_list = match_list
