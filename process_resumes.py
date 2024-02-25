from openai import OpenAI
import pypandoc
import os
client = OpenAI()

# Example file:
docxFilename = r"/Users/ellacarter/Documents/resume.docx"
output = pypandoc.convert_file(docxFilename, 'plain', outputfile="resume2.txt")
assert output == ""
   
# Variable contains the path to the file
path = r"/Users/ellacarter/Documents/resume2.txt"
# The file is read and its data is stored
data = open(path, 'r').read()
 
# Replacing all occurrences of newline in data with ''
data = data.replace('\n', '')
 
# Displaying the resultant data
#print(data)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided a resume. Your task is to score this resume on a scale from 1- 10 on how qualified they are for the job described in the following paragraph: Need a talented Java developer who can speak French"
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
