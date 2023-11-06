import sys
import os

print("Running Sherlock")

data_csv = r"""username,name,url_main,url_user,exists,http_status,response_time_s
hirushaadi,Anilist,https://anilist.co/,https://anilist.co/user/hirushaadi/,Claimed,200,4.281000000000859
hirushaadi,Chess,https://www.chess.com/,https://www.chess.com/member/hirushaadi,Claimed,200,12.20299999999952
hirushaadi,Codewars,https://www.codewars.com,https://www.codewars.com/users/hirushaadi,Claimed,200,16.64099999999962
hirushaadi,DEV Community,https://dev.to/,https://dev.to/hirushaadi,Claimed,200,15.20299999999952
hirushaadi,DeviantART,https://deviantart.com,https://hirushaadi.deviantart.com,Claimed,200,18.17199999999866
hirushaadi,Docker Hub,https://hub.docker.com/,https://hub.docker.com/u/hirushaadi/,Claimed,200,16.59399999999914
hirushaadi,G2G,https://www.g2g.com/,https://www.g2g.com/hirushaadi,Claimed,200,20.936999999999898
hirushaadi,Imgur,https://imgur.com/,https://imgur.com/user/hirushaadi,Claimed,200,31.53099999999904
hirushaadi,LeetCode,https://leetcode.com/,https://leetcode.com/hirushaadi,Claimed,200,34.76599999999962
hirushaadi,Lichess,https://lichess.org,https://lichess.org/@/hirushaadi,Claimed,200,34.48400000000038
hirushaadi,Lolchess,https://lolchess.gg/,https://lolchess.gg/profile/na/hirushaadi,Claimed,200,36.60900000000038
hirushaadi,Medium,https://medium.com/,https://medium.com/@hirushaadi,Claimed,200,48.75
hirushaadi,Reddit,https://www.reddit.com/,https://www.reddit.com/user/hirushaadi,Claimed,200,55.26599999999962
hirushaadi,Snapchat,https://www.snapchat.com,https://www.snapchat.com/add/hirushaadi,Claimed,200,60.23400000000038
hirushaadi,Telegram,https://t.me/,https://t.me/hirushaadi,Claimed,200,65.375
hirushaadi,Tenor,https://tenor.com/,https://tenor.com/users/hirushaadi,Claimed,200,65.95299999999952
hirushaadi,TikTok,https://tiktok.com/,https://tiktok.com/@hirushaadi,Claimed,200,68.40599999999904
hirushaadi,TryHackMe,https://tryhackme.com/,https://tryhackme.com/p/hirushaadi,Claimed,200,82.32799999999952
hirushaadi,Twitter,https://twitter.com/,https://twitter.com/hirushaadi,Claimed,403,110.21899999999914
hirushaadi,Unsplash,https://unsplash.com/,https://unsplash.com/@hirushaadi,Claimed,200,70.75
hirushaadi,Virgool,https://virgool.io/,https://virgool.io/@hirushaadi,Claimed,200,76.0619999999999
hirushaadi,VirusTotal,https://www.virustotal.com/,https://www.virustotal.com/gui/user/hirushaadi,Claimed,200,72.65599999999904
hirushaadi,Whonix Forum,https://forums.whonix.org/,https://forums.whonix.org/u/hirushaadi/summary,Claimed,200,75.07799999999952
hirushaadi,mastodon.social,https://chaos.social/,https://mastodon.social/@hirushaadi,Claimed,200,88.17200000000048
hirushaadi,metacritic,https://www.metacritic.com/,https://www.metacritic.com/user/hirushaadi,Claimed,200,89.6869999999999
"""


# {python} sherlock --verbose --no-color --nsfw --csv {username}
username = sys.argv[1:][-1]
print(username)

if not os.path.isdir(os.path.join(os.getcwd(), username)):
    os.mkdir(username)
csv_path = os.path.join(os.getcwd(), username, f'{username}.csv')
with open(csv_path, 'w') as file:
    file.write(data_csv)

print("Quitting Sherlock")
