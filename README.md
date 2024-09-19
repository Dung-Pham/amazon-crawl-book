
# Crawl Amazon Books

## Link
[Amazon All Books](https://www.amazon.com/books-used-books-textbooks/b/?ie=UTF8&node=283155&ref_=topnav_storetab_b)
---
## Update
  - xong Topic 1, 2, 3 + filter 1,2 của topic 8

## Note
  - Xem topic ở trong folder data (32 topic)
  - Mỗi topic có nhiều filter (khoảng 40)
  - Mỗi filter có nhiều sách (khoảng 95-100)
  - Tạm thời lấy khoảng 3 - 4 topic để làm sạch đã nhá
  - Hiện tại t vừa lấy xong topic 1 rồi, giờ 2 người lấy 2 topic để cào rồi ghép lại là đc 3 topic r, còn ai nữa thì làm cái process kia vs báo cáo nữa 
  - T cũng đã lấy danh sách topic và filter rồi, chỉ còn lấy sách nữa thôi
## Lấy dữ liệu
  
  - Sửa vị trí lấy filter ở dòng số 195 file get_book.py nha
    ```python
    for filter in list_filter[a:b]:
    ```
  - lấy vị trí filter ở trong file filters_data.xlsx
  - tùy chỉnh theo vị trí của filter trong file excel nhá
## Giải thích

    - về id: T1F1B2: sách thứ 2 của filter 2 thuộc topic 1
      - T: là topic
      - F: là filter
      - B: là book
    - Về hoạt động:
      - get_book:
        - Đầu tiên là đọc và lấy ra danh sách filter từ file filters_data.xlsx
        - Đọc và lấy ra danh sách topic từ file topic_data.xlsx
        - Lặp qua các filter được giới hạn 
        - Tại mỗi filter thì kiểm tra xem nó thuộc topic nào để lấy link từ topic đó rồi truy cập vào web của topic tương ứng
        - Mở web và chọn đúng filter thành công thì thực hiện lấy sách 
        - sau khi lấy xong sách của mỗi filter, thì ghi luôn vào file books_data.xlsx danh sách của filter đó


