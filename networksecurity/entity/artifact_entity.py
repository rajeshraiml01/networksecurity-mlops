from dataclasses import dataclass   # acts as a decorator to automatically add special methods to classes

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str
    #feature_store_file_path: str
    #is_ingested: bool = False
    #message: str = None

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str