import time
from typing import List

import praw
from praw.reddit import Comment, Submission


class Reddit:
    def __init__(self, bot_name: str):
        self.reddit = praw.Reddit(bot_name, user_agent=f"${bot_name} user agent")
        self.reddit.validate_on_submit = True

    def create_post(self) -> Submission:
        title = "PRAW documentation"
        url = "https://praw.readthedocs.io"
        return self.reddit.subreddit("test").submit(title, url=url)

    def remove_post(self, post_id: str):
        self.reddit.submission(post_id).delete()

    def leave_comment_for_post(self, post_id: str, text: str) -> Comment:
        submission = self.reddit.submission(post_id)
        return submission.reply(body=text)

    def remove_comment(self, comment_id: str):
        self.reddit.comment(comment_id).delete()

    def get_all_comments_for_post(self, post_id: str) -> List:
        time.sleep(5)  # TODO make wait_until_condition function for explicit await
        return self.reddit.submission(post_id).comments.list()


# if __name__ == "__main__":
#     REDDIT = Reddit("bot1")
#
#     # setup
#     post = REDDIT.create_post()
#
#     # test
#     comment = REDDIT.leave_comment_for_post(post.id, "Some comment text!")
#     comments_list = REDDIT.get_all_comments_for_post(post.id)
#     assert len(comments_list) == 1
#
#     # teardowm
#     REDDIT.remove_comment(comment.id)
#     comments_list = REDDIT.get_all_comments_for_post(post.id)
#     assert len(comments_list) == 0
#     REDDIT.remove_post(post.id)
