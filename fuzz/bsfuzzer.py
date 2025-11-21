from thefuzz import fuzz

"""
TODO: método que reciba los dos participants, la lista de cadenas de evento y el separator.
Devuelve el mejor event_string así como el ratio obtenido para dicho resultado, que debe ser superior al ratio mínimo.
"""

class BSFuzzer:

    def __init__(self):
        pass

    @staticmethod
    def get_ratio(str1: str, str2: str) -> float:
        return fuzz.ratio(str1, str2)

    @staticmethod
    def get_partial_ratio(str1: str, str2: str) -> float:
        return fuzz.partial_ratio(str1, str2)

    @staticmethod
    def check_participant_similarity(web_participant: str, pick_participant: str, min_ratio: int = 42, min_partial_ratio: int = 85) -> bool:
        # TODO: investigar ratio Tottenham / Nottingham, que se confunden
        ratio: float = BSFuzzer.get_ratio(web_participant, pick_participant)
        partial_ratio: float = BSFuzzer.get_partial_ratio(web_participant, pick_participant)
        return ratio >= min_ratio and partial_ratio >= min_partial_ratio

    @staticmethod
    def is_valid_event_participant_list(pick_participants: list[str], web_participants: list[str], min_ratio: int = 42, min_partial_ratio: int = 64) -> bool:
        return (len(web_participants) == 2 and (BSFuzzer.check_participant_similarity(web_participants[0], pick_participants[0], min_ratio, min_partial_ratio)) and
                (BSFuzzer.check_participant_similarity(web_participants[1], pick_participants[1], min_ratio, min_partial_ratio)))

    @staticmethod
    def compute_ratio(pick_participants: list[str], search_result_event_participants: list[str], partial_ratio_factor : float = 0.65) -> float:
        home_ratio: float = BSFuzzer.get_ratio(pick_participants[0].lower(), search_result_event_participants[0].lower())
        away_ratio: float = BSFuzzer.get_ratio(pick_participants[1].lower(), search_result_event_participants[1].lower())
        home_partial_ratio: float = BSFuzzer.get_partial_ratio(pick_participants[0].lower(), search_result_event_participants[0].lower())
        away_partial_ratio: float = BSFuzzer.get_partial_ratio(pick_participants[1].lower(), search_result_event_participants[1].lower())
        computed_ratio: float = ((1.0 - partial_ratio_factor) * (home_ratio + away_ratio) / 2
                                 + partial_ratio_factor * (home_partial_ratio + away_partial_ratio) / 2)
        return min(100.0, computed_ratio)



