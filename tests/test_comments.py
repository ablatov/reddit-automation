from reddit_helper import Reddit

REDDIT = Reddit("bot1")

# TODO remove logic from test into setup and teardowns
# @pytest.fixture
# def post_setup():
#   yield
#
# @pytest.fixture
# def post_teardown():
#   yield


class TestComments:
    def test_should_leave_comment_for_thread(self):
        # setup
        post = REDDIT.create_post()

        # test
        comment = REDDIT.leave_comment_for_post(post.id, "Some comment text!")
        comments_list = REDDIT.get_all_comments_for_post(post.id)
        assert len(comments_list) == 1

        # teardown
        REDDIT.remove_comment(comment.id)
        comments_list = REDDIT.get_all_comments_for_post(post.id)
        assert len(comments_list) == 0
        REDDIT.remove_post(post.id)
