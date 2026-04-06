class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_keys = {}
        col_keys = {i: [] for i in range(9)}
        square_keys = {i: [] for i in range(9)}

        for i, row in enumerate(board):
            temp_rowList = []
            for j, val in enumerate(row):
                if val != ".":
                    # Rows
                    temp_rowList.append(val)

                    # Columns
                    col_keys[j].append(val)

                    # Squares (3x3 box index)
                    square_index = (i // 3) * 3 + (j // 3)
                    square_keys[square_index].append(val)

            row_keys[i] = temp_rowList

        # Check all three dicts
        for d in [row_keys, col_keys, square_keys]:
            for lst in d.values():
                if len(lst) != len(set(lst)):
                    return False

        return True

