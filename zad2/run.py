import subprocess

runsParameters = [
    ['-1', '-t 0.5', '-c 0.999', '-k 0.1', '-i 3000', '-e 7']
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
        currRunParams.insert(0, 'python3')

        process = subprocess.run(currRunParams, capture_output=True)
        output = process.stdout.decode("utf-8").rstrip()
        out.write(output)
        out.write(paramStr)
