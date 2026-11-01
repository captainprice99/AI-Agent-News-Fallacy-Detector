# AI-Powered News Fallacy Detector

This is a platform that identifies logical fallacies in news articles using LangChain and Retrieval Augmented Generation (RAG). It helps users critically evaluate news content by detecting potential biases, misleading arguments, and logical inconsistencies.

## Features

- **Automated News Analysis**: Scans and analyzes news articles for logical fallacies
- **Comprehensive Fallacy Detection**: Identifies various types of logical fallacies using a knowledge base
- **Two-Stage Analysis**: 
  1. Summarizes news articles concisely
  2. Analyzes content for logical inconsistencies and biases
- **Web Integration**: Fetches relevant news articles using SerperAPI
- **Customizable Fallacy Database**: Easy to update and expand the types of fallacies detected

## Prerequisites

- Python 3.8+
- OpenAI API key
- Serper API key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI-Agent-News-Fallacy-Detector
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

By default, the script will search for news articles about "european policy" and analyze them for logical fallacies.

### Customization

To analyze different topics, modify the `topic` variable in `main.py`:

```python
topic = "your_topic_here"
```

## Project Structure

```
BotCatcher/
├── chains/                  # LangChain processing pipelines
│   ├── chain1_summary.py    # First stage: Article summarization
│   └── chain2_review.py     # Second stage: Fallacy detection
├── config/
│   └── settings.py          # Configuration and API keys
├── data/
│   └── fallacies.csv        # Database of logical fallacies
├── prompts/                 # LLM prompt templates
│   ├── prompt1.py           # Summary generation prompt
│   └── prompt2.py           # Fallacy analysis prompt
├── utils/
│   ├── loader.py            # Article content loading
│   └── search.py            # News search functionality
├── .env.example             # Example environment variables
├── .gitignore
├── main.py                  # Main application script
├── README.md
└── requirements.txt         # Python dependencies
```

## How It Works

1. **Article Retrieval**: The system searches for relevant news articles using SerperAPI
2. **Content Loading**: Article content is extracted and cleaned
3. **Summarization**: The first LLM chain generates a concise summary of the article
4. **Fallacy Analysis**: The second LLM chain analyzes the summary for logical fallacies
5. **Results Presentation**: The system presents the analysis, highlighting potential fallacies

## Future Enhancements

- [ ] Web interface for easier interaction
- [ ] Support for multiple articles in batch processing
- [ ] More detailed fallacy explanations with examples
- [ ] Sentiment analysis integration
- [ ] Historical analysis of news sources
- [ ] Browser extension for real-time analysis
- [ ] User authentication to save analysis history
- [ ] API endpoint for integration with other services

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
