class RagError(Exception):
    """Base class for all expected errors of the project."""


class InvalidArgumentError(RagError):
    """A CLI argument has an invalid value (empty query, k <= 0...)."""


class IndexNotFoundError(RagError):
    """The index is missing: the user must run the index command first."""


class DatasetError(RagError):
    """A dataset file is missing, unreadable or malformed."""


class GenerationError(RagError):
    """The language model could not be loaded or failed to generate."""
