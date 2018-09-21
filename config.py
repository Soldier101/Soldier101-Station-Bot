import os
#token configuration
# Legacy token system
#BOTTOKEN = 'Yourtokenhere' #uncomment and put your token here if you want it to be unsecure
# new tokens (env var named BOTTOKEN need to contain the token for the bot)
BOTTOKEN = (os.environ['BOTTOKEN']) #comment out if you want to use the plain text token

