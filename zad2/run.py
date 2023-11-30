import subprocess

runsParameters = [
    ['-1', '-t 30', '-c 0.999', '-k 0.4', '-i 3000', '-e 9'],
    ['-1', '-t 25', '-c 0.95', '-k 0.35', '-i 3000', '-e 8'],
    ['-1', '-t 20', '-c 0.9', '-k 0.3', '-i 3000', '-e 7'],
    ['-1', '-t 15', '-c 0.8', '-k 0.25', '-i 2500', '-e 6'],
    ['-1', '-t 10', '-c 0.7', '-k 0.2', '-i 1500', '-e 4'],
    ['-1', '-t 5', '-c 0.6', '-k 0.15', '-i 500', '-e 3'],
    ['-1', '-t 0.5', '-c 0.5', '-k 0.1', '-i 100', '-e 1'],

    ['-2', '-t 10', '-c 0.999', '-k 0.4', '-i 1200', '-e 9'],
    ['-2', '-t 5', '-c 0.95', '-k 0.35', '-i 1100', '-e 8'],
    ['-2', '-t 4', '-c 0.9', '-k 0.3', '-i 1000', '-e 7'],
    ['-2', '-t 3', '-c 0.8', '-k 0.25', '-i 800', '-e 6'],
    ['-2', '-t 2', '-c 0.7', '-k 0.2', '-i 600', '-e 4'],
    ['-2', '-t 0.5', '-c 0.6', '-k 0.15', '-i 400', '-e 3'],
    ['-2', '-t 0.05', '-c 0.5', '-k 0.1', '-i 200', '-e 1'],
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

        currRunParams.insert(0, 'simulation.py')
        currRunParams.insert(0, 'python')

        process = subprocess.run(currRunParams, capture_output=True)
        output = process.stdout.decode("utf-8").rstrip()
        out.write(output)
        out.write(paramStr)
        out.write('\n')
