from voice_assistant import VoiceAssistant

def main():
    assistant = VoiceAssistant()
    
    print("=" * 50)
    print("💬 Text Assistant Starting...")
    print("Type 'exit' to quit")
    print("=" * 50)
    
    assistant.greet()
    assistant.show_help()
    
    while True:
        try:
            command = input("\nYour command: ").lower().strip()
            
            if command in ['exit', 'quit', 'stop']:
                assistant.speak("Goodbye!")
                break
            
            if assistant.process_command(command):
                break
        
        except KeyboardInterrupt:
            assistant.speak("Goodbye!")
            break

if __name__ == "__main__":
    main()