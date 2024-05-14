from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain_openai import ChatOpenAI
 
_ = load_dotenv(find_dotenv())

with open("app/openai-prompting.txt") as f:
    text = f.read()

template = """
{text}

_______________________________________

Based on the above instructions help me write a good prompt TEMPLATE.

This template should be a python string template that can later be formatted. 

The variabes of the template should only be enclosed in curly braces.

And the most important part you are not allowed to the following list of characters in this template: < >

An example of how variables can be provided to this template is Question: {{question}} Answer: {{answer}} 

(Note this is just an example of how to format the template please do not include it in the final prompt)


Go through the objective and determine the input variables required along with the prompt. 

Return your answer in the following format:

```prompt
...
```

This is my objective:

{objective}

Return only the python string template. Do not include anything else.
"""

prompt = PromptTemplate.from_template(template)
prompt = prompt.partial(text=text)
chain = prompt | ChatOpenAI(temperature=0) | StrOutputParser()