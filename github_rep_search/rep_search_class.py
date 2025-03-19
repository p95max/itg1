import requests

class GithubRepositorySearcher:
    def __init__(self):
        self.keyword = None

    def enter_keyword(self):
        while True:
            try:
                print("---Github Repository Searcher by keyword---")
                user_keyword = input("Enter keyword: ")
                if user_keyword:
                    self.keyword = user_keyword
                    return user_keyword
                else:
                    print("Keyword cannot be empty")

            except KeyboardInterrupt:
                print("\nInput was interrupted.")
                return None

    def check_keyword(self):
        while True:
            try:
                params = {'q': self.keyword} # 'per_page': 10, 'sort': 'stars'
                response = requests.get("https://api.github.com/search/repositories", params)
                return response.json()

            except requests.exceptions.HTTPError:
                   if response.status_code == 400:
                      print(f"Error! '{response.status_code}'")
                      self.enter_keyword()
                      return self.check_keyword()
                   else:
                       print(f"HTTP error: {response.status_code}. Please try again.")

    def show_result(self, result):
        if not result:
            return

        # print(result)
        # print(result.keys())
        print(f"Total results founded: {result['total_count']}")

        for info in result['items']:
            print(f"Repository name: '{info['name']}'")
            print(f"Description: <{info['description']}>")
            print(f"Link: <{info['html_url']}>")


    def run(self):

        self.enter_keyword()
        result = self.check_keyword()
        self.show_result(result)

if __name__ == '__main__':
    app = GithubRepositorySearcher()
    app.run()