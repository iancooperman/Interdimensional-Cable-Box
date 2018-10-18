import praw


class RedditSkimmer:
    def __init__(self):
        # Define variables needed for PRAW instance.
        self.client_id = "5DfMk-zj5HF6CA"
        self.client_secret = "YgpVWQxBojDPyQWnt9cnXu-YCuI"
        self.user_agent = "whatever works"

        self.start_praw_instance()

        self.post_generator = self.interdimensional_cable_sub.hot(limit=None)

    def start_praw_instance(self):
        # Get a read-only instance of Reddit.
        self.reddit_reader = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, user_agent=self.user_agent)
        self.interdimensional_cable_sub = self.reddit_reader.subreddit('interdimensionalcable')


if __name__ == "__main__":

    reddit = RedditSkimmer()

    print(next(reddit.post_generator).title)
