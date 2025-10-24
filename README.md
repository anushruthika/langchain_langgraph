# uv 
    py -m pip install uv
create a folder 
    
    cd foldername
uv is a faster modern package manager
    
    py -m uv init
    .\.venv\Scripts\Activate.ps1

this will help to add both venv and pip-tools with all langchain dependencies.
    
    py -m uv add langchain
provider:  a specific integration package for a third-party service langchain-{provider} : https://python.langchain.com/docs/integrations/providers/ 
(kept isolated so we install only required packages for openai and dont include aws or other providers)
    
    py -m uv add langchain-openai
    # to remove packages from pyproject.toml(modern version to requirements.txt including all the metadata)
    py -m uv remove langchain-openai
    # to remove it from environment itself
    py -m uv pip uninstall langchain-openai

    py -m uv add langchain-google-vertexai
    # additional packages
    py -m uv add python-dotenv black isort

to use gcloud cli, in google cloud sdk shell
    
    gcloud init
    gcloud auth application-default login
    gcloud auth application-default set-quota-project imgcp-51c5a39739fbedcd
then go to project folder cli previously used
    
    python main.py
