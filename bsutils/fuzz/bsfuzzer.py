from thefuzz import fuzz
import unicodedata

"""
TODO: método que reciba los dos participants, la lista de cadenas de evento y el separator.
Devuelve el mejor event_string así como el ratio obtenido para dicho resultado, que debe ser superior al ratio mínimo.
"""

class BSFuzzer:

    # TODO: distinguir métodos públicos y privados

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
    def _is_valid_event_participant_list(pick_participants: list[str], web_participants: list[str], min_ratio: int = 42, min_partial_ratio: int = 64) -> bool:

        # TODO: éste es el que se llama para buscar los eventos en black. Hay que mejorarlo. Si em ambos participants
        #  coincide una palabra lo suficientemente larga, aumentar la puntuación.


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

    @staticmethod
    def is_valid_event_participant_list(
            pick_participants: list[str],
            web_participants: list[str],
            min_ratio: int = 42,
            min_partial_ratio: int = 64
    ) -> bool:
        if len(web_participants) != 2 or len(pick_participants) != 2:
            return False

        # Normalizar
        pick_norm = [BSFuzzer._normalized_participant_string(p) for p in pick_participants]
        web_norm = [BSFuzzer._normalized_participant_string(p) for p in web_participants]

        # Ratios para cada participante
        ratios = [
            max(fuzz.ratio(pick_norm[i], web_norm[i]),
                fuzz.token_set_ratio(pick_norm[i], web_norm[i]))
            for i in range(2)
        ]

        partial_ratios = [
            fuzz.partial_ratio(pick_norm[i], web_norm[i])
            for i in range(2)
        ]

        # Bonus por palabras comunes
        common_words = sum(len(BSFuzzer._get_common_words(pick_norm[i], web_norm[i]))
                           for i in range(2))
        common_bonus = common_words * 5

        # Promedios (sin ponderar)
        avg_ratio = sum(ratios) / 2 + common_bonus
        avg_partial = sum(partial_ratios) / 2

        return avg_ratio >= min_ratio and avg_partial >= min_partial_ratio


    @staticmethod
    def _normalized_participant_string(participant: str) -> str:
         name = ''.join(c for c in unicodedata.normalize('NFD', participant)
                        if unicodedata.category(c) != 'Mn')
         # Normalizar abreviaturas comunes
         replacements = {
             ' fc': '', ' cf': '', ' cd': '', ' sd': '',
             ' united': ' utd', ' football club': '',
             ' athletic': ' ath', ' atletico': ' atl',
             ' deportivo': ' dep', ' real': '',
             ' club': '', ' de': '', ' del': '',
             ' sporting': ' sp', '
         }

         name_lower = name.lower()
         for old, new in replacements.items():
             name_lower = name_lower.replace(old, new)
         return name_lower.strip()

    @staticmethod
    def _get_common_words(str1: str, str2: str, min_length: int = 4) -> list[str]:
        """Encuentra palabras comunes significativas"""
        words1 = set(word for word in str1.lower().split() if len(word) >= min_length)
        words2 = set(word for word in str2.lower().split() if len(word) >= min_length)
        return list(words1 & words2)