import requests

def github_repository_searcher():

    keyword = input("Enter keyword: ")
    params = {'q': keyword} # 'per_page': 10, 'sort': 'stars'
    response = requests.get("https://api.github.com/search/repositories", params)

    if response.status_code != 200:
        print(f"Error! '{response.status_code}'")
        return

    result = response.json()

    # print(result)
    # print(result.keys())
    print(f"Total results: {result['total_count']}")

    for info in result['items']:
        print(f"Repository name: '{info['name']}'")
        print(f"Description: <{info['description']}>")
        print(f"Link: <{info['html_url']}>")

github_repository_searcher()
