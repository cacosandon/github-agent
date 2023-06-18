import os
from dotenv import load_dotenv

from langchain.tools import StructuredTool
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.utilities import SerpAPIWrapper

from github_agent.tools.github_tool import GithubTools

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
SERPAPI_API_KEY = os.environ.get("SERPAPI_API_KEY")

github_functions = GithubTools(token=GITHUB_TOKEN)
tools = [
    StructuredTool.from_function(
        github_functions.search_repositories, name="Search for repositories"
    ),
    StructuredTool.from_function(
        github_functions.get_repository_pull_requests, name="Get repository pull requests"
    ),
    StructuredTool.from_function(
        github_functions.get_repository_pull_request_information,
        name="Get repository pull request information",
    ),
    StructuredTool.from_function(
        github_functions.get_repository_issues, name="Get repository issues"
    ),
    StructuredTool.from_function(
        github_functions.get_repository_issue_information, name="Get repository issue information"
    ),
    StructuredTool.from_function(
        github_functions.comment_in_repository_issue, name="Comment in repository issue"
    ),
]

if SERPAPI_API_KEY:
    tools += [
        StructuredTool.from_function(SerpAPIWrapper().run, name="search"),
    ]

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0,
    streaming=True,
    verbose=True,
    model="gpt-3.5-turbo",
)

agent = initialize_agent(
    tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)


if __name__ == "__main__":
    query = input("Enter query: ")

    agent.run(query)
