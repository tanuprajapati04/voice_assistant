from voice_assistant import VoiceAssistant
import sys

def main():
    assistant = VoiceAssistant()
    
    print("=" * 50)
    print("🎤 Voice Assistant Starting...")
    print("=" * 50)
    
    assistant.greet()
    
    assistant.show_help()
    
    print("\n🎤 Speak your command (or type 'exit' to quit):")
    print("-" * 50)
    
    # Main loop
    running = True
    while running:
        try:
            user_input = input("Press Enter to speak or type 'exit' to quit: ")
            
            if user_input.lower() == 'exit':
                assistant.speak("Goodbye!")
                break
            
            
            command = assistant.listen()
            
            if command:
                if assistant.process_command(command):
                    running = False
        
        except KeyboardInterrupt:
            assistant.speak("Goodbye!")
            running = False
            break
    
    print("\n" + "=" * 50)
    print("Voice Assistant Shutdown")
    print("=" * 50)

if __name__ == "__main__":
    main()