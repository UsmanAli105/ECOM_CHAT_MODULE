import gradio as gr
import logging
from langchain_core.messages import AIMessage, ToolMessage

# Your imports
from main import agent_executor, agent_state

# Setup logger
logging.basicConfig(
    filename="chat_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

# Initialize chat history
chat_history = []

def chat(user_input, history):
    try:
        # Invoke the agent
        response = agent_executor.invoke({
            "input": user_input,
            "agent_scratchpad": agent_state
        })

        # Update agent_state
        intermediate_steps = response.get("intermediate_steps", [])
        for step in intermediate_steps:
            # Log the entire step to see its structure
            logging.info(f"Intermediate Step: {step}")

            # Handle each action and observation in the intermediate steps
            if hasattr(step, 'tool_call'):
                action = step
                observation = action.observation
                agent_state.append(AIMessage(content="", additional_kwargs={"tool_calls": [action.tool_call]}))
                agent_state.append(ToolMessage(content=str(observation), tool_call_id=action.tool_call.tool_call_id))
            else:
                logging.warning(f"Expected 'tool_call' not found in step: {step}")

        bot_output = response.get("output", "No output found")

        # Save the conversation to logs
        logging.info(f"User: {user_input}")
        logging.info(f"Bot: {bot_output}")

        # Update Gradio chat history
        history.append((user_input, bot_output))
        return history, ""

    except Exception as e:
        error_msg = f"⚠️ Error: {str(e)}"
        logging.error(error_msg)
        history.append((user_input, error_msg))
        return history, ""


# Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align: center;'>🤖 Product Assistant</h1>")

    chatbot = gr.Chatbot(
        label="Chat with Assistant",
        bubble_full_width=True,
        show_label=False,
        height=600,
        render_markdown=True,  # Enable Markdown rendering
    )
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align: center;'>🤖 Product Assistant</h1>")

    chatbot = gr.Chatbot(
        label="Chat with Assistant",
        bubble_full_width=True,
        show_label=False,
        height=600,
        render_markdown=True,  # Enabled for Markdown rendering
    )

    with gr.Row():
        with gr.Column(scale=10):
            user_input = gr.Textbox(
                placeholder="Type your message here...",
                show_label=False,
                autofocus=True
            )
        with gr.Column(scale=1, min_width=80):
            send_btn = gr.Button("🚀 Send", variant="primary")

    # Chat logic
    send_btn.click(chat, inputs=[user_input, chatbot], outputs=[chatbot, user_input])
    user_input.submit(chat, inputs=[user_input, chatbot], outputs=[chatbot, user_input])  # allow Enter key


# Launch
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8050)
