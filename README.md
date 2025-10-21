# AnalyserGPT

<p align="center">
  <img src="https://github.com/user-attachments/assets/b837454a-10ce-43d4-882e-36d6987d5127" alt="Image 1" width="48%">
  <img src="https://github.com/user-attachments/assets/3da7134d-f225-4c76-ba1f-52b4250e29d1" alt="Image 2" width="48%">
</p>

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

4. **Set up API Keys:**

   **For Local Development:**

   - Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
   - Or create a `.env` file in the project root
   - Add your API keys:

   ```toml
   OPENAI_API_KEY = "your-key-here"
   GEMINI_API_KEY = "your-key-here"
   OPEN_ROUTER_API_KEY = "your-key-here"
   GROQ_API_KEY = "your-key-here"
   ANTROPHIC_API_KEY = "your-key-here"
   ```

   **For Streamlit Community Cloud:**

   1. Go to your app dashboard on [share.streamlit.io](https://share.streamlit.io)
   2. Click on your deployed app
   3. Click the **⚙️ Settings** button
   4. Go to the **Secrets** section
   5. Add your API keys in TOML format:

   ```toml
   OPENAI_API_KEY = "your-key-here"
   GEMINI_API_KEY = "your-key-here"
   OPEN_ROUTER_API_KEY = "your-key-here"
   GROQ_API_KEY = "your-key-here"
   ANTROPHIC_API_KEY = "your-key-here"
   ```

   6. Click **Save**

## Usage

1. Start the Docker container:
   ```bash
   streamlit run .\streamlit-ui.py
   ```
2. Provide tasks like:
   ```
   Can you analyze the data.csv dataset, generate a graph of survived and died passengers grouped by class, and save it as output.png? Additionally, provide a summary of the survival rate for each class in a text file named summary.txt.
   ```

## File Structure

- `agents/`: Contains AI agents for data analysis and code execution.
- `config/`: Configuration files for Docker and constants.
- `models/`: Client for interacting with AI models.
- `teams/`: Team logic for coordinating tasks.
- `temp/`: Temporary files and outputs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
