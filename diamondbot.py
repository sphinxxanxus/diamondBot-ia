#!/usr/bin/python3
import argparse
from threading import Thread
import os
from time import clock, sleep

from labproblem import LabProblem
from search import *
from state import State

goal_position: tuple = ()


def cmd_line():
    parser = argparse.ArgumentParser(description='Jeu de labyrinthe')
    parser.add_argument('-i', '--init', help="Etat initial", type=str)
    parser.add_argument('-g', '--goal', help="Etat final", type=str)
    parser.add_argument('-l', '--list', help='Liste des algos ',
                        action='store_true')
    parser.add_argument('-n', '--num', help='Numéro de l\'algo', type=int)
    return parser.parse_args()


def read_file(file_name: str) -> list:
    """Retourne le contenu du fichier en entrer sous forme d'un tableau
    à double dimension
    @:param file_name
    @:rtype list
    """
    state_grid: list[list] = []
    with open(file_name, 'r', encoding='utf-8') as file_open:
        for line in file_open:
            state_grid.append(list(line))
    return state_grid


def get_diamant_position(grid: list) -> tuple:
    """Retourne la position du diamant dans sur le goal grid
    :rtype tuple
    """
    try:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'D':
                    return tuple([i, j])
    except IndexError:
        pass


def heuristic(nod) -> int:
    """Fonction heuristique pour les algos qui prennent une heuristique"""
    i, j = nod.state.position_robot  # Position du robot
    k, m = goal_position  # Position du diamant
    h: int = abs(k - i) + abs(m - j)  # distance de manhattan entre S et D
    return h


def heuristic_ucs(nod) -> int:
    """Fonction heuristique spécifique à UCS"""
    return 0


class Algo:  # class qui permet de faire le mapage
    """Classe qui permet de faire le mapage"""

    def __init__(self, algo_num: int, label: str, func):
        self.algo_num = algo_num
        self.label = label
        self.func = func


def get_list_algo():  # Affiche la liste des algos disponibles
    """Affiche la liste des algorithmes"""
    for k, v in build_algo().items():
        print("{}: {}".format(k, v.label))


def build_algo() -> dict:
    """Fonction de mapage du dictionnaire des Algo. {Key: Algo}"""
    # Mapage key:Algo
    algo_list: dict = {
        1: Algo(1, 'A* Graph search', astar_graph_search),
        2: Algo(2, 'Uniform cost search', astar_graph_search),
        3: Algo(3, 'BFS Graph Search', breadth_first_graph_search),
        4: Algo(4, 'BFS  Tree Search',
                breadth_first_tree_search),
        5: Algo(5, 'DFS Graph Search', breadth_first_graph_search),
        6: Algo(6, 'DFS Tree Search', breadth_first_tree_search),
        7: Algo(7, 'Depth Limited Search', depth_limited_search),
        8: Algo(8, 'IDS', iterative_deepening_search),
        9: Algo(9, 'Best First Search', best_first_graph_search)
    }
    return algo_list


def run_algo() -> None:
    """Function qui tourne l'algo choisi et affiche les résultat"""
    global node
    start_time: float = clock()  # début
    try:
        if args.num in (1, 9):
            node = algo[args.num].func(problem, heuristic)
        elif args.num == 2:
            node = algo[args.num].func(problem, heuristic_ucs)
        else:
            node = algo[args.num].func(problem)
    except KeyError:
        print('Aucun algo ne correspond à ce numéro',flush=True)
        os._exit(-1)

    end_time: float = clock()  # Fin

    path: list = node.path()  # Chemin trouver pour le goal
    path.reverse()  # Retourne la liste
    nb_step: int = 0  # Nombre d'action effectué pour atteindre le goal
    path_cost: int = 0
    for n in path:
        # print(n.state)
        path_cost = n.path_cost
        nb_step += 1
    # print(State(goal_grid))  # Affiche la grille finale
    print("| " + str(args.init).ljust(15) + " | "
          + str(algo[args.num].label).ljust(20)
          + " | " + str(path_cost).ljust(5) + " | "
          + "{0:.18f}".format(end_time - start_time).ljust(10)
          + " | " + str(problem.nb_explored_node).ljust(5)
          + " | " + str(nb_step).ljust(5) + " | ", flush=True)
    os._exit(0)  # arrete le programme à la fin de cette fonction


class Threads(object):
    def __init__(self, func_run_algo):
        self.start: float = clock()  # début de l'exécution
        self.run = func_run_algo
        # Config et démarrage du thread du run algo
        thread_algo = Thread(target=self.run, args=())
        thread_algo.daemon = True

        # Config et démarrage du thread d'arrêt
        thread_stop = Thread(target=self.timeout, args=())
        thread_stop.daemon = True

        thread_algo.start()
        thread_stop.start()

    def timeout(self):  #  function qui gère l'arrêt
        while True:
            if clock() - self.start >= 4:  # condition d'arrêt
                print("| " + str(args.init).ljust(15) + " | "
                      + str(algo[args.num].label).ljust(20)
                      + " | " + " - ".ljust(5) + " | "
                      + "Infini".ljust(20)
                      + " | " + " - ".ljust(5)
                      + " | " + "- ".ljust(5) + " | ",flush=True)
                # os.system("echo {}".format(response))
                os._exit(-1)  # Arrete le programme après le temps spécifié


if __name__ == '__main__':
    args = cmd_line()
    if args.init and args.goal and args.num and args.num != -1:
        initial_grid: list = read_file(args.init)  # Récupération état initial
        goal_grid: list = read_file(args.goal)  # Récupération état final
        initial_state = State(initial_grid)  # Initialisation de l'état initial
        # print(initial_state)  # Affiche la grille initiale
        # print('Postion initiale du smiley: ' +
        #      str(initial_state.position_robot))  # Position initial du smiley

        goal_position = get_diamant_position(goal_grid)  # Position du diamant
        # print('Postion du diamant: ' + str(goal_position))
        problem = LabProblem(initial_state)  # Initialisation du problem
        problem.goal_position = goal_position  # Affectation du goal
        algo: dict = build_algo()  # Dict des algos {key:Algo}
        t = Threads(run_algo)
        sleep(1000000)  # met le thread main en attente pendant ce temps en s
    if args.list:
        get_list_algo()
        sys.exit(0)
