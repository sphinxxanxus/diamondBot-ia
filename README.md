# TP DiamondBot

## Description
Ce Tp d'IA consistait à faire trouver le chemin à un robot pour aller vers un
diamant qui se situe dans le même environnement que lui en utilisant des 
algorithmes d'intelligence artificielle

### Exemple
MMMMMMMM
M   HS M
MM MHCMM
M   M  M
M H HH M
M D HCMM
MMMMMMMM

Ici, l'objectif est de faire déplacé le smiley modéilisé par un **S** vers le diamant qui est modélisé par un **D**

## Modélisation du problèmes
Nous avons modéliser le problème comme suit:
 - **H** signifie **tâche d'huile** qui traversable avec un coût égal à **2** 
 - **M** signifie **Mur** qui n'est pas traversable.
 - ' ' qui signife des zones accessibles avec un coût égal à **1**
 - **D** qui modélise le **Diamant recherché**
 - **$** qui modélise le smiley qui se met sur une tâche d'huile
 - **C** qui siginifie des **Crânes**

*NB: Le smiley ne passe pas sur les crânes dans les mur* 

## Les algorithmes implémentés 
 - A* Graph Search
 - Uniform cost search
 - Breadth First Graph Search
 - Breadth First  Tree Search
 - Depth First Graph Search
 - Depth First Tree Search
 - Depth Limited Search
 - Iterative Deepning Search
 - Best First Search
 
# Utilisation de **diamondbot.py**

Le script **diamondbot.py** est en quelque sorte le main qui est exécuté:

## aide
`python3 diamondbot.py -h` affiche la liste des arguments et à quoi il correspondent

## liste des algorithmes
`python3 diamondbot.py -l`

## exécution d'un level
`python3 diamondbot.py -n numero_de_l_algo -i etat_initial -g etat_final`
### Exemple 
`python3 diamondbot.py -n 1 -i benchs/labInst01.init -g benchs/labInst01.goal`
exécute le premier algorithme qui est **Astar** sur le niveau 1 qui est dans le dossier **benchs**

## Utilisation de **run_all.sh**
Pour exécuter tout les algorithmes sur tout les niveaux qui sont dans un dossier, il faut faire recours au script bash qui est dans **run_all.sh**

Ce script prends entrée le chemin d'un dossier contenant la liste des ficher 
**.init** et **.goal** qui correspondent à un *état initial et état final pour un niveau*. 

Il sort un tableau contenant la liste des résulats des algorithmes par niveau
### aide: help
`bash run_all.sh -h`

### exécution des niveaux d'un dossier
`bash run_all.sh -p chemin_du_dossier`

#### Exemple sur le dossier benchs
`bas run_all.sh -p benchs`


# Perspective
**Faire de ce programme un ensemble de tous les types d'algorithmes implémentables en utilisant le jeu diamondbot pour illustrer**
