from pathlib import Path
import logging

# ----------------------------
# Logging Configuration
# ----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("file_creation.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ----------------------------
# Define Files to Create
# ----------------------------
PROJECT_NAME = "medical-Chatbot"

files_to_create = [
    
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/experiment.ipynb",
    "test.py"
]

# ----------------------------
# Function to Create Files
# ----------------------------
def create_files(base_path: Path):
    """Create project files (and parent folders if they don't exist)."""
    project_root = base_path / PROJECT_NAME
    project_root.mkdir(parents=True, exist_ok=True)
    logger.info(f"Project root: {project_root}")

    for file_path in files_to_create:
        path = project_root / file_path
        try:
            # Create parent directories automatically
            path.parent.mkdir(parents=True, exist_ok=True)

            # Create the file if not exists
            if not path.exists():
                path.touch()
                logger.info(f"Created file: {path}")
            else:
                logger.warning(f"File already exists: {path}")
        except Exception as e:
            logger.error(f"Error creating file {path}: {e}")

    logger.info(" All files created successfully.")


# ----------------------------
# Run the Script
# ----------------------------
if __name__ == "__main__":
    base_dir = Path.cwd()  # You can also set your path manually
    create_files(base_dir)
