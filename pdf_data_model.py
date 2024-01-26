from pydantic import BaseModel
from typing import List


class PDFData(BaseModel):
    """
    Pydantic model representing the structure of the PDF data for vector insertion to Qdrant.
    Includes the document text as a field used for search and pdf name and path as payload.
    """
    text_vectors: List[float]
    name: str
    path: str
