from openai import AzureOpenAI
import streamlit as st


chat_engine = st.secrets["AZURE_OPENAI_CHAT_DEPLOYMENT"]


client = AzureOpenAI(
  api_key = st.secrets["AZURE_OPENAI_API_KEY"],  
  api_version = st.secrets["AZURE_OPENAI_API_VERSION"],
  azure_endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]
)

PERSONA = """
I have a keyframe query that have QA question (or not). 
The first part of the query is the description to query frame and the rest is the QA question about the frame (include question maek). 
Please extract the two part from the input query. Make sure that you just extract, do not infer, summary or do any extra function and the whole meaning unchnaged. 
If you cannot extract the questions, leave it empty string
Output in JSON format
{
"description": "the description extracted",
"question": "the question extracted"
}
"""

class Agent:
    def __init__(self) -> None:
        self.conversation = [{'role': 'system', 'content': PERSONA}]
    
    def run(self, input: str) -> str:
        if len(self.conversation) < 2:
            self.conversation.append({"role": "user", "content": input})
        else:
            self.conversation[1]['user'] = input

        response = client.chat.completions.create(
            model=chat_engine,
            messages=self.conversation
        )
        
        return response.choices[0].message.content