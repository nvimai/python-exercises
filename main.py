# Lấy hết toàn bộ dữ liệu mình cần dựa trên cấu trúc class product name, type, brand, price
# Tìm cách lưu ra file csv
# beautifulsoup read URL(search web)


# from bs4 import BeautifulSoup

# import requests
# htmlText = requests.get(
#     'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# soup = BeautifulSoup(htmlText, 'lxml')
# job = soup.find('li', {"class": "clearfix job-bx wht-shd-bx"})
# companyName = job.find('h3', {"class": ""})


# with open('airpodreal.html', 'r') as htmlFile:
#     content = htmlFile.read()
#     soup = BeautifulSoup(content, 'lxml')
#     nameTag = soup.find_all('h1')
#     for name in nameTag:
#         print(f'Name: {name.text}')

#     typeTag = soup.find_all('a', {"class": "breadcrumb-item"})
#     print(f'Type: {typeTag[2].text}')

#     brandTag = soup.find_all('td')
#     print(f'Brand: {brandTag[1].text}')

#     priceTag = soup.find_all('span', {"class": "product-price__current-price"})
#     for price in priceTag:
#         print(f'Price: {price.text}')
