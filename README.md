# Github-Agent: Autonomous GPT Experiment with Github API

Github-Agent is a test application that leverages [PyGithub](https://github.com/PyGithub/PyGithub) and [Langchain autonomous agents](https://docs.langchain.com/docs/components/agents/) to perform several tasks around the Github API.

## Demo 18 Jun 2023
https://github.com/cacosandon/github-agent/assets/30879716/d93731b9-18c2-49c5-8981-6931d21cec4a

## 🧪 Features
- Search repositories by name.
- Get pull requests (PRs) and issues.
- Access the body and collaborators of specific PRs or issues.
- Comment on issues.
- Search the internet to solve issues or search for projects.

## How to use
> 🚨 **Warning**: Please exercise moderation when utilizing it as the agent is highly volatile and may engage in undesired behaviors (such as commenting multiple issues on your behalf).

1. `git clone https://github.com/cacosandon/github-agent/tree/main`

2. Fill `OPENAI_API_KEY`, `GITHUB_TOKEN` and `SERPAPI_API_KEY` (optional) in a `.env` file with your tokens.

3. Create an environment and install dependencies with `poetry shell` + `poetry install`

4. Run `python main.py`
