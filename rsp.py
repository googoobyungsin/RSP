import random

while True:
    player = input("가위 바위 보 중에 하나를 입력하세요!! : ")

    if player in ['가위', '바위', '보']:
        bot = random.choice(['가위', '바위', '보'])

        print("Player : {0}".format(player))
        print("Bot : {0}".format(bot))

        if player == ("가위"):
            if bot == ("가위"):
                print("무승부")
            elif bot == ("바위"):
                print("패배")
            else:
                print("승리")

        if player == ("바위"):
            if bot == ("바위"):
                print("무승부")
            elif bot == ("보"):
                print("패배")
            else:
                print("승리")

        if player == ("보"):
            if bot == ("보"):
                print("무승부")
            elif bot == ("가위"):
                print("패배")
            else:
                print("승리")
    else:
        print("잘못된 값을 입력하셨습니다.")
        continue
