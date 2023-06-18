# Github-Agent: Autonomous GPT Experiment with Github API

Github-Agent is a test application that leverages [PyGithub](https://github.com/PyGithub/PyGithub) and [Langchain autonomous agents](https://docs.langchain.com/docs/components/agents/) to perform several tasks around the Github API.

## Demo 18 Jun 2023
https://github.com/cacosandon/github-agent/assets/30879716/1826b053-5eee-4208-aa9d-9ec73dc3fc56



## 🧪 Features
- Search repositories by name
- Get pull requests (PRs) and issues
- Access the body and collaborators of specific PRs or issues.

## How to use
1. `git clone https://github.com/cacosandon/github-agent/tree/main`

2. Fill `OPENAI_API_KEY` and `GITHUB_TOKEN` (optional) in `main.py` with your tokens. Github token is not necessary. Adding your Github token allows you to increase the API limit rate and also give access to your repositories.

3. Create an environment and install dependencies with `poetry shell` + `poetry install`

4. Run `python main.py`
