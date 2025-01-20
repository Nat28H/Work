coin = int(input("Num coin : "))
player_turn = 1

while coin > 0:
    for _ in range(coin):
        print('⊙', end=' ')
    print()  # เพิ่มบรรทัดใหม่หลังจากพิมพ์เหรียญ

    if player_turn == 1:
        play1 = int(input("Player 1 เลือกหยิบ (1 หรือ 2): "))
        if play1 not in [1, 2]:
            print("เลือกไม่ถูกต้อง")
            continue  # กลับไปวนลูปใหม่
        coin -= play1
        if coin == 0:
            print("Player 1 แพ้")
            break  # ออกจากลูปเมื่อมีผู้ชนะ
    else:
        play2 = int(input("Player 2 เลือกหยิบ (1 หรือ 2): "))
        if play2 not in [1, 2]:
            print("เลือกไม่ถูกต้อง")
            continue
        coin -= play2
        if coin == 0:
            print("Player 2 แพ้")
            break

    player_turn = 1 - player_turn  # สลับผู้เล่น