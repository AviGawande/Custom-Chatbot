from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = 'PASTE YOUR OPENAI API KEY HERE'
model =OpenAI(temperature=0.6)


prompt = model("who is aryabhatta ")
print(prompt)