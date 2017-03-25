from watson import get_feelings
from pprint import pprint

results = []
with open('test.txt', 'r') as tests:
    for line in tests:
        try:
            data = {'text': line.strip(), 'analysis': get_feelings(line.strip())}
            results.append(data)
        except Exception as e:
            print(e)
            print(line)
pprint(results)