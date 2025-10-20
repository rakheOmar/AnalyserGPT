# AnalyserGPT

AnalyserGPT is a powerful data analysis tool that leverages AI to process datasets, generate insights, and create visualizations. Designed for simplicity and efficiency, it integrates seamlessly with Docker and OpenAI models to deliver robust analysis capabilities.

## Features

- **Data Analysis**: Analyze datasets like `titanic.csv` and generate insights.
- **Visualization**: Create graphs and save them as image files.
- **Text Summaries**: Generate textual summaries of data insights.
- **Docker Integration**: Runs in a Dockerized environment for easy setup and isolation.

## Prerequisites

- Python 3.8+
- Docker
- OpenRouter/Gemini/Antrophic API Key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rakheOmar/AnalyserGPT.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AnalyserGPT
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

1. Start the Docker container:
   ```bash
   uv run main.py
   ```
2. Provide tasks like:
   ```
   Can you analyze the titanic.csv dataset, generate a graph of survived and died passengers grouped by class, and save it as output.png? Additionally, provide a summary of the survival rate for each class in a text file named summary.txt.
   ```

## File Structure

- `agents/`: Contains AI agents for data analysis and code execution.
- `config/`: Configuration files for Docker and constants.
- `models/`: Client for interacting with AI models.
- `teams/`: Team logic for coordinating tasks.
- `temp/`: Temporary files and outputs.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
