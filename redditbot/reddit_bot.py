import praw
import prawoauth2
from settings import app_key, app_secret, user_agent, scopes, access_token, refresh_token


class RedditBot:
    def __init__(self):
        self.r = praw.Reddit(user_agent=user_agent)

        # Reddit OAuth 2 connection (required by reddit)

        self.o = prawoauth2.PrawOAuth2Mini(self.r, app_key=app_key,
                                           app_secret=app_secret,
                                           access_token=access_token,
                                           refresh_token=refresh_token,
                                           scopes=scopes)

        # a list of strings that will be checked against to see if the post titles are vod questions
        # add strings that are common titles for the vod question posts
        self.question_list = ['will be available to watch?', 'vods get posted?']
        # This is the message that the bot will respond to posts with
        self.msg = 'This is the text that the bot will respond with.'

    @staticmethod
    def check_if_responded(post_id):
        """
        :param post_id: the id of the post to check
        This function checks to see if the post_id has already been responded to
        """
        with open('already_posted.txt', 'r') as f:
            for line in f:
                print("Line: ", line)
                if post_id in line:
                    f.close()
                    return True
            f.close()
            return False

    def search(self):
        """
        This function searches through new posts to see if they match a list of
        strings to auto reply to post that match that list
        """
        try:
            subreddit = self.r.get_subreddit('criticalrole')
            subreddit.refresh()

            for post in subreddit.get_new(limit=15):
                is_vod_question = any(string in post.title.lower() for string in self.question_list)
                if is_vod_question:
                    already_responded = self.check_if_responded(post.id)
                    if not already_responded:
                        post.add_comment(self.msg)
                        with open('already_posted.txt', 'a') as out:
                            out.write(post.id + '\n')
                            out.close()
        except praw.errors.OAuthInvalidToken:
            self.o.refresh()

if __name__ == '__main__':
    begin_bot = RedditBot()
    begin_bot.search()
