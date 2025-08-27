import random

money = int(input("Nhập số tiền: "))
win_games = lose_games = total_games = 0

while money > 0:
    print(f"\nSố tiền hiện tại: {money}")
    try:
        bet = int(input("Nhập số tiền cược: "))
    except ValueError:
        print("Giá trị cược không hợp lệ. Vui lòng nhập số nguyên.")
        continue

    if bet <= 0:
        print("Số tiền cược phải lớn hơn 0.")
        continue
    if bet > money:
        print("Bạn không có đủ tiền để cược.")
        continue

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    pod = die1 + die2
    print(f"Xúc xắc: {die1} và {die2} (tổng = {pod})")

    try:
        g = int(input("Nhập dự đoán [1_Tài, 2_Xỉu]: "))
    except ValueError:
        print("Lựa chọn không hợp lệ. Ván này bị hủy.")
        continue

    if g not in (1, 2):
        print("Chỉ được chọn 1 (Tài) hoặc 2 (Xỉu).")
        continue

    # Quy ước: g==1 -> Tài (pod > 5); g==2 -> Xỉu (pod < 5); pod == 5 -> Hòa
    if pod > 5 and g == 1:
        print("Bạn đã thắng (Tài).")
        money += bet
        win_games += 1
    elif pod < 5 and g == 2:
        print("Bạn đã thắng (Xỉu).")
        money += bet
        win_games += 1
    elif pod == 5:
        print("Hòa: không mất không được tiền.")
        # không cộng vào win/lose
    else:
        print("Bạn đã thua.")
        money -= bet
        lose_games += 1

    total_games = win_games + lose_games

    if money <= 0:
        print("Bạn đã hết tiền chơi game.")
        break

    cont = input("Bạn có muốn chơi tiếp không? (y/n): ").strip().lower()
    if cont != "y":
        print("Cảm ơn bạn đã chơi.")
        break

print("\nThống kê:")
print(f"Tổng ván (không tính hòa): {total_games}, Thắng: {win_games}, Thua: {lose_games}, Tiền còn lại: {money}")
if total_games > 0:
    print(f"Tỷ lệ thắng: {win_games/total_games:.2%}")