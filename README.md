# RedditHomophily

Calculates the number of deltas awarded for the 5 'hottest' posts on Reddit's /r/changemyview, and the number of different groups of users in that post (grouped by interests). A work in progress.

## Setup

1. Get Python, e.g. with Anaconda (anaconda.com/download).

2. The required libraries are listed in `requirements.txt`. Install them by running `pip install -r requirements.txt` in a terminal, from this folder.

3. Create a Reddit account and a Reddit app at this page: reddit.com/prefs/apps.
4. Create a file called `config.py` in this folder, with the following form:

```python
client_id=[your client id]
client_secret=[your client secret]
user_agent=[your user agent]
```

## How it Works

The top 5 hottest posts are scraped one-by-one, to count the number of deltas awarded, and to collect the subs contributed to by each author in the post.

For each pair of authors, their similarity of interests is calculated, according to the similarity of the subs that they contribute to. Take author A and author B. Suppose A contributes to /r/tech. For each sub that B contributes to, the similarity between /r/tech and that sub is calculated, according to the procedure outlined [here](shorttails.io/interactive-map-of-reddit-and-subreddit-similarity-calculator). This produces a number between 0 and 1. Say that the most similar sub that B contributes to is /r/technology (which has a similarity of 0.805). Then A's /r/tech sub has a similarity of 0.805 to the subs of B. The overall similarity between A and B is the sum of the similarities of A's subs to B's, plus the sum of the similarities of B's subs to A's, divided by the number of A's subs and B's subs (counting duplicates between them). This is thus weighted to produce a number between 0 and 1.

A weighted graph is produced where the nodes correspond to the authors in the post, and the edges between them are weighted by the similarities between each pair of authors. The [Python-Louvain library](python-louvain.readthedocs.io) is used to find the number of groups in this graph, by calculating its best partition.