# podcast_notes_automation

This project automates the process of fetching podcast metadata, downloading episodes, transcribing audio, and generating summaries. It integrates with various services such as Spotify, Listen Notes, and [Summary.fm](http://summary.fm/) to provide a seamless workflow for podcast note-taking and summarization.

**Features**
Fetch Podcast Metadata: Retrieve metadata from Spotify, including episode title, duration, and release date.
Download Episodes: Use Listen Notes to find and download podcast episodes.
Transcribe Audio: Automatically transcribe audio files using [Summary.fm](http://summary.fm/).
Generate Summaries: Create detailed summaries and transcriptions of podcast episodes.
Language Detection and Translation: Detect the language of the podcast and translate transcriptions into English if necessary.

**Project Structure**

```
/Users/i_kawano/Documents/podcast_notes_automation/
├── src/
│   ├── test_integration.py
│   ├── summary_fm.py
│   └── ...
├── outputs/
│   ├── 【9-1】世界で最も繁栄している鳥類「ニワトリ」家畜化の真髄を観る　鶏編その1/
│   │   └── episode_summary.md
│   ├── 【9-2】資本主義が産んだ怪物ニワトリ！卵も肉も資本主義によって生まれ変わる。　鶏編その2/
│   │   └── episode_summary.md
│   └── 【9-4】卵という神秘のシステム。世界の見え方が変わる卵のあれこれ。鶏編その4/
│       └── episode_summary.md
└── README.md

```

**Files**

- src/test_integration.py: Contains the integration test for fetching podcast metadata, downloading episodes, and processing audio.
- src/summary_fm.py: Handles the transcription and summarization of audio files using [Summary.fm](http://summary.fm/).
- outputs/: Directory containing the generated summaries and transcriptions for each podcast episode.

**How to Use**

1. Setup: Ensure you have the necessary API keys and credentials for Spotify, Listen Notes, and [Summary.fm](http://summary.fm/). Configure these in the config.yaml file.
2. Run Integration Test: Execute src/test_integration.py to fetch metadata, download episodes, and process audio.
3. View Outputs: Check the outputs/ directory for the generated summaries and transcriptions.

**Example Usage**

```jsx
# Navigate to the project directory
cd /Users/i_kawano/Documents/podcast_notes_automation/

# Run the integration test
python src/test_integration.py

# Check the outputs
ls outputs/
```

**Dependencies**

- `selenium`
- `webdriver_manager`
- `google.generativeai`
- `pandas`
- `requests`

**Configuration**

Ensure you have a config.yaml file with the following structure:

```jsx
gemini:
  api_key: "your_gemini_api_key"
spotify:
  client_id: "your_spotify_client_id"
  client_secret: "your_spotify_client_secret"
listen_notes:
  api_key: "your_listen_notes_api_key"
```

**Contributing**

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

**License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.