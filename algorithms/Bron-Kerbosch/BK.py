class Node(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __repr__(self):
        return self.name

AC = Node('AC')
AM = Node('AM')
RO = Node('RO')
RR = Node('RR')
PA = Node('PA')
AP = Node('AP')
TO = Node('TO')
MA = Node('MA')
PI = Node('PI')
BA = Node('BA')
CE = Node('CE')
RN = Node('RN')
PB = Node('PB')
PE = Node('PE')
AL = Node('AL')
SE = Node('SE')
MS = Node('MS')
MT = Node('MT')
GO = Node('GO')
SP = Node('SP')
MG = Node('MG')
RJ = Node('RJ')
ES = Node('ES')
RS = Node('RS')
SC = Node('SC')
PR = Node('PR')

AC.neighbors = [AM, RO]
AM.neighbors = [AC, RR, RO, MT, PA]
RO.neighbors = [AC, AM, MT]
RR.neighbors = [AM, PA]
PA.neighbors = [AM, MT, AP, TO, MA]
AP.neighbors = [PA]
TO.neighbors = [MT, PA, GO, MA, PI, BA]
MA.neighbors = [PA, TO, PI]
PI.neighbors = [TO, MA, BA, CE, PE]
BA.neighbors = [GO, TO, MG, PI, ES, SE, AL, PE]
CE.neighbors = [PI, PE, PB, RN]
RN.neighbors = [CE, PB]
PB.neighbors = [CE, PE, RN]
PE.neighbors = [PI, BA, CE, AL, PB]
AL.neighbors = [BA, SE, PE]
SE.neighbors = [BA, AL]
MS.neighbors = [MT, PR, SP, GO, MG]
MT.neighbors = [RO, AM, PA, TO, GO, MS]
GO.neighbors = [MT, MS, TO, BA, MG]
SP.neighbors = [MS, PR, MG, RJ]
MG.neighbors = [MS, GO, SP, BA, ES, RJ]
RJ.neighbors = [SP, MG, ES]
ES.neighbors = [RJ, MG, BA]
RS.neighbors = [SC]
SC.neighbors = [RS, PR]
PR.neighbors = [MS, SC, SP]

all_nodes = [AC, AM, RO, RR, PA, AP, TO, MA, PI, BA, CE, RN, PB, PE, AL, SE, MS, MT, GO, SP, MG, RJ, ES, RS, SC, PR]


def find_cliques(potential_clique=[], remaining_nodes=[], skip_nodes=[], depth=0):

    if len(remaining_nodes) == 0 and len(skip_nodes) == 0:
        print('This is a clique:', potential_clique)
        return 1

    found_cliques = 0
    for node in remaining_nodes:

        # Try adding the node to the current potential_clique to see if we can make it work.
        new_potential_clique = potential_clique + [node]
        new_remaining_nodes = [n for n in remaining_nodes if n in node.neighbors]
        new_skip_list = [n for n in skip_nodes if n in node.neighbors]
        found_cliques += find_cliques(new_potential_clique, new_remaining_nodes, new_skip_list, depth + 1)

        # We're done considering this node.  If there was a way to form a clique with it, we
        # already discovered its maximal clique in the recursive call above.  So, go ahead
        # and remove it from the list of remaining nodes and add it to the skip list.
        remaining_nodes.remove(node)
        skip_nodes.append(node)
    return found_cliques

total_cliques = find_cliques(remaining_nodes=all_nodes)
print('Total cliques found:', total_cliques)
