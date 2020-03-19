import tweepy
# 「xxxxx」を、TwitterのAPIトークンに置き換える。
CONSUMER_KEY = 'xxxxx'
CONSUMER_SECRET = 'xxxxx'
ACCESS_TOKEN = 'xxxxx'
ACCESS_TOKEN_SECRET = 'xxxxx'

# いいねを消すアカウントの「@」以降のアカウント名を入れる
screen_name = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
API = tweepy.API(auth)
user_info = API.get_user(screen_name=screen_name)

# 一回の取得で約20件のいいねを取得できます。
#「*」入れた数字 ×20 が削除される いいね の数です。（APIの仕様上一度に消せる数に制限があります）
for i in range(*):
	FAVORITE = API.favorites(screen_name=screen_name,page=i+1)
	for number in FAVORITE:
		status = API.destroy_favorite(number.id)
		print('「{}」というツイートのいいねを取り消しました！'.format(status.text))

###Written by Kanoe###