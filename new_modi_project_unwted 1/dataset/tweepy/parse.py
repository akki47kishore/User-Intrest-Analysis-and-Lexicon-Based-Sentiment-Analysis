from bs4 import BeautifulSoup
import lxml
import requests 


def getPhoneStats(url):
    try:
        request= requests.get(url)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content,"lxml")

            for ul in soup.findAll("ul"):
                '''header = table.th.get_text()
                for row in table.findAll("tr"):
                    out_row = [ header ]
                    for col in row.findAll("td"):
                        out_row.append(col.get_text())
                    print(out_row)'''
                print ul.get_text()
        else:
            print('unable to connect ')
    except requests.HTTPError as e:
        print('Unable to open url',e)

if __name__ == "__main__":
    getPhoneStats('''http://tweeplers.com/?cc=IN''')
