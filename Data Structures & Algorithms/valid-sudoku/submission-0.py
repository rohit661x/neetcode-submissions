class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # board [[][]]

        # each row can contain 1-9, a number must not repeat
        # each column can contain 1-9, a number must not repeat
        # each 3x3 block can contain 1-9, a number must not repeat
        # an empty cell is denoted with "."
        # repeatition implies understanding membership -> hash set

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        #range(stop) → one argument specifies the stopping point.

        # Detect duplicates within each row.
        # Detect duplicates within each column.
        # Detect duplicates within each 3×3 box.

        #the input is a two-dimensional array, This means we need to navigate two dimensions. the outer dim for row, the inner dim for col
        # -> nested for loops

        for i in range(9):
                for j in range(9):
                    num = board[i][j]

                    if num != ".":
                        if num in rows[i]:
                            return False
                        rows[i].add(num)

                        if num in cols[j]:
                            return False
                        cols[j].add(num)

                        #transform row indices 0, 1, 2 into 0, indices 3, 4, 5 into 1, and indices 6, 7, 8 into 2 
                        #i // 3 & j // 3 

                        box_index = (i // 3) * 3 + (j // 3)

                        if num in boxes[box_index]:
                            return False
                        boxes[box_index].add(num)
        return True
