def checkmate(board):    
    # print(len(board))
    # print(board.split())

    if board == "":
        return ("Error")

    board = board.upper()
    
    count_k = board.count("K")
    if count_k != 1:
        return "Error"
    
    board_split = board.split()
    total_rows = len(board_split)
    for row in board_split:
        if len(row) != total_rows:
            return "Error"

    
    
    diagonal = [(-1,-1), (-1,1), (1,-1), (1,1)]

    n = len(board_split)
    #หา K ว่าอยู่ตำแหน่งไหน
    #R...
    #.K..
    #.P..
    #....
    ki = kj = 0
    for i in range(n):
        for j in range(n):
            print(board_split[i][j], end="")
            if board_split[i][j] == 'K':
                ki, kj = i, j
        print()

    #หาแนวตรงรอบ K
    #..X..
    #..O..
    #XXKXX
    #..X..
    #..X..
    straight = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for i, j in straight:
        temp_i, temp_j = i + ki, j + kj
        while 0 <= temp_i < n and 0 <= temp_j < n:
            txt = board_split[temp_i][temp_j]
            if txt in 'RQ':
                return "Success"
            if txt in 'PB':
                break
            temp_i += i
            temp_j += j

    #หาแนวเฉียงรอบ K
    #X...X
    #.X.X.
    #..K..
    #.X.X.
    #X...X
    for i, j in diagonal:
        temp_i, temp_j = i + ki, j + kj
        while 0 <= temp_i < n and 0 <= temp_j < n:
            txt = board_split[temp_i][temp_j]
            if txt in 'BQ':
                return "Success"
            if txt in 'RP':
                break
            temp_i += i
            temp_j += j

    #เช็ค P ใต้ K
    #....
    #....
    #.K..
    #P...
    if 0 <= ki+1 < n and 0 <= kj-1 < n:
        if board_split[ki+1][kj-1] == 'P':
            return "Success"
    if 0 <= ki+1 < n and 0 <= kj+1 < n:
        if board_split[ki+1][kj+1] == 'P':
            return "Success"

    return "Fail"
# ================== ตัวอักษรบนกระดาน ==================
#
# K = King (ราชา)
#     หมากของเรา มีได้ตัวเดียว เป็นตัวที่เราเช็คว่าโดนรุกไหม
#
# P = Pawn (เบี้ย)
#     กินได้แค่ทแยงขึ้นด้านบน 1 ช่อง (ซ้ายบน / ขวาบน)
#         . . . . .
#         . X . X .      X = ช่องที่ P กินได้
#         . . P . .
#     กลับด้านมองจาก K: P ที่กิน K ได้ต้องอยู่ "ใต้ K ทแยง 1 ช่อง"
#
# B = Bishop (บิชอป / โคน)
#     กินทแยงได้ทั้ง 4 ทิศ ไกลแค่ไหนก็ได้ จนกว่าจะเจอหมากตัวแรกที่ขวาง
#         X . . . X
#         . X . X .
#         . . B . .
#         . X . X .
#         X . . . X
#
# R = Rook (เรือ)
#     กินแนวตรงได้ทั้ง 4 ทิศ (บน ล่าง ซ้าย ขวา) ไกลแค่ไหนก็ได้
#         . . X . .
#         . . X . .
#         X X R X X
#         . . X . .
#         . . X . .
#
# Q = Queen (ควีน)
#     รวมท่าของ B กับ R: กินได้ทั้งแนวตรงและแนวทแยง 8 ทิศ
#         X . X . X
#         . X X X .
#         X X Q X X
#         . X X X .
#         X . X . X
#
# ตัวอักษรอื่นทั้งหมด ('.', ' ', 'x', '0', ...) = ช่องว่าง
#
# กฎสำคัญ: หมากกินได้แค่ "ตัวแรกที่เจอบนเส้นทาง"
#     R . P K   -> R กิน K ไม่ได้ เพราะ P บังอยู่
#
# ======================================================