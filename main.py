def main():
    while True:
        print("選択してください：")
        print("1: hirata-yuk")
        print("2: yuki-yositomi")
        print("3: たか@59期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("選択肢1が選ばれました。")
        elif choice == "2":
            print("yuki-yoshitomi")
        elif choice == "3":
            print("たか@59期が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
