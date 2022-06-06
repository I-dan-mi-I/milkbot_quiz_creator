from xml.etree.ElementTree import Element, SubElement, tostring
import requests

print("Dan_Mi Quiz Creator for MilkBot")

quiz: Element = Element('data')
pos: int = 1

continue_bool = True

while continue_bool:
    print(f"Question {pos}")

    text = input("Question Text\n")
    img = input("Question Image\n")

    answers: list[str] = []
    answers_need: bool = input("Question with answer options (y/yes/n/not)\n").lower() in ["y", "yes"]

    while answers_need:
        ans = input("Answer\n")
        if ans != "":
            answers.append(ans)
        else:
            answers_need = False

    quiz_child = SubElement(quiz, "question")

    if text != "":
        quiz_child_text = SubElement(quiz_child, "text")
        quiz_child_text.text = text
    else:
        break

    if img != "":
        quiz_child_img = SubElement(quiz_child, "img")
        quiz_child_img.text = img

    if answers:
        quiz_child_answers = SubElement(quiz_child, "answer_options")
        for answer in answers:
            quiz_child_answer = SubElement(quiz_child_answers, "answer")
            quiz_child_answer_text = SubElement(quiz_child_answer, "text")
            quiz_child_answer_text.text = answer

    continue_bool: bool = input("Continue (y/yes/n/not)\n").lower() in ["y", "yes"]
    pos += 1

response = requests.post('http://hastebin.com/documents', data=tostring(quiz, encoding='utf8', method='xml'))
if response.status_code == 200:
    print(f"https://www.toptal.com/developers/hastebin/raw/{response.json()['key']}")
