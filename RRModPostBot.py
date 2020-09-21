# Copyright 2020 called2voyage
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import praw
import os
from datetime import datetime, timezone

reddit = praw.Reddit('bot3')
print(reddit.user.me())
subreddit = reddit.subreddit("religion")
print(subreddit)

if not os.path.isfile("post_history.txt"):
    post_history = []
else:
    with open("post_history.txt", "r") as f:
        post_history = f.read()
        post_history = post_history.split("\n")
        post_history = list(filter(None, post_history))

#If it's Monday, and the weekly submission hasn't yet been posted
if datetime.now(tz=timezone.utc).weekday() == 0 and datetime.now(tz=timezone.utc).strftime('%Y-%m-%d') not in post_history:
    title = 'Weekly "What is my religion?" discussion'
    selftext = '''Are you looking for suggestions of what religion suits your beliefs?
Or maybe you're curious about joining a religion with certain qualities but don't know if it exists?
Once a week, we provide an opportunity here for you to ask other users what religion fits you.
'''
    subreddit.submit(title, selftext=selftext)
