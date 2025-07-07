from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config.settings import llm
from prompts.prompt2 import template2

chain2 = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        input_variables=["summary", "fallacies_df"],
        template=template2
    )
)