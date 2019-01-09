from praw.models import MoreComments


def count_deltas(submission, REDDIT):

    allComments = submission.comments.list()

    for comment in allComments:
        if not isinstance(comment, MoreComments):
            author = comment.author
            if author == 'DeltaBot':
                body = comment.body
                id = body.split('r/DeltaLog/comments/')[1].split(')')[0]
                sub = REDDIT.submission(id=id)
                text = sub.selftext
                return text.count('*')

    return 0


def author_top_subs(author):

    subs = set()

    for comment in author.comments.top('all', limit=100):
        subs.add(comment.subreddit.display_name)

    return list(subs)


def submission_authors(submission, replaceMore=False):

    if replaceMore:
        submission.comments.replace_more(limit=0)

    allComments = submission.comments.list()

    authors = set()
    for comment in allComments:
        if not isinstance(comment, MoreComments):
            author = comment.author
            if author is not None:
                authors.add(author)

    return {author.name: author_top_subs(author) for author in authors}
