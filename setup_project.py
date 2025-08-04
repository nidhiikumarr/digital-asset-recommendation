import subprocess
import sys
import venv
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_project_structure():
    """Create project directory structure"""
    try:
        # Define directories to create
        directories = [
            "backend",
            "backend/utils",
            "data/vector_store",
            "data/videos",
            "data/frames",
            "logs"
        ]
        
        # Create directories
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            
        # Create __init__.py files
        init_files = [
            "backend/__init__.py",
            "backend/utils/__init__.py"
        ]
        
        for init_file in init_files:
            Path(init_file).touch(exist_ok=True)
            
        logger.info("Project structure created successfully")
        
    except Exception as e:
        logger.error(f"Failed to create project structure: {e}")
        raise

if __name__ == "__main__":
    create_project_structure()
