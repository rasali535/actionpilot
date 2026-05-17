import os
import asyncio
import sys
from dotenv import load_dotenv

# Add parent directory to path so we can import backend packages
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

from agents.transcription import SpeechmaticsAgent

async def main():
    print("Testing SpeechmaticsAgent...")
    api_key = os.getenv("SPEECHMATICS_API_KEY")
    print(f"Loaded Speechmatics API Key: {api_key}")
    
    agent = SpeechmaticsAgent()
    
    dummy_wav_path = "scratch/dummy_test.wav"
    # A valid WAV header + 2000 bytes of silent PCM samples
    wav_header = (
        b"RIFF\xf4\x07\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00"
        b"\x22\x56\x00\x00\x44\xac\x00\x00\x02\x00\x10\x00data\xd0\x07\x00\x00"
        + b"\x00" * 2000
    )
    with open(dummy_wav_path, "wb") as f:
        f.write(wav_header)
        
    print(f"Created a dummy WAV file at {dummy_wav_path}")
    
    try:
        print("Submitting to Speechmatics ASR API...")
        result = await agent.transcribe(dummy_wav_path)
        print("\n--- Transcription Result ---")
        print(result)
        print("----------------------------\n")
    except Exception as e:
        print(f"Error during transcription: {e}")
    finally:
        if os.path.exists(dummy_wav_path):
            os.remove(dummy_wav_path)

if __name__ == "__main__":
    asyncio.run(main())
