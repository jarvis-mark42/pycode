import sys
import requests
#create an access token and enter here
access_token=""
#from google find out the timestamp to the start of your birthday and enter here
timestamp=""
li=[]
def url_create():
        url="https://graph.facebook.com/me/feed?since=%s&access_token=%s" % (timestamp,access_token)
        return url
 
def get_post(url):
        req_obj=requests.get(url)
        datas=req_obj.json()
        return datas
 
def get_id(datas):
        for data in datas['data']:
                li.append(str(data['id']))
        return li
 
def response(li):
        for i in li:
                url="https://graph.facebook.com/%s/comments?&access_token=%s" % (i,access_token)
                requests.post(url,{"message" :"thanks"})
if __name__ == "__main__":
        url=url_create()
        datas=get_post(url)
        lis=get_id(datas)
        response(lis)
