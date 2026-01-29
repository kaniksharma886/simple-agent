import os
import yaml
import pandas as pd
from langchain_openai import AzureChatOpenAI
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# --- 1. LOAD CONFIG ---
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

os.environ["AZURE_OPENAI_API_KEY"] = config['azure']['api_key']
os.environ["AZURE_OPENAI_ENDPOINT"] = config['azure']['endpoint']
os.environ["AZURE_OPENAI_API_VERSION"] = config['azure']['api_version']

# --- 2. TOOLS (Same as before) ---
@tool
def preview_csv(file_path: str) -> str:
    """Useful for seeing headers and first 3 rows of a CSV."""
    try:
        return pd.read_csv(file_path).head(3).to_string()
    except Exception as e:
        return f"Error: {str(e)}"

tools = [preview_csv]

# --- 3. INITIALIZE AGENT WITH EXTERNAL PROMPTS ---
llm = AzureChatOpenAI(
    azure_deployment=config['azure']['deployment_name'],
    temperature=0
)

# Pulling prompts from YAML
prompt = ChatPromptTemplate.from_messages([
    ("system", config['prompts']['system_message']),
    ("human", config['prompts']['human_template']),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- 4. RUN ---
target_file = config['data_sources']['default_csv']
query = f"Give me a summary of {target_file}"

response = agent_executor.invoke({"input": query})
print(response["output"])