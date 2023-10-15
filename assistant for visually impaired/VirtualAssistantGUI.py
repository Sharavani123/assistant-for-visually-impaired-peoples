import tkinter as tk
import threading
import functions  # Import your functions module

class VirtualAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Assistant")
        
        self.init_components()
    
    def init_components(self):
        self.label = tk.Label(self.root, text="Virtual Assistant")
        self.label.pack(pady=10)
        
        self.textbox = tk.Text(self.root, width=40, height=10)
        self.textbox.pack()
        
        self.listen_button = tk.Button(self.root, text="Start Listening", command=self.start_listening)
        self.listen_button.pack(pady=10)
        
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)
        
    def start_listening(self):
        # Start a new thread for listening to user commands
        threading.Thread(target=self.listen_to_user).start()
    
    def listen_to_user(self):
        self.listen_button.config(state=tk.DISABLED)
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.END, "Listening...")
        
        # Call your listening and processing code here
        # For example, you can use your speech recognition code here
        # resp = engine.recognize_speech_from_mic()
        # intent, text = detect.detect_intent_texts(project_id, 0, [resp], 'en')
        
        # Simulate a response for demonstration
        intent = "SampleIntent"
        text = "You said: Hello, how can I help you?"
        
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.END, f"Intent: {intent}\n")
        self.textbox.insert(tk.END, f"Response: {text}\n")
        
        # Perform actions based on intent
        if intent == "SampleIntent":
            response = functions.sample_function()
            self.textbox.insert(tk.END, f"Action: {response}\n")
        
        self.listen_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualAssistantGUI(root)
    root.mainloop()
