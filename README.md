# UngDungTimThongTinBaiHat
*)Mô tả chức năng ứng dụng
  - Chức năng 1: ứng dụng cho phép người dùng tra cứu thông tin bài hát dựa vào tên bài hát, tên bài hát có thể là tiếng Việt (có dấu/không dấu) hoặc tiếng Anh.
    +) Trường hợp tên bài hát chính xác, client hiển thị các thông tin:
        =>Lời bài hát
        =>Tên nhạc sỹ
        =>Một số audio/video (trên Youtube hoặc các trang nghe nhạc) để người dùng có thể nghe trực tiếp trên client.
    +) Trường hợp tên bài hát không chính xác, có lỗi đánh máy: gợi ý hoặc trả về bài hát gần đúng nhất.
  - Chức năng 2: tra cứu thông tin ca sĩ Việt Nam dựa vào tên
    +) Trường hợp tên ca sĩ chính xác, client hiển thị các thông tin (có thể lấy từ Wikipedia):
        =>Họ tên, ngày sinh, quê quán
        =>Thông tin về sự nghiệp
        =>Các bài hát, album nổi tiếng
        =>Một số audio/video (trên Youtube hoặc các trang nghe nhạc để người dùng có thể nghe trực tiếp trên client)
    +) Trường hợp tên ca sĩ không chính xác, có lỗi đánh máy hoặc không tìm thấy thông tin: báo lỗi
*)Yêu cầu về chức năng phía server (không cần GUI):
  - Nhận dữ liệu từ client, tìm kiếm và xử lý yêu cầu, trả kết quả lại cho client. Toàn bộ các thao tác xử lý nằm ở server, client chỉ hiển thị kết quả do server trả về và chạy audio/video do server gửi link.
*)Yêu cầu chung:
  - Các client phải chạy trên các máy tính khác nhau.
  - Mã hóa dữ liệu giữa client – server.    
