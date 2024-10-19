import instaloader

loader = instaloader.Instaloader()
a = input("Enter your instagram username: ")
b = input("Enter your password: ")
loader.login(a,b)
profile = instaloader.Profile.from_username(loader.context,a)

following = {followee.username for followee in profile.get_followees()}
followers = {follower.username for follower in profile.get_followers()}

not_following_back = list(following - followers)
print("People you follow who do not follow you back:")
for i in not_following_back:
    print(i)
