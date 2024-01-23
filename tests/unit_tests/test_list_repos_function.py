from src.etl_languages import EtlLanguages

class TestListReposFunction:

    def __init__(self) -> None:
        self.owner = EtlLanguages(owner='amzn', token='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')

    def test_create_list_of_repos_by_owner_and_token(self):

        self.owner.list_repos()
