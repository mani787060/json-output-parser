from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


# prompt = template.format(topic='black hole')
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result['name'])


# Using chain to do the same thing in simple way

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)



# So, the problem in json_output_parser is that it expects the model's response to be in a specific JSON format. If the model's response does not adhere to this format, the parser will fail to extract the desired information.  

# Also, the biggest problem of json_output_parser is that we cannot enforce schema on the model's response. So, if the model's response is not in the expected format, we will get an error. This is where structured output parsers come into play.
