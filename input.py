# working with file example

import json
# using with to close file when code block exits
with open('input.json', 'r') as input:
    # load json as python object
    obj = json.load(input)
    with open('output.txt', 'w') as output:
        output.write(obj['name'] + "'s Hobbies:\n")
        for hobby in obj['hobbies']:
            output.write(hobby + "\n")