import sys
import pkg_resources
import subprocess
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_python_version():
    """Validate Python version"""
    required_version = (3, 8)
    current_version = sys.version_info[:2]
    
    if current_version < required_version:
        logger.error(f"Python {required_version[0]}.{required_version[1]} or higher is required")
        return False
    
    logger.info(f"Python version check passed: {sys.version}")
    return True

def check_dependencies():
    """Validate installed dependencies"""
    required_packages = [
        "fastapi",
        "uvicorn",
        "torch",
        "numpy",
        "opencv-python",
        "streamlit"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            pkg_resources.require(package)
            logger.info(f"Package {package} is installed")
        except pkg_resources.DistributionNotFound:
            missing_packages.append(package)
    
    if missing_packages:
        logger.error(f"Missing packages: {', '.join(missing_packages)}")
        return False
    
    return True

def check_directories():
    """Validate required directories"""
    required_dirs = [
        "data/videos",
        "data/frames",
        "data/embeddings",
        "data/metadata",
        "logs",
        "backend",
        "frontend"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        path = Path(dir_path)
        if not path.exists():
            missing_dirs.append(dir_path)
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {dir_path}")
    
    if missing_dirs:
        logger.warning(f"Created missing directories: {', '.join(missing_dirs)}")
    else:
        logger.info("All required directories exist")
    
    return True

def main():
    """Main validation function"""
    try:
        checks = [
            ("Python Version", check_python_version()),
            ("Dependencies", check_dependencies()),
            ("Directories", check_directories())
        ]
        
        all_passed = all(result for _, result in checks)
        
        if all_passed:
            logger.info("All validation checks passed!")
            return 0
        else:
            failed_checks = [name for name, result in checks if not result]
            logger.error(f"Validation failed for: {', '.join(failed_checks)}")
            return 1
            
    except Exception as e:
        logger.error(f"Validation failed with error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
