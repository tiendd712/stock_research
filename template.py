import os
from pathlib import Path

list_of_paths = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.pdata_transformationy",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "notebooks/experiments.ipynb",
    "model_configs/model_configs.yaml",
    "src/data/data_seeds/",
    "src/data/data_raw/",
    "src/model_artifacts/"
]

for path in list_of_paths:
    path = Path(path)
    
    # If path is a directory (ends with slash or has no suffix), create it
    if path.suffix == "":
        path.mkdir(parents=True, exist_ok=True)
    else:
        # Otherwise, treat it as a file
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.stat().st_size == 0:
            with open(path, "w") as f:
                pass
