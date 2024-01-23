import requests
import base64
import pandas 

class EtlLanguages:

    def __init__(self, owner: str, token: str) -> None:
        self.owner = self.verify_existent_user(owner)
        self.token = token
        self.base_api_url = 'https://api.github.com'
        self.headers ={'Authorization': 'Bearer ' + self.token, 'X-GitHub-Api-Version': '2022-11-28'}

    def verify_existent_user(self, owner: str) -> str:
        request_http = requests.get(url=f'{self.base_api_url}/{owner}/repos')
        if request_http.status_code > 400:
            ValueError(args=f'The username {owner} not exist on Github.')

        return owner

    def list_repos(self) -> list:

        repos_list = []

        for page_number in range(1,20):
            try:
                response_http = requests.get(url=f'{self.base_api_url}/users/{self.owner}/repos?page={page_number}', headers=self.headers)
                if response_http.status_code >= 400:
                    print(response_http.body)
                elif response_http.status_code != 200 and response_http.status_code < 400:
                    print(f'SOMETHING IS WRONG WITH STATUS {response_http.status_code}')
                    break
                elif response_http.status_code == 200:
                    repos_list.append(response_http.json())
                else:
                    print(f'HTTP STATUS CODE {response_http.status_code}')
                    pass
            except:
                if response_http == 404:
                    print(f'The TRY to GET information of owner {self.owner} was error. The owner was not found. HTTP STATUS: {response_http.status_code}')
                else:
                    print(f'The request to GET information of owner {self.owner} has an problem with the status {response_http.status_code} and message {response_http.reason}')

        return self.repos_list
    
    def repos_name(self) -> list:

        return repos_name_list 
    
    def languages_name(self) -> list:
        pass

    def generate_dataframe(self) -> None:
        pass