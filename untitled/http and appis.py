import json

import requests
r= requests.get('https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple')
r.status_code
r.text
type(r.text)
import _json
question = json.loads(r.text)
question
{"response_code":0,"results":[{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"Where does the Mac part of the name Fleetwood Mac come from?","correct_answer":"John McVie","incorrect_answers":["Christine McVie","Mac McAnally","David Tennant"]}]}
type (question)
import pprint
pprint.pprint(question)
question['results'][0]['category']
person = {'Name':'John' , 'Age':30}
person_json = json.dumps(person)
person_json
type(person_json)
