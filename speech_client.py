from google.cloud import speech
import logging

# Configure logging (optional but recommended)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger(__name__).setLevel(logging,INFO)

def initialize_speech_client():
    """Initializes and returns a Google Cloud SpeechClient.
    Handles potential errors and provides logging.
    """
    try:
        client = speech.SpeechClient()
        logging.info("Google Cloud Speech-to-Text client initialized successfully.")
        return client
    except Exception as e:
        logging.error(f"Error initializing SpeechClient: {e}")
        return None

# Example usage (within speech_client.py or another file that imports this function):
if __name__ == "__main__":  # This code runs only when the script is executed directly
    speech_client = initialize_speech_client()
    if speech_client:
        logging.info("Speed client is ready to use")
        
        # Proceed with speech-to-text operations
        # ... (Your code to use the speech_client)
        pass
