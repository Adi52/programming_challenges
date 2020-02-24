import pygame.gfxdraw

class Piece():
    def __init__(self, screen, board, ai_settings):
        self.PIECE_SIZE = 100
        self.screen = screen
        self.board = board
        self.ai_settings = ai_settings

    def draw(self, column, row, color):
        # Puste kółka z nałożonymi okręgami aby wyrównać krawędzie + cień
        pygame.gfxdraw.aacircle(self.screen, column * self.PIECE_SIZE + 67, row * self.PIECE_SIZE + 173, 42, (37, 67, 166))
        pygame.gfxdraw.filled_circle(self.screen, column * self.PIECE_SIZE + 67, row * self.PIECE_SIZE + 173, 42, (37, 67, 166))
        pygame.gfxdraw.aacircle(self.screen, column * self.PIECE_SIZE + 70, row * self.PIECE_SIZE + 170, 42, color)
        pygame.gfxdraw.filled_circle(self.screen, column * self.PIECE_SIZE + 70, row * self.PIECE_SIZE + 170, 42, color)