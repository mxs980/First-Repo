from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, Filter
from chat_pdf.modules.pdf_data_model import PDFData
from chat_pdf.modules.vectorizer import Vectorizer

class QdrantManager:
    """
    Class responsible for communication with Qdrant to insert and retrieve PDF data.
    """
    
    def __init__(self, host='localhost', port=6333, collection_name='chat_pdf_data'):
        self.client = QdrantClient(host=host, port=port)
        self.collection_name = collection_name
        self.vectorizer = Vectorizer()

    def create_collection(self):
        """Create a new collection in Qdrant DB for storing PDF data."""
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vector_size=len(self.vectorizer.fit_texts(["Sample text to initialize vectorizer"])),
            distance="Cosine"
        )

    def store_pdf_data(self, pdf_data: PDFData):
        """
        Store PDF data as a vector in Qdrant.
        
        :param pdf_data: a Pydantic model instance representing the PDF data.
        """
        vectors = self.vectorizer.fit_transform([pdf_data.text]).tolist() // INPUT_REQUIRED {Provide the text attribute of PDFData which holds actual text content}
        pdf_data.text_vectors = vectors[0]
        point = PointStruct(
            id=None,
            vector=pdf_data.text_vectors,
            payload=pdf_data.dict(exclude={"text_vectors"})
        )
        self.client.upsert_points(self.collection_name, [point])

    def search_pdf_data(self, query: str, limit: int = 10):
        """
        Search and retrieve PDF data from Qdrant by a given query.

        :param query: a string query to search by.
        :param limit: the number of results to return.
        """
        vector = self.vectorizer.transform_text(query)
        
        search_results = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            filter=None,
            limit=limit
        )
        
        return search_results
