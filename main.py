
import vertexai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
location = os.getenv("GOOGLE_CLOUD_LOCATION")

# vertexai.init(project=project_id, location=location)
vertexai.init()

############################################################################################################


def simple():
    """ 
    basic function to invoke model, stream model
    """
    from langchain_google_vertexai import VertexAI

    model = VertexAI(model_name="gemini-2.5-pro",temperature=0.5,max_tokens=None,max_retries=6,stop=None,)

    message = "What are some of the pros and cons of Python as a programming language in one line?"

    print(model.invoke(message))
    
    # for chunk in model.stream(message):
    #     print(chunk, end="", flush=True)
    
    # await model.ainvoke(message)
def chat():
    from langchain_google_vertexai import ChatVertexAI
    model = ChatVertexAI(model_name="gemini-2.5-pro")


############################################################################################################

if __name__ == "__main__":
    simple()
        

