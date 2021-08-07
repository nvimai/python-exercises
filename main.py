# Lấy hết toàn bộ dữ liệu mình cần dựa trên cấu trúc class product name, type, brand, price
# Tìm cách lưu ra file csv
# beautifulsoup read URL(search web)


from bs4 import BeautifulSoup

with open('airpodreal.html', 'r') as htmlFile:
    content = htmlFile.read()
    soup = BeautifulSoup(content, 'lxml')
    nameTag = soup.find_all('h1')
    for name in nameTag:
        print(f'Name: {name.text}')

    typeTag = soup.find_all('a', {"class": "breadcrumb-item"})
    print(f'Type: {typeTag[2].text}')

    brandTag = soup.find_all('td')
    print(f'Brand: {brandTag[1].text}')

    priceTag = soup.find_all('span', {"class": "product-price__current-price"})
    for price in priceTag:
        print(f'Price: {price.text}')
