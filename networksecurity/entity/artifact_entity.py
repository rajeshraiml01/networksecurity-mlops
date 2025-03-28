from dataclasses import dataclass   # acts as a decorator to automatically add special methods to classes

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str
    #feature_store_file_path: str
    #is_ingested: bool = False
    #message: str = None