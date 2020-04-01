from instapy import InstaPy
from instapy.util import smart_run
import requests

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder

follow_list = [
    '要 follow 的帳號', '要 follow 的帳號二'
]

# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

bot = InstaPy(username="IG 帳號", password="IG 密碼", headless_browser=True )

with smart_run(bot):
    bot.follow_user_followers(follow_list, amount=200, randomize=False)
    bot.follow_user_following(follow_list, amount=200, randomize=False)
    bot.set_user_interact(amount=2,
                 percentage=70,
                  randomize=True,
                   media='Photo')
    bot.follow_likers(follow_list, photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=True)    
    bot.follow_commenters(follow_list, amount=200, daysold=365, max_pic = 100, sleep_delay=600, interact=False)
    bot.unfollow_users(amount=200, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
    bot.end()
