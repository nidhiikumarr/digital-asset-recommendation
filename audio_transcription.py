from google.cloud import speech
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transcribe_audio(audio_file, language_code="en-US", sample_rate_hertz=44100):
    """Transcribes audio from a file using Google Cloud Speech-to-Text."""
    try:
        client = speech.SpeechClient()

        with open(audio_file, "rb") as f:
            content = f.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # Or other encoding
            sample_rate_hertz=sample_rate_hertz, 
            language_code=language_code,
        )
        

        response = client.recognize(config=config, audio=audio)
        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript
        logging.info(f"Transcribed audio: {transcript}") # Log the transcript
        return transcript

    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        return None

# Example usage:
audio_file_path = "path/to/your/audio.wav"  # Replace with your audio file path
transcript = transcribe_audio(audio_file_path)
if transcript:
    # Process the transcript
    pass
else:
    Logging.error("failure in transcribing audio")
    # Handle 