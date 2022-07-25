# Artificial-Potential-Field-pathplanning-for-static-maps
Using Artificial Potential Field to solve path planning problems and considering different traversals (only diagonal, diagonal else straight, diagonal and straight)

-------- REQUIREMENTS --------

1.Python 3
2.Networkx
3.Matplotlib

-------- CODE DESCRIPTION --------

Maps(n x n) are represented as:
	1 - free space
	0 - obstacle
	(0, 0) - start
	(n, n) - destination 
	
PotentialAssignment.py - takes maps as input and assigns potential to each node from destination node to its subsequent neighbour slowly reducing the potential value

DiagonalPathGen.py - traverses only through diagonal nodes
DiagonalelseStraightPathGen.py - traverses through diagonal nodes if not possible it choses lateral movement
Diagonal&StraightPathGen.py - traverses through any neighbour node


-------- HOW TO RUN APF FOR DIFFERENT MAPS --------

1. Copy Map content to map.txt
2. Run PotentialAssignment.py to get potential map in map_out.txt
3. Run DiagonalPathGen.py to get paths with only diagonal traversal in paths.txt
4. Run DiagonalelseStraightPathGen.py to get paths with diagonal traversal else straight traversal in paths.txt
5. Run Diagonal&StraightPathGen.py to get paths with both diagonal traversal and straight traversal in paths.txt
(Note: For some maps Diagonal&StraightPathGen.py may be memory bound as it can generate millions of paths 
so if memory error occurs Run Diagonal&StraightPathGen100.py this generates about 100 random paths in paths.txt)
6. For Visualization copy one path from paths.txt into "PATH1" variable in GUI.py and Run 

