from langchain.tools import StructuredTool
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

from github_agent.tools.github_tool import GithubTools

OPENAI_API_KEY = "your openai api key here"
GITHUB_TOKEN = "your github token here"

github_tools = GithubTools(token=GITHUB_TOKEN)

tools = [
    StructuredTool.from_function(github_tools.search_repositories),
    StructuredTool.from_function(github_tools.get_repository_pull_requests),
    StructuredTool.from_function(github_tools.get_repository_pull_request_information),
    StructuredTool.from_function(github_tools.get_repository_issues),
    StructuredTool.from_function(github_tools.get_repository_issue_information),
]

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, streaming=True, verbose=True, model="gpt-3.5-turbo")

agent = initialize_agent(
    tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)


if __name__ == "__main__":
    query = input("Enter query: ")

    agent.run(query)
