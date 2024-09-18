from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd


# Thiết lập tùy chọn trình duyệt với user-agent
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Tùy chọn chạy không giao diện
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Khởi tạo ChromeDriver với Service và ChromeOptions
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

base_url = 'https://www.amazon.com/books-used-books-textbooks/b/?ie=UTF8&node=283155&ref_=topnav_storetab_b&fbclid=IwY2xjawFXbBNleHRuA2FlbQIxMAABHSlh7ZzKAu3Ob2HVu6LB5m668a2d-vLH0qriYTZPnW1WMtaDzORMw77NJw_aem_-7ifTexpyV6BvDXz4FelmQ'

# page_url = f"{base_url}&page={page}"
topic_data = []

driver.get(base_url)
try: 
    try:
        topic_elements = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.a-section.a-spacing-none.apb-browse-refinements'))
        )
        print('đã tìm thấy thẻ ông')
        # topic= (topic_elements.find_elements(By.CSS_SELECTOR, 'ul.a-unordered-list.a-nostyle.a-vertical.a-spacing-medium'))
        print('đã tìm thấy thẻ cha')
    except:
        print('không tìm thấy thẻ')
    html = topic_elements.get_attribute("outerHTML")
    soup = BeautifulSoup(html, 'lxml')
    
    topics = soup.find_all('ul', {'class': 'a-unordered-list a-nostyle a-vertical a-spacing-medium'})
    # print(topics)
    book_topic = topics[1].find_all('li')
    book_topic.pop(0)
    # print(book_topic)

    i = 1
    for topic in book_topic:
        # lấy tên topic
        tag_name = topic.find_all('span')
        # print(tag_topic)
        name = tag_name[1].getText()
        
        # lấy link topic
        tag_link = topic.find('a')
        link = 'https://www.amazon.com' + tag_link.get('href')
        
        topic_info = {
            'Tid': 'T' + str(i),
            'name': name,
            'link' : link
        }
        topic_data.append(topic_info)
        i+=1
    df = pd.DataFrame(topic_data)
    df.to_excel('topic_data.xlsx', index=False, engine='openpyxl')

    
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

finally:
    driver.quit()