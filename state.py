class State:
    def __init__(self, tab):
        self.grid: list = tab  # état
        self.position_robot = self.get_position_robot()  # position du smiley

    def get_position_robot(self)->tuple:
        """Retourne la position actuelle du smiley dans l'état courant
        :rtype tuple"""
        try:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.grid[i][j] == 'S' or self.grid[i][j] == '$':
                        return tuple([i, j])
        except IndexError:
            pass
        return tuple()

    def __repr__(self):
        """Fonction appeller par défaut en python quand on demande
        de print une class directement"""
        chaine: str = ""
        for line in self.grid:
            for cell in line:
                chaine += cell
        return chaine

    def __eq__(self, state):
        """Compare l'état actuel à un autre état passé"""
        if self.position_robot == state.position_robot:
            return True
        return False

    def __hash__(self):
        chaine: str = ""
        for line in self.grid:
            for cell in line:
                if cell == 'M':
                    chaine += '1'
                elif cell == 'S':
                    chaine += '0'
                elif cell == 'H':
                    chaine += '3'
                elif cell == 'C':
                    chaine += '4'
                elif cell == '$':
                    chaine += '0'
        return int(chaine)
