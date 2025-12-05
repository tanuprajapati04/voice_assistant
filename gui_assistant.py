import tkinter as tk
from tkinter import scrolledtext, messagebox
from voice_assistant import VoiceAssistant
import threading

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("600x500")
        
        self.assistant = VoiceAssistant()
        
        self.create_widgets()
        
        self.update_display("Assistant", "Voice Assistant Started!")
        self.assistant.greet()
    
    def create_widgets(self):
        
        title_label = tk.Label(
            self.root, 
            text="🎤 Voice Assistant", 
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=10)
        
        
        self.display_area = scrolledtext.ScrolledText(
            self.root, 
            wrap=tk.WORD, 
            width=70, 
            height=20,
            font=("Arial", 10)
        )
        self.display_area.pack(padx=20, pady=10)
        
    
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.listen_btn = tk.Button(
            button_frame,
            text="🎤 Speak Command",
            command=self.listen_command,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12),
            width=15
        )
        self.listen_btn.pack(side=tk.LEFT, padx=5)
       
        self.text_btn = tk.Button(
            button_frame,
            text="⌨️ Text Command",
            command=self.text_command,
            bg="#2196F3",
            fg="white",
            font=("Arial", 12),
            width=15
        )
        self.text_btn.pack(side=tk.LEFT, padx=5)
        
    
        self.help_btn = tk.Button(
            button_frame,
            text="❓ Help",
            command=self.show_help,
            bg="#FF9800",
            fg="white",
            font=("Arial", 12),
            width=15
        )
        self.help_btn.pack(side=tk.LEFT, padx=5)
        
        # Exit button
        self.exit_btn = tk.Button(
            button_frame,
            text="❌ Exit",
            command=self.exit_app,
            bg="#f44336",
            fg="white",
            font=("Arial", 12),
            width=15
        )
        self.exit_btn.pack(side=tk.LEFT, padx=5)
    
    def update_display(self, sender, message):
        """Update the display area with messages"""
        self.display_area.insert(tk.END, f"{sender}: {message}\n")
        self.display_area.see(tk.END)
        self.root.update()
    
    def listen_command(self):
        """Handle voice command in a separate thread"""
        def listen_thread():
            self.listen_btn.config(state=tk.DISABLED)
            self.update_display("System", "Listening... Speak now!")
            command = self.assistant.listen()
            if command:
                self.update_display("You", command)
                if self.assistant.process_command(command):
                    self.root.after(1000, self.exit_app)
            self.listen_btn.config(state=tk.NORMAL)
        
        threading.Thread(target=listen_thread, daemon=True).start()
    
    def text_command(self):
        """Handle text command input"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Enter Command")
        dialog.geometry("400x150")
        
        tk.Label(dialog, text="Enter your command:", font=("Arial", 12)).pack(pady=10)
        
        entry = tk.Entry(dialog, width=50, font=("Arial", 12))
        entry.pack(pady=10)
        entry.focus()
        
        def submit():
            command = entry.get().strip().lower()
            if command:
                dialog.destroy()
                self.update_display("You", command)
                if self.assistant.process_command(command):
                    self.root.after(1000, self.exit_app)
        
        tk.Button(dialog, text="Submit", command=submit, bg="#4CAF50", fg="white").pack(pady=10)
    
    def show_help(self):
        """Show help information"""
        help_text = """
        Available Commands:
        • Say/Type 'time' - Get current time
        • Say/Type 'date' - Get today's date
        • Say/Type 'search [query]' - Search on Google
        • Say/Type 'open [website]' - Open YouTube, Google, etc.
        • Say/Type 'hello' or 'hi' - Greet the assistant
        • Say/Type 'exit', 'quit', or 'stop' - Close the assistant
        
        """
        messagebox.showinfo("Voice Assistant Help", help_text)
    
    def exit_app(self):
    
        self.assistant.speak("Goodbye!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()