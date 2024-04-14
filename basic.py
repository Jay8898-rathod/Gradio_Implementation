import gradio as gr

def greet(name):
    print("Hello.."+name+", nice to meet you!!!")

interface = gr.Interface(fn=greet, inputs='text', outputs='text')
interface.launch()