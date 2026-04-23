def main():
    while True:
        print("選択してください：")
        print("1: ねここ")
        print("2: だいふく")
        print("3: おにちゃん")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("ねここが選ばれました。")
        elif choice == "2":
            print("だいふくが選ばれました。")
        elif choice == "3":
            print("おにちゃんが選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")


if __name__ == "__main__":
    main()
