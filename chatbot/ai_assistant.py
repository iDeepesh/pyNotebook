from tkinter import *
from tkinter import ttk

def handle_button():
    ai_responses.configure(state="normal")
    ai_responses.insert(END, "\n"+ human_message.get(1.0, END))
    ai_responses.configure(state="disabled")
    human_message.delete(1.0, END)

def handle_enter(self):
    ai_responses.configure(state="normal")
    ai_responses.insert(END, "\n"+ human_message.get(1.0, END))
    ai_responses.configure(state="disabled")
    human_message.delete(1.0, END)

root = Tk()
root.title("Deepesh AI Assistant")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root, padding="5 5 5 5")
frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)

ai_responses = Text(frame, state="normal", height=50, width=125)
ai_responses.grid(column=0, row=0, sticky=(N, W, E, S), rowspan=3, columnspan=3)
ai_responses.insert("1.0", "This is a test message.")
ai_responses.configure(state="disabled")

human_message = Text(frame, height=20, width=125)
human_message.grid(column=0, row=3, sticky=(N, W, E, S), columnspan=3)
human_message.bind("<Return>", handle_enter)

send_message = ttk.Button(frame, text="Send", command=handle_button)
send_message.grid(row=3, column=3, sticky=(N, W, E, S))

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=3)
frame.rowconfigure(1, weight=3)
frame.rowconfigure(2, weight=3)
frame.rowconfigure(3, weight=3)

root.mainloop()