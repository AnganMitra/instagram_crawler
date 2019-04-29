from instagram.client import InstagramAPI
import urllib2
access_token = "1699028470.35d7c66.4427a64b66694e568bafe2cff99c4faa"     # this is the access_token

"""
https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
Get basic information about a user.
"""
def get_user_details(user_id):
	url=url="https://api.instagram.com/v1/users/"+str(user_id)+"/?access_token="+str(access_token)
	f = urllib2.urlopen(url)
	w=open(".//data_collected//"+str(user_id)+"-itself",'w')
	data=f.read()
	w.write(data)
	w.close()
	return data
"""
https://api.instagram.com/v1/users/{user-id}/follows?access_token=ACCESS-TOKEN
Get the list of users this user follows.
"""	
def user_follows(user_id):

	url="https://api.instagram.com/v1/users/"+str(user_id)+"/follows?access_token="+str(access_token)
	f = urllib2.urlopen(url)
	w=open(".//data_collected//"+str(user_id)+"-follows",'w')
	data=f.read()
	w.write(data)
	w.close()
	return data
"""
https://api.instagram.com/v1/users/{user-id}/followed-by?access_token=ACCESS-TOKEN
Get the list of users this user is followed by.
"""

def user_followed(user_id):
	
	url="https://api.instagram.com/v1/users/"+str(user_id)+"/followed-by?access_token="+str(access_token)
	f = urllib2.urlopen(url)
	w=open(".//data_collected//"+str(user_id)+"-followed_by",'w')
	data=f.read()
	w.write(data)
	w.close()
	return data
	
def main():
	
	user_id=1699028470
	api = InstagramAPI(access_token=access_token)
	get_user_details(user_id)
	user_follows(user_id)
	user_followed(user_id)
	return
	
if __name__ == "__main__":
	main()
	
	
	

