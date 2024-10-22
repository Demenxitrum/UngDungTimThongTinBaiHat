import requests
from client.src.requests_handler import search_song, search_artist

def start_app():
    print("Chào mừng bạn đến với ứng dụng tìm bìa hát.")
    choice = input("Bạn muốn tìm kiếm: 1.Bài hát, 2.Ca sĩ(Nhập 1 hoặc 2): ")

    if choice == '1':
        song_name = input("Nhập tên bài hát: ")
        result = search_song(song_name)
        print("Kết quả tìm kiếm bài hát:")
        print(result)
    elif choice == '2':
        artist_name = input("Nhập tên ca sĩ: ")
        result = search_song(song_name)
        print("Kết quả tìm kiếm ca sĩ:")
        print(result)
    else:
        print("Lựa chọn không hợp lệ.")
