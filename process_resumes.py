from openai import OpenAI
import pypandoc
import os
client = OpenAI()

word_docs = []
text_files = []
resumes = []
directory = r"/Users/ellacarter/Documents/PearlHacks/"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if f[-5:] == ".docx":
            word_docs.append(f) #make sure this is the file name
        if f[-4:] == ".txt":
            resumes.append(f)

i = 0
for doc in word_docs:
    name = "resumedoc" + str(i) + ".txt"
    output = pypandoc.convert_file(doc, 'plain', outputfile=name)
    doc_path = directory + name
    resumes.append(doc_path)
    i += 1
    assert output == ""

responses = []

print("resumes are as follows\n" + str(resumes))

print("start processing through openai\n")


for resume in resumes:
    print("This resume is: " + str(resume))
    print("This resume's score is the following: ")
    data = open(resume, 'r').read()
    data = data.replace('\n', '')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "You will be provided a resume. Your task is to score this resume on a scale from 1 - 100 on how qualified they are for the job described in the following paragraph: Need a talented Java developer who can speak French. Only print out the score for how qualified the applicant is."
            },
            {
            "role": "user",
            "content": data
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    print(response.choices[0].message)




