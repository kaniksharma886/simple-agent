# 📊 Azure AI Data Agent

A configuration-driven AI agent that uses **LangChain** and **Azure OpenAI** to analyze local CSV files.

## ⚙️ Setup

1.  **Environment**: Ensure Python 3.9+ is installed.
2.  **Dependencies**:
    ```bash
    pip install langchain langchain-openai pandas pyyaml
    ```
3.  **Config**: Update `config.yaml` with your Azure API Key, Endpoint, and Deployment Name.

## 🚀 How to Run

1.  Place your data file (e.g., `sales_data.csv`) in the project folder.
2.  Run the script:
    ```bash
    python main.py
    ```

## 🛠 Features

- **Decoupled Architecture**: Prompts and settings are in YAML, not hardcoded.
- **CSV Tools**: Agent can automatically preview files and calculate statistics.
- **Traceability**: Every thought and tool call is logged to `agent_trace.log`.
