from tkinter import Frame, Canvas
from game_platform.piece import Piece
from game_platform.board import Board

TITLE = 'UU-Game'
HEIGHT = 800  # test size
WIDTH = 800  # test size
BACKGROUND_COLOUR = 'white'
SLCTD_PCE_X_POS = 500
SLCTD_PCE_Y_POS = 50


class GamePlatform(Frame):
    """
    The game platform GUI
    Author(s): Adam Ross
    Last-edit-date: 21/02/2019
    """

    def __init__(self, master, play):
        """
        Initializes the GUI
        :param master: the parent widget
        :param play: Play class instance
        """
        super().__init__(master)
        self.master = master
        self.play = play
        self.master.title(TITLE)
        self.canvas = Canvas(height=HEIGHT, width=WIDTH, bg=BACKGROUND_COLOUR)
        self.canvas.pack()
        self.pieces = dict({i: Piece(self.canvas, self.play.game.pieces[i])
                            for i in self.play.game.pieces}.items())
        self.board = Board(self.canvas, 10, 300, 300)

    def move_selected_piece(self, pce_id):
        """
        Moves a selected piece to the selected piece area on the GUI
        Takes an ID (1 - 16) for finding the selected piece by key: ID - 1
        :param pce_id: the id for the selected piece being moved
        """
        self.canvas.delete(self.pieces[str(pce_id - 1)].shape)

        if self.pieces[str(pce_id - 1)].horizontal:
            self.canvas.delete(self.pieces[str(pce_id - 1)].horizontal)

        if self.pieces[str(pce_id - 1)].vertical:
            self.canvas.delete(self.pieces[str(pce_id - 1)].vertical)
        self.pieces[str(pce_id - 1)] = Piece(self.canvas, bin(pce_id - 1)[2:].
                                             zfill(self.play.game.N),
                                             SLCTD_PCE_X_POS, SLCTD_PCE_Y_POS)