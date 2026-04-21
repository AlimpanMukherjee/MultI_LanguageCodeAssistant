# 

import requests
import gradio as gr

url = "http://localhost:11434/api/generate"

def generate_response(prompt):
    data = {
        "model": "codeguru",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)

        print("STATUS:", response.status_code)
        print("RAW:", response.text)

        if response.status_code == 200:
            return response.json()['response']
        else:
            return f"Error: {response.text}"

    except Exception as e:
        return f"Exception: {str(e)}"


interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=7, label="Enter your prompt"),
    outputs=gr.Textbox()
)

interface.launch()