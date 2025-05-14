from tools import (
    get_brands, get_category, get_all_products,
    get_products_by_category, get_products_by_brand,
    get_products_by_brand_and_category,
    get_products_by_brand_and_category_min_price_max_price,
    get_products_by_brand_and_category_min_max_price_rating,
    add_to_cart, view_my_cart, submit_cart, check_order_status,
    get_userid_and_token
)
import os
import openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor


openai.api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)




# Gather all tools
all_tools = [
    get_brands, get_category, get_all_products,
    get_products_by_category, get_products_by_brand,
    get_products_by_brand_and_category,
    get_products_by_brand_and_category_min_price_max_price,
    get_products_by_brand_and_category_min_max_price_rating,
    add_to_cart, view_my_cart, submit_cart, check_order_status,
    get_userid_and_token
]

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a smart product assistant. Think step-by-step. Use tools if needed."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(
    llm=llm,
    tools=all_tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=all_tools,
    verbose=True,
    return_intermediate_steps=True
)