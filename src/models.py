import uuid
from typing import List
from pydantic import BaseModel, Field


class MinimalSource(BaseModel):
    """A location in the corpus: a file and a character range."""

    file_path: str
    first_character_index: int
    last_character_index: int


class UnansweredQuestion(BaseModel):
    """A question without an answer yet."""

    question_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question: str


class AnsweredQuestion(UnansweredQuestion):
    """A question with its ground-truth sources and answer."""

    sources: List[MinimalSource]
    answer: str


class RagDataset(BaseModel):
    """A dataset of questions, answered or not."""

    rag_questions: List[AnsweredQuestion | UnansweredQuestion]


class MinimalSearchResults(BaseModel):
    """The sources retrieved for one question."""

    question_id: str
    question: str
    retrieved_sources: List[MinimalSource]


class MinimalAnswer(MinimalSearchResults):
    """Retrieved sources plus the generated answer."""

    answer: str


class StudentSearchResults(BaseModel):
    """Output of the search_dataset command."""

    search_results: List[MinimalSearchResults]
    k: int


class StudentSearchResultsAndAnswer(BaseModel):
    """Output of the answer_dataset command."""

    search_results: List[MinimalAnswer]
    k: int


class Chunk(BaseModel):
    """A piece of a corpus file, stored in the index."""

    file_path: str
    first_character_index: int
    last_character_index: int
    text: str

    def to_source(self) -> MinimalSource:
        """Convert this chunk to the MinimalSource output format."""
        return MinimalSource(
            file_path=self.file_path,
            first_character_index=self.first_character_index,
            last_character_index=self.last_character_index,
        )
