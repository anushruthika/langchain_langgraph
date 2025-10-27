
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

def prompt_template_func():
    from langchain_core.prompts import PromptTemplate
    from langchain_google_vertexai import ChatVertexAI

    og_inp="Tell me a joke about {topic}"
    # prompt_template = PromptTemplate.from_template(og_inp)
    # prompt_template.invoke({"topic": "cats"})
    about="cat"

    summary_prompt_template = PromptTemplate(
        input_variables=["topic"], template=og_inp
    )
    model = ChatVertexAI(model_name="gemini-2.5-pro",temperature=1)
    # llm = ChatOllama(temperature=0, model="gemma3:270m")
    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | model

    response = chain.invoke(input={"topic": about})
    print(response.content)
    pass
############################################################################################################

if __name__ == "__main__":
    # simple()
    prompt_template_func()
        

