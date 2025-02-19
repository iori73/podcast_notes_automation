```markdown
# Podcast Notes Automation Project

This project is designed to **automatically generate notes for podcasts**. It supports processing both **Spotify URLs** and **local MP3 files**, extracting key information and creating summaries to streamline your podcast listening experience. This project can generate the basic information, a summary, a table of contents, and a transcription for a given podcast.

## Overview

This project automates the process of creating podcast notes by:

*   **Extracting podcast information**: Retrieving details such as title, description, and audio URL from Spotify.
*   **Downloading audio**: Downloading the audio file from a given URL.
*   **Converting audio**: Converting the audio file to a suitable format (MP3) if necessary.
*   **Generating transcriptions**: Transcribing the podcast audio into text.
*   **Creating summaries**: Generating concise summaries of the podcast content.

It supports two primary processing paths:

1.  **Processing from Spotify URL:** For podcasts available on Spotify, the project takes a Spotify episode URL as input and uses the Listen Notes API to download the audio file.
2.  **Processing from Local MP3 File:** For podcasts not on Spotify or manually downloaded from Listen Notes, the project processes a locally stored MP3 file directly.

## File Structure

Here's a breakdown of the project's file structure:

```
podcast_notes_automation/
├── src/                    # Source code
│   ├── main.py             # Main application (Selenium, Gemini AI setup)
│   ├── test_integration.py # Integration tests using Spotify URLs
│   ├── test_local_audio.py # Tests for local MP3 file processing
│   ├── audio_processor.py  # Audio processing class (MP4 to MP3 conversion)
│   ├── local_audio.py      # Local audio file processing
│   ├── listen_notes.py     # Listen Notes API client
│   ├── spotify.py          # Spotify API client
│   ├── summary_fm.py       # Transcription and summarization
│   ├── audio_converter.py  # Audio conversion utilities (FFmpeg)
│   ├── test_audio.py       # Tests audio conversion
│   ├── test_gemini.py      # Tests Gemini AI API
│   ├── test_summary.py     # Tests summary generation (Gemini AI)
│   ├── test_summary_fm.py  # Tests SummaryFMProcessor class
│   └── utils.py            # Utility functions (config loading)
├── downloads/              # Downloaded audio files
├── outputs/                # Generated transcriptions and summaries
├── config/                 # Configuration files
│   └── config.yaml         # API keys and settings
├── venv/                   # Python virtual environment
├── requirements.txt        # Python package dependencies
└── README.md               # This file
```

## Key Components

*   **API Clients:**
    *   `spotify.py`: Interacts with the Spotify API to retrieve podcast information.
    *   `listen_notes.py`: Uses the Listen Notes API to download audio files.
*   **Audio Processing:**
    *   `audio_processor.py`: Handles audio file conversions (e.g., MP4 to MP3).
    *   `audio_converter.py`: Provides audio conversion utilities using FFmpeg.
    *   `local_audio.py`: Manages processing of local audio files.
*   **Text Processing:**
    *   `summary_fm.py`: Handles transcription and summarization of audio.
*   **Tests:**
    *   `test_integration.py`: Tests the end-to-end process using Spotify URLs.
    *   `test_local_audio.py`: Tests the processing of local audio files.
    *   Other `test_*.py` files: Test individual components.

## Usage and Important Notes

### 1. Audio Input Methods

This project supports two methods for audio input:

*   **A) Spotify URL Processing:** Use this method for podcasts publicly available on Spotify.

    1.  Use `test_integration.py` to run the process.
    2.  Modify the `spotify_url` variable in the `test_podcast_fetch()` function.
    3.  Run `python src/test_integration.py`.
*   **B) Local MP3 File Processing:** Use this method for podcasts that aren't available on Spotify or if you have manually downloaded the MP3 file from Listen Notes.

    1.  Use `test_local_audio.py` to run the process.
    2.  Modify the `mp3_path` variable in the `test_local_audio()` function with the path to the local MP3 file.
    3.  Run `python src/test_local_audio.py`.

### 2. Setting up the project

Before running the project, there are a few things you will need to set up.

*   **A) Virtual Environments:** It's recommended to set up separate virtual environments for Spotify URL processing and local MP3 file processing. This is because there can be conflicts between the two.

    1.  For Spotify URL processing:

        ```
        python3 -m venv venv_spotify
        source venv_spotify/bin/activate
        pip install -r requirements.txt
        ```
    2.  For local audio file processing:

        ```
        python3 -m venv venv_local_audio
        source venv_local_audio/bin/activate
        pip install -r requirements.txt
        ```
*   **B) API Keys:** You'll need to obtain API keys for Spotify, Listen Notes, and Gemini AI and add them to the `config.yaml` file.

    ```yaml
    spotify:
      client_id: "your_spotify_client_id"
      client_secret: "your_spotify_client_secret"
    listen_notes:
      api_key: "your_listen_notes_api_key"
    gemini:
      api_key: "your_gemini_api_key"
    ```
*   **C) Language Settings:** The project requires manual language setting changes in two files.
    *   `listen_notes.py`: sets the language for searching episodes.

        ```python
        language = "Japanese"  # or "English"
        ```
    *   `summary_fm.py`: sets the language for transcription and summarization.

        ```python
        select.select_by_value("Japanese") # or "English"
        ```

### 3. How to change the Language Setting

*   Use the search function in your text editor.
*   Search for "Japanese" or "English".
*   Change the setting depending on the language of the podcast that you want to process.
*   Make sure that the setting has been changed in both files.

### 4. Important Notes

*   **Switching Between Processing Methods**: When switching between Spotify URL processing and local MP3 file processing, you may need to exit the terminal and rebuild the virtual environment.
*   **403 Errors**: Even if data exists on LISTEN NOTES, a 403 error may occur when creating an MD file with `python src/test_integration.py`.
*   **Separate Virtual Environments:** Due to potential conflicts, it's recommended to use separate virtual environments for `test_local_audio.py` and `test_integration.py`.
*   **API Keys**: You need to configure the API keys for Spotify, Listen Notes, and Gemini AI in the `config.yaml` file.
*   **Manual Language Setting**: Remember to manually adjust the language settings in `listen_notes.py` and `summary_fm.py` before processing.
