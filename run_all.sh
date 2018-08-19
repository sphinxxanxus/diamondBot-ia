#!/usr/bin/bash
# Copyright (C) 2018  alcoy

# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3.0 of the License, or (at
# your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.


usage(){
	echo "Usage: [-p <Chemin du dossier contenant la liste des niveaux>]" 1>&2
	exit 1
}

while getopts ":p:" option; do
	#statements
	case "${option}" in
		p )
			p=${OPTARG}	
		;;
		* )
			usage # pour tout autre paramètre affichage de l'usage
		;;
	esac
done

shift $((OPTIND-1))
if [ -z "${p}" ]; then
	#statements
	usage
	exit 1 # arrête le programme
fi

# Prendre la liste des états initiaux
i=0
while read line; do
	#statements
	init_array[ $i ]="$line"
	((i++))
done < <( ls -1 "$p"/*.init )
# echo ${init_array[19]}

# Prendre la liste des goal états
i=0
while read line; do
	goal_array[ $i ]="$line"
	((i++))
done < <(ls -1 "$p"/*.goal) # subprocessing
i=1
while [[ $i -lt 11 ]]; do
	echo " _____________________________________________________________________________________________"

	echo "| Niveaux               | Algorithme           | Coût  | Temps (s)            | Nb E  | Step  |"
	echo "|_______________________|______________________|_______|______________________|_______|_______|"

	j=0
	while [[ $j -lt ${#goal_array[@]} ]]; do
		#statements
		./diamondbot.py -n $i -i ${init_array[$j]} -g ${goal_array[$j]}
		((j++))
		echo "|_______________________|______________________|_______|______________________|_______|_______|"

	done
	echo " "
	((i++))
done
exit 0
