def is_valid(board, row, col, num):
    # Satır kontrolü
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Sütun kontrolü
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # 3x3'lük bölge kontrolü
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    # Boş bir hücre bul
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True  # Sudoku tamamlandı
    
    row, col = empty_loc
    
    # 1'den 9'a kadar sayılar denenecek
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            # Geriye dönüp kontrol et
            if solve_sudoku(board):
                return True
            
            # Eğer geçerli bir çözüm değilse, sayıyı geri al
            board[row][col] = 0
    
    # Sudoku çözülemezse
    return False

# Sudoku örneği
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Çözüm:")
    for row in sudoku_board:
        print(row)
else:
    print("Sudoku çözülemedi.")
