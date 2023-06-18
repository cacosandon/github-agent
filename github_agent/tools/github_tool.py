from typing import List, Literal

from github import Github
from github.Repository import Repository
from github.PullRequest import PullRequest
from github.GithubException import UnknownObjectException


class GithubTools:
    """
    Multiple tools provided by Github client.
    """

    def __init__(self, token: str) -> None:
        self.github_service = Github(login_or_token=token)

    def search_repositories(
        self, query: str, sort: Literal["stars", "forks"] = "stars", order: str = "desc"
    ) -> List[Repository]:
        """
        A tool to search Github repositories by name and sorted by params.
        Returns list of max 5 repositories with the exact names.
        Useful for getting the exact repository name and then obtaining pull requests, issues, etc.
        """
        repositories = self.github_service.search_repositories(query=query, sort=sort, order=order)

        return repositories.get_page(0)[:5]

    def get_repository_pull_requests(
        self,
        repository_name: str,
        state: str,
        sort: str = "created",
        direction: str = "desc",
    ) -> List[PullRequest] | str:
        """
        A tool to search Github pull requests by repository name, state and sorted by params.
        Returns list of max 10 pull requests.
        """

        try:
            repository = self.github_service.get_repo(repository_name)
        except UnknownObjectException:
            return "Repository not found. Please use the exact name."

        return (
            f"The pull requests of the repository {repository_name} are: "
            f"{repository.get_pulls(state=state, sort=sort, direction=direction).get_page(0)[:10]}"
        )

    def get_repository_pull_request_information(
        self, repository_name: str, pull_request_number: int
    ) -> str:
        """
        A tool to search Github pull request information by repository name and pull request number.
        Returns pull request information.
        """

        try:
            repository = self.github_service.get_repo(repository_name)
        except UnknownObjectException:
            return "Repository not found. Please use the exact name."

        try:
            pull_request = repository.get_pull(pull_request_number)
        except UnknownObjectException:
            return "Pull request not found. Please use the exact number."

        collaborators = [collaborator.login for collaborator in pull_request.requested_reviewers]

        return (
            f"Pull request title: {pull_request.title}\n"
            f"Pull request body: {pull_request.body}\n"
            f"Pull request state: {pull_request.state}\n"
            f"Owner: {pull_request.user.login}\n"
            f"Collaborators: {collaborators}\n"
        )

    def get_repository_issues(
        self,
        repository_name: str,
        state: str,
        sort: str = "created",
        direction: str = "desc",
        page: int = 0,
    ) -> List[PullRequest] | str:
        """
        A tool to search Github issues by repository name, state and sorted by params.
        Returns issues with their names and issue numbers.
        """

        try:
            repository = self.github_service.get_repo(repository_name)
        except UnknownObjectException:
            return "Repository not found. Please use the exact name."

        return (
            f"The issues of repository {repository_name} are: "
            f"{repository.get_issues(state=state, sort=sort, direction=direction).get_page(page)}"
        )

    def get_repository_issue_information(self, repository_name: str, issue_number: int) -> str:
        """
        A tool to get Github issue data by repository name and issue number.
        Useful when you need to know more about a specific issue.
        Returns issue information.
        """

        try:
            repository = self.github_service.get_repo(repository_name)
        except UnknownObjectException:
            return "Repository not found. Please use the exact name."

        try:
            issue = repository.get_issue(issue_number)
        except UnknownObjectException:
            return "Issue not found. Please use the exact number."

        return (
            f"Issue title: {issue.title}\n"
            f"Issue body: {issue.body}\n"
            f"Issue state: {issue.state}\n"
            f"Owner: {issue.user.login}\n"
            f"Collaborators: {[collaborator.login for collaborator in issue.assignees]}\n"
        )
