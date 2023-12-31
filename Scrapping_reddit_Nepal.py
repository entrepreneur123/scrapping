# -*- coding: utf-8 -*-
"""scraping  reddit Nepal

Automatically generated by Colaboratory.

Please use your own client id, secret and user_agent !I have removed for security purpose!!
   """

!pip -qqq install asyncpraw

CLIENT_ID = "xxxxxxxxxxxxxxxxxx"
CLIENT_SECRET = 	"XXXXXXXXXXXXXXXXXXXXXXXXXXX"

import asyncpraw
import asyncio

reddit_collected = asyncpraw.Reddit(client_id="XXXXXXXXXXXXXXXXXXXX", client_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" ,user_agent="XXXXXXXXXXX")



subreddit_name = 'Nepal'

Subreddit_scrapper = await reddit_collected.subreddit(subreddit_name)

Subreddit_scrapper

async def get_reddit_post(subreddit_name):
  subreddit = await reddit_collected.subreddit(subreddit_name)
  async for submission in subreddit.top(limit=25):
    yield submission

subreddit_name = 'Nepal'

# subreddit = await reddit_collected.subreddit(subreddit_name)
# async for submission in subreddit.hot():
#         print(submission)
#         print(submission.title)

import pandas as pd

column_names = ['Title','url','Upvotes','author','time','Num_comments']
async def main():
  items_reddit = []
  async for post in get_reddit_post(subreddit_name):
    post_data = {
        "Title":post.title,
        "URL":post.url,
        "Upvotes":post.score,
        "Author":post.author,
        "time":post.created_utc,
        "Num_comments":post.num_comments,


    }
    items_reddit.append(post_data)
    df = pd.DataFrame(items_reddit, columns=column_names)
  return df
collected_data = await main()

collected_data

async def main():
  items_reddit = []
  async for post in get_reddit_post(subreddit_name):
    print(f'Title:{post.title}')
    print(f'URL:{post.url}')
    print(f'Upvotes:{post.score}')
    print(f"author:{post.author}")
    print(f"time:{post.created_utc}")
    print(f"Num_comments:{post.num_comments}")
    items_reddit.append(post)
  return items_reddit
collected_data = await main()

collected_data

column_names = ['Title','URL','Upvotes','Author','Time','Num_comments']

async def main():
  items_reddit = []
  async for post in get_reddit_post(subreddit_name):
    post_data = {
        "Title":post.title,
        "URL":post.url,
        "Upvotes":post.score,
        "Author":post.author,
        "Time":post.created_utc,
        "Num_comments":post.num_comments,
    }
    items_reddit.append(post_data)
    df = pd.DataFrame(items_reddit, columns=column_names)
  return df

collected_data = await main()

collected_data