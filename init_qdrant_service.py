from chat_pdf.modules.qdrant_manager import QdrantManager

# Initialize Qdrant service manager
qdrant_manager = QdrantManager()
qdrant_manager.create_collection()
