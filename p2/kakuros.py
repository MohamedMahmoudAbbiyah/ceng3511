from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model


def kakuro_solver(list1):

    mode = cp_model.CpModel()

    #The variables.
    x1 = mode.NewIntVar(1, 9, 'x1')
    x2 = mode.NewIntVar(1, 9, 'x2')
    x3 = mode.NewIntVar(1, 9, 'x3')
    y1 = mode.NewIntVar(1, 9, 'y1')
    y2 = mode.NewIntVar(1, 9, 'y2')
    y3 = mode.NewIntVar(1, 9, 'y3')
    z1 = mode.NewIntVar(1, 9, 'z1')
    z2 = mode.NewIntVar(1, 9, 'z2')
    z3 = mode.NewIntVar(1, 9, 'z3')

    # The constraints
    mode.Add((x1 + x2 + x3) == list1[3])
    mode.Add((y1 + y2 + y3) == list1[4])
    mode.Add((z1 + z2 + z3) == list1[5])
    mode.Add((x1 + y1 + z1) == list1[0])
    mode.Add((x2 + y2 + z2) == list1[1])
    mode.Add((x3 + y3 + z3) == list1[2])

    mode.AddAllDifferent([x1,x2,x3])
    mode.AddAllDifferent([y1, y2, y3])
    mode.AddAllDifferent([z1, z2, z3])
    mode.AddAllDifferent([x1, y1, z1])
    mode.AddAllDifferent([x2, y2, z2])
    mode.AddAllDifferent([x3, y3, z3])

    #here we solve the module
    solver = cp_model.CpSolver()
    status = solver.Solve(mode)

    if status == cp_model.FEASIBLE:
        return [solver.Value(x1), solver.Value(x2), solver.Value(x3),
                solver.Value(y1), solver.Value(y2), solver.Value(y3),
                solver.Value(z1), solver.Value(z2), solver.Value(z3)]




with open("kakuro_input.txt", "r") as inputFile:
    items = []
    for line in inputFile.readlines():
        line = line.replace("\n", "")
        line = line.split(", ")
        for item in line:
            items.append(int(item))


result = kakuro_solver(items)

with open("kakuro_output.txt", "w+")as outputFile:
    outputFile.write("x" + ", " + str(items[0]) + ", " + str(items[1]) + ", " + str(items[2]) + "\n" +
                     str(items[3]) + ", " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2]) + "\n" +
                     str(items[4]) + ", " + str(result[3]) + ", " + str(result[4]) + ", " + str(result[5]) + "\n" +
                     str(items[5]) + ", " + str(result[6]) + ", " + str(result[7]) + ", " + str(result[8]) )
