from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config.settings import llm
from prompts.prompt1 import template1

chain1 = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        input_variables=["content", "fallacies_df"],
        template=template1
    )
)