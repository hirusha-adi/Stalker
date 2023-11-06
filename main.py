from modules import sherlock_account
from utils.init import initializse

initializse()
username = "hirushaadi"
data = sherlock_account.getSherlock(username=username)
sherlock_account.showSherlock(data=data)
