from community import best_partition
from praw import Reddit

from config import client_id, client_secret, user_agent
from graph import author_graph, plot_graph
from submissions import count_deltas, submission_authors


REDDIT = Reddit(client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent)

cmv = REDDIT.subreddit('changemyview')

for submission in cmv.hot(limit=5):

    print('\n')
    print(submission.url)

    nDelta = count_deltas(submission, REDDIT)

    print(nDelta, 'deltas')

    authorSubs = submission_authors(submission)

    G = author_graph(authorSubs)

    plot_graph(G)

    partition = best_partition(G)

    nGroups = len(set(partition.values()))

    print(nGroups, 'group(s)')
