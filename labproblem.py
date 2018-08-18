from search import *
from action import Action


class LabProblem(Problem):
    goal_position: tuple = ()
    nb_explored_node: int = 0

    def goal_test(self, state):
        self.nb_explored_node += 1
        if self.goal_position == state.position_robot:
            return True
        return False

    def successor(self, state):
        sucess: list[tuple] = []
        action = Action(state)

        succ: tuple = action.up()  # Déplacer le smiley vers le haut
        if len(succ) != 0:  # si le déplcement est possible
            sucess.append(succ)  # Enregistrement de l'état et de l'action

        succ: tuple = action.down()  # Déplacer le smiley vers le bas
        if len(succ) != 0:
            sucess.append(succ)

        succ: tuple = action.right()  # Déplacer le smiley vers la droite
        if len(succ) != 0:
            sucess.append(succ)

        succ: tuple = action.left()  # Déplacer le smiley vers la gauche
        if len(succ) != 0:
            sucess.append(succ)

        return sucess

    def path_cost(self, c, state1, action, state2)->int:
        k, m = state2.position_robot  # Recupere position du S sur le state2
        grid_state1: list = state1.grid.copy()  # Etat de la grille

        #  Vérification de l'emplacement du smiley avant son déplacement
        if grid_state1[k][m] == ' ' or grid_state1[k][m] == '$':
            c += 1
        elif grid_state1[k][m] == 'H':
            c += 2
        return c

