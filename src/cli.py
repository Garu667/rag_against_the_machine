from tqdm import tqdm
import sys

from src.errors import RagError, InvalidArgumentError

def _check_query(query: str):
    if not str(query).strip():
        raise InvalidArgumentError("Query must be a non-empty string")

def _check_k(k: int):
    if isinstance(k, bool) or not isinstance(k, int) or k <= 0:
        raise InvalidArgumentError("k must be a positive integer")

class RagCLI:
    def index(self, max_chunk_size: int = 2000):
        ...

    def search(self, query: str, k: int = 10) -> None:
        _check_query(query)
        _check_k(k)

    def search_dataset(self, dataset_path: str, k: int, save_directory: str):
        _check_k(k)

    def answer(self, query: str, k: int = 10):
        _check_query(query)
        _check_k(k)

    def answer_dataset(self, student_search_results_path: str, save_directory: str):
        ...

    def evaluate(self, student_search_results_path: str, dataset_path: str):
        ...
