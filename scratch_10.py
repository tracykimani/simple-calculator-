import _json
import random
import requests

url = 'https://opentdb.com/api.php?amount=5&difficulty=easy&type=multiple'
endGame:  ''

while endGame != 'quit':
    r = requests.get (url)
    if r.status_code != 200:
        endGame = input('Sorry, there was a problem retrieving the question. Press enter or try again or type ''quit'' to quit game.')
    else:
         data = _json.loads(r.text)
         question = data['results'][0]['question']
         answers = data ['results'][0]['incorrect_answers']
         correct_answer = data ['results'][0]['correct_answer']
         answers.append(correct_answer)
         random.shuffle(answers)

         print(question + '\n')

         for answer in answers:
             print(answer)

             input('')