def main():
    while True:
        print("選択してください：")
        print("1: きょん")
        print("2: ren")
        print("3: sayaka")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("きょんが選ばれました。")
        elif choice == "2":
            print("renが選ばれました。")
        elif choice == "3":
            print("sayakaが選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

