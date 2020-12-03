with open('d3.txt') as f:
    puzzle_input = f.readlines()

puzzle_input = [x.strip() for x in puzzle_input]


class Toboggan:
    column = 0  # horizontal string index
    row = 0  # the array index
    current_row = puzzle_input[0]  # starting row
    trees = 0  # how many trees we hit

    def move(self, move_x, move_y):
        # Move row
        self.row += move_y
        try:
            self.current_row = puzzle_input[self.row]

            # Return on blank lines
            if not self.current_row:
                self.current_row = None
                return
        except IndexError:
            self.current_row = None
            return

        row_length = len(self.current_row)

        # Move column
        if self.column + move_x >= row_length:
            self.column = self.column + move_x - row_length
        else:
            self.column += move_x

        char_i = self.current_row[self.column]

        if char_i == '#':
            self.trees += 1


# Right 3, down 1
toboggan = Toboggan()

while (toboggan.current_row != None):
    toboggan.move(3, 1)

print(f'Trees hit: {toboggan.trees}')
