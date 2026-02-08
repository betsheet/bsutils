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
    def check_participant_similarity(web_participant: str, pick_participant: str, min_ratio: int = 42,
                                     min_partial_ratio: int = 85) -> bool:
        ratio: float = BSFuzzer.get_ratio(web_participant, pick_participant)
        partial_ratio: float = BSFuzzer.get_partial_ratio(web_participant, pick_participant)
        return ratio >= min_ratio and partial_ratio >= min_partial_ratio

    @staticmethod
    def is_valid_event_participant_list(pick_participants: list[str], web_participants: list[str],
                                        validation_threshold: float = 0.65) -> bool:

        # TODO: éste es el que se llama para buscar los eventos en black. Hay que mejorarlo. Si em ambos participants
        #  coincide una palabra lo suficientemente larga, aumentar la puntuación.
        if not len(web_participants) == 2 or not len(pick_participants) == 2:
            return False

        # analizamos similitud de home
        home_ratio: float = BSFuzzer.get_participant_ratio(pick_participants[0], web_participants[0])
        away_ratio: float = BSFuzzer.get_participant_ratio(pick_participants[1], web_participants[1])

        """
            si uno de los 2 coincide 100% le damos un bonus al whole/partial ratio.

            necesitamos un buen método de normalización de strings para evitar problemas con tildes, caracteres especiales, 
            cadenas propias de participants (W, II, Reserves, Utd...) etc.
        """
        # TODO: Exigimos que la media de ratios de ambos participants supere un umbral de validación, quizás deberíamos considerar otras métricas.
        computed_ratio: float = 0.01 * (home_ratio + away_ratio) / 2
        return computed_ratio >= validation_threshold

    @staticmethod
    def get_participant_ratio(pick_participant: str, search_result_participant: str, total_ratio_weight: float = 0.7,
                              partial_ratio_weight: float = 0.3, total_coincidence_ratio: float = 1.5) -> float:
        normalized_pick_participant: str = BSFuzzer._normalize_string(pick_participant)
        normalized_search_result: str = BSFuzzer._normalize_string(search_result_participant)

        computed_total_ratio: float = BSFuzzer.get_ratio(normalized_pick_participant, normalized_search_result)
        computed_partial_ratio: float = BSFuzzer.get_partial_ratio(normalized_pick_participant,
                                                                   normalized_search_result)

        # computar coincidencia completa (bonus)
        if normalized_pick_participant in normalized_search_result or normalized_search_result in normalized_pick_participant:
            computed_partial_ratio = min(100.0, computed_partial_ratio * total_coincidence_ratio)

        # Devolvemos una ponderación de ambos ratios, dando más peso al total ratio pero sin descartar el partial ratio
        return computed_total_ratio * total_ratio_weight + computed_partial_ratio * partial_ratio_weight

    @staticmethod
    def _normalize_string(s: str) -> str:
        # Normalizamos el string para eliminar acentos y caracteres especiales
        normalized = unicodedata.normalize('NFD', s.lower())
        return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')

    @staticmethod
    def compute_ratio(pick_participants: list[str], search_result_event_participants: list[str],
                      partial_ratio_factor: float = 0.65) -> float:
        home_ratio: float = BSFuzzer.get_ratio(pick_participants[0].lower(),
                                               search_result_event_participants[0].lower())
        away_ratio: float = BSFuzzer.get_ratio(pick_participants[1].lower(),
                                               search_result_event_participants[1].lower())
        home_partial_ratio: float = BSFuzzer.get_partial_ratio(pick_participants[0].lower(),
                                                               search_result_event_participants[0].lower())
        away_partial_ratio: float = BSFuzzer.get_partial_ratio(pick_participants[1].lower(),
                                                               search_result_event_participants[1].lower())

        computed_ratio: float = ((1.0 - partial_ratio_factor) * (home_ratio + away_ratio) / 2
                                 + partial_ratio_factor * (home_partial_ratio + away_partial_ratio) / 2)
        return min(100.0, computed_ratio)
