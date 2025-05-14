from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
# from tools.product_tools import (
#     get_all_products,
#     generate_product_table,
#     get_product_by_category,
#     get_product_by_filter
# )
# from tools.brand_tools import (
#     get_all_brands
# )
# from tools.category_tools import (
#     get_all_category
# )
# from tools.order_tools import (
#     place_order,
#     get_order_status,
#     cancel_order
# )


from services.product_service import get_all_products, get_products_by_category, get_products_by_brand, get_products_by_brand_and_category, get_products_by_brand_and_category_min_price_max_price, get_products_by_brand_and_category_min_max_price_rating
from services.category_service import fetch_category_dropdown
from services.brand_service import fetch_brand_dropdown
from services.order_service import add_item_to_cart, view_cart

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# 1. Setup LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

# 2. Tools
tools = [get_all_products,
         get_products_by_category,
         get_products_by_brand,
         get_products_by_brand_and_category,
         get_products_by_brand_and_category_min_price_max_price,
         get_products_by_brand_and_category_min_max_price_rating,
         fetch_category_dropdown,
         fetch_brand_dropdown,
         add_item_to_cart,
         view_cart,
         ]

# 3. Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a smart product assistant. Think step-by-step. Use tools if needed."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# 4. Create ReAct agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# 5. Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True
)

# 6. Initialize empty memory (agent scratchpad)
agent_state = []


# 7. Add workflow for fetching all categories and brands at the start
def fetch_categories_and_brands():
    print("Fetching all categories and brands...")

    # Fetch categories and brands
    categories = get_all_category()
    brands = get_all_brands()

    # Update agent state with categories and brands
    agent_state.append(AIMessage(content="Fetched categories: " + str(categories)))
    agent_state.append(AIMessage(content="Fetched brands: " + str(brands)))

    return categories, brands


# 8. CLI Chat Loop
def chat():
    print("🔵 Welcome to Product Assistant CLI Chat! (Type 'exit' to quit)\n")

    # Fetch categories and brands at the start
    fetch_categories_and_brands()

    while True:
        user_input = input("🧑‍💻 You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break

        try:
            response = agent_executor.invoke({
                "input": user_input,
                "agent_scratchpad": agent_state
            })

            # Update state
            intermediate_steps = response.get("intermediate_steps", [])
            for action, observation in intermediate_steps:
                agent_state.append(AIMessage(content="", additional_kwargs={"tool_calls": [action.tool_call]}))
                agent_state.append(ToolMessage(content=str(observation), tool_call_id=action.tool_call.tool_call_id))

            # Print assistant reply
            print("\n🤖 Assistant:", response['output'])
            print()

        except Exception as e:
            print(f"⚠️ Error: {e}\n")


if __name__ == "__main__":
    chat()
