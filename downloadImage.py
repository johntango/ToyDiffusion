# download jpg file from url and save it to a file
import urllib.request
url = "https://www.infomoney.com.br/wp-content/uploads/2019/06/homer-simpson.jpg"
urllib.request.urlretrieve(url, "homer.jpg")
# read the image file
