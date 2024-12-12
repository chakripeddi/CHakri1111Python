# AI Voice Assistant

A web-based AI-powered voice assistant application that allows users to control web applications using natural language voice commands.

## Features

- Voice Command Control
- Multi-Application Integration
- Natural Language Processing
- Web Automation
- Voice Recognition
- User Preferences Management

## Project Structure

```
├── api/
│   └── routes.py           # API endpoints
├── config/
│   └── settings.py         # Configuration settings
├── models/
│   └── database.py         # Database models
├── services/
│   ├── voice_recognition.py # Voice recognition service
│   ├── nlp_processor.py    # NLP processing service
│   └── web_automation.py   # Web automation service
├── utils/
│   └── logger.py           # Logging utility
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables in `config/settings.py`

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

1. Start the server
2. Access the API at `http://localhost:8000`
3. Use the `/process-command` endpoint to submit voice commands
4. Check the API documentation at `http://localhost:8000/docs`

## License

MIT