from state import State


class Action:
    def __init__(self, etat):
        self.state = etat
        self.copy: list = []  # Contient la copie de state.grid

    def copy_tab(self, tab)->list:
        """ cette fonction fait une copie d'une liste - utilisée pour avoir
        une copie du tableau qui représente un état """
        self.copy: list = []
        for i in range(len(tab)):
            self.copy.append(tab[i][:])
        return self.copy

    def up(self) -> tuple:
        """Deplace le smiley vers le haut
        :rtype tuple
        :return (self.up , State(next_child_grid))"""
        move: bool = False  # aucun mouvement effectué
        # Copie de l'état actuel
        next_child_grid: list = self.copy_tab(self.state.grid)
        i, j = self.state.position_robot  # Emplacement du smiley
        if i > 1:  # Condition pour un move up
            if next_child_grid[i - 1][j] == ' ':
                next_child_grid[i - 1][j] = 'S'  # Deplacement
                move = True  # mouvemet effectué
            elif next_child_grid[i-1][j] == 'H':
                next_child_grid[i-1][j] = '$'  # Deplacement
                move = True
            if move:  # vérifie si un mouvement à été effectué
                if next_child_grid[i][j] == '$':
                    next_child_grid[i][j] = 'H'
                else:
                    next_child_grid[i][j] = ' '
            return tuple([self.up, State(next_child_grid)])
        return tuple()

    # Déplacer le smiley vers le bas
    def down(self) -> tuple:
        """Depalce le smiley vers le bas"""
        move: bool = False
        next_child_grid: list = self.copy_tab(self.state.grid)
        i, j = self.state.position_robot
        if i < len(next_child_grid) - 2:  # Condition pour un move down
            if next_child_grid[i+1][j] == ' ':
                next_child_grid[i+1][j] = 'S'
                move = True
            elif next_child_grid[i+1][j] == 'H':
                next_child_grid[i+1][j] = '$'
                move = True
            if move:
                if next_child_grid[i][j] == '$':
                    next_child_grid[i][j] = 'H'
                else:
                    next_child_grid[i][j] = ' '
            return tuple([self.down, State(next_child_grid)])
        return tuple()

    # Déplacer le smiley vers la gauche
    def left(self) -> tuple:
        """Deplace le smiley vers la gauche"""
        move: bool = False
        next_child_grid: list = self.copy_tab(self.state.grid)
        i, j = self.state.position_robot
        if j > 1:  # Condition pour un move left
            if next_child_grid[i][j - 1] == ' ':
                next_child_grid[i][j - 1] = 'S'
                move = True
            elif next_child_grid[i][j-1] == 'H':
                next_child_grid[i][j-1] = '$'
                move = True
            if move:
                if next_child_grid[i][j] == '$':
                    next_child_grid[i][j] = 'H'
                else:
                    next_child_grid[i][j] = ' '
            return tuple([self.left, State(next_child_grid)])
        return tuple()

    # Déplacer le smiley vers la droite
    def right(self) -> tuple:
        """Deplace le smiley vers la droite"""
        move: bool = False
        next_child_grid: list = self.copy_tab(self.state.grid)
        i, j = self.state.position_robot
        if j < len(next_child_grid[0]) - 2:  # Condition pour un move right
            if next_child_grid[i][j + 1] == ' ':
                next_child_grid[i][j + 1] = 'S'
                move = True
            elif next_child_grid[i][j + 1] == 'H':
                next_child_grid[i][j + 1] = '$'
                move = True
            if move:
                if next_child_grid[i][j] == '$':
                    next_child_grid[i][j] = 'H'
                else:
                    next_child_grid[i][j] = ' '
            return tuple([self.right, State(next_child_grid)])
        return tuple()
