
import requests

url = 'https://www.google.com/search?q=Tim+Berners-Lee'

r = requests.get(url)
print(r.status_code)
print(r.request.headers)
print(r.text)

#--------------------------------------------------------------
API_ENDPOINT = "http://pastebin.com/api/api_post.php"
  
# your API key here 
API_KEY = "3"
  
# your source code here 
source_code = 1
  
# data to be sent to api 
data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 

#---------------------------------------------------------------
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")

print(response.status_code)
print(r.request.headers)
print(r.text)


























