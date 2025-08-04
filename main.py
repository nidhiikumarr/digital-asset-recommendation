import logging
from speech_client import initialize_speech_client  # Import the function

# Configure logging in your main script as well
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    speech_client = initialize_speech_client()
    if speech_client:

        pass
    else:
        logging.error("Could not initialize speech client. Exiting.")
