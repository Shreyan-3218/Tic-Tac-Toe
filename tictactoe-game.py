class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        
    def print_board(self):
        """Print the current state of the board"""
        for i in range(0, 9, 3):
            print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ')
            if i < 6:
                print('-----------')
    
    def is_winner(self, player, board):
        """Check if the given player has won"""
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True
        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True
        # Check diagonals
        if board[0] == board[4] == board[8] == player:
            return True
        if board[2] == board[4] == board[6] == player:
            return True
        return False
    
    def is_board_full(self, board):
        """Check if the board is full"""
        return ' ' not in board
    
    def get_available_moves(self, board):
        """Get list of empty positions"""
        return [i for i, spot in enumerate(board) if spot == ' ']
    
    def minimax(self, board, depth, is_maximizing):
        """Minimax algorithm for AI moves"""
        # Terminal states
        if self.is_winner(self.ai, board):
            return 1
        if self.is_winner(self.human, board):
            return -1
        if self.is_board_full(board):
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_available_moves(board):
                board[move] = self.ai
                score = self.minimax(board, depth + 1, False)
                board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.human
                score = self.minimax(board, depth + 1, True)
                board[move] = ' '
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self):
        """Get the best move for AI using minimax"""
        best_score = float('-inf')
        best_move = 0
        
        for move in self.get_available_moves(self.board):
            self.board[move] = self.ai
            score = self.minimax(self.board, 0, False)
            self.board[move] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
                
        return best_move
    
    def play(self):
        """Main game loop"""
        print("Welcome to Tic-Tac-Toe!")
        print("Positions are numbered from 0-8, left to right, top to bottom")
        print("You are X, AI is O")
        
        while True:
            self.print_board()
            
            # Human turn
            while True:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if 0 <= move <= 8 and self.board[move] == ' ':
                        break
                    else:
                        print("Invalid move, try again")
                except ValueError:
                    print("Please enter a number between 0-8")
            
            self.board[move] = self.human
            
            # Check if human won
            if self.is_winner(self.human, self.board):
                self.print_board()
                print("Congratulations! You won!")
                break
                
            # Check if board is full
            if self.is_board_full(self.board):
                self.print_board()
                print("It's a tie!")
                break
            
            # AI turn
            print("\nAI is making a move...")
            ai_move = self.get_best_move()
            self.board[ai_move] = self.ai
            
            # Check if AI won
            if self.is_winner(self.ai, self.board):
                self.print_board()
                print("AI wins!")
                break
                
            # Check if board is full
            if self.is_board_full(self.board):
                self.print_board()
                print("It's a tie!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
