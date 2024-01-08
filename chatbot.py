from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'
model =OpenAI(temperature=0.6)


prompt = model("who is aryabhatta ")
print(prompt)