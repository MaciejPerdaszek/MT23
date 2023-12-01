import subprocess

runsParameters = [
    ['--PopulationSize= 50', '--NumberOfGenerations= 10', '--MutationRate= 0.5', '--CrossoverRate= 0.5', '--Elitism', '--CrossoverPoints= 8,17'],
    ['--PopulationSize= 50', '--NumberOfGenerations= 10', '--MutationRate= 0.5', '--CrossoverRate= 0.5', '--Elitism', '--CrossoverPoints= 8,17'],
    ['--PopulationSize= 50', '--NumberOfGenerations= 10', '--MutationRate= 0.5', '--CrossoverRate= 0.5', '--Elitism', '--CrossoverPoints= 8,17'],
    ['--PopulationSize= 50', '--NumberOfGenerations= 10', '--MutationRate= 0.5', '--CrossoverRate= 0.5', '--Elitism', '--CrossoverPoints= 8,17'],
    ['--PopulationSize= 50', '--NumberOfGenerations= 10', '--MutationRate= 0.5', '--CrossoverRate= 0.5', '--Elitism', '--CrossoverPoints= 8,17'],
]

with open('output.txt', 'w') as out:
    for currRunParams in runsParameters:
        paramStr = ""
        for param in currRunParams:
            split = str(param).split(' ')
            if len(split) > 1:
                paramStr += (";" + split[1])
            else:
                paramStr += (";" + split[0])

        currRunParams.insert(0, 'arguments.py')
        currRunParams.insert(0, 'python')

        process = subprocess.run(currRunParams, capture_output=True)
        output = process.stdout.decode("utf-8").rstrip()
        out.write(output)
        out.write(paramStr)
        out.write('\n')
