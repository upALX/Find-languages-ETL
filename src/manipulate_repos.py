class ManipulateRepos:

    def __init__(self, owner: str, token: str) -> None:
        self.owner = owner
        self.api_base_url = 1
        self.token = token
        self.headers = ''

    # Create a repo on GitHub X NETFLIX, APPLE, AMAZON(AMZN), SPOTIFY
    def create_repo(self, repo_name: str) -> str:
        pass

    # Add file on X repository
    def add_file(self, repo_name: str, file_name: str, file_path: str) -> None:
