import requests
import toolbox as tb


@tb.decorator.memoize(94000) 
def get_github_repo_info(username, repo_name):
    url = f'https://api.github.com/repos/{username}/{repo_name}'
    response = requests.get(url)
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info()
    else:
        print(
            f"Error: Unable to fetch information. Status code: {response.status_code}")


# Example usage
github_username = 'owrel'
repository_name = 'clindoc'
get_github_repo_info(github_username, repository_name)
get_github_repo_info(github_username, repository_name)
