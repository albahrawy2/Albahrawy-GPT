import sys
import time
import os

def clear_screen():
    print("\033[H\033[J", end="")

def banner():
    print("\033[1;31m")
    print("=" * 70)
    print("     █████╗ ██╗     ██████╗  █████╗ ██╗  ██╗██████╗  █████╗ ██╗    ██╗")
    print("    ██╔══██╗██║     ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║    ██║")
    print("    ███████║██║     ██████╔╝███████║███████║██████╔╝███████║██║ █╗ ██║")
    print("    ██╔══██║██║     ██╔══██╗██╔══██║██╔══██║██╔══██╗██╔══██║██║███╗██║")
    print("    ██║  ██║███████╗██████╔╝██║  ██║██║  ██║██║  ██║██║  ██║╚███╔███╔╝")
    print("    ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ")
    print("               [ ADVANCED OFFENSIVE CLI AI FRAMEWORK v2.5 ]           ")
    print("=" * 70)
    print("\033[0m")

def show_help():
    print("\033[1;33m[+] Available Modules & Commands:\033[0m")
    print("    - python <query> : Generate custom Python automation or security scripts.")
    print("    - wordlist       : Generate advanced password lists locally.")
    print("    - scan <ip>      : Generate local socket scanning payloads.")
    print("    - clear          : Clear the terminal screen.")
    print("    - info           : Show framework version and status.")
    print("    - exit           : Terminate the session securely.\n")

def main():
    clear_screen()
    banner()
    print("\033[1;32m[*] Albahrawy-GPT Framework successfully loaded and online.\033[0m")
    print("\033[1;33m[*] Type 'help' to view options or enter your prompt below.\033[0m\n")
    
    while True:
        try:
            query = input("\033[1;36mAlbahrawy-Framework:~# \033[0m").strip()
            
            if query.lower() == 'exit':
                print("\n\033[1;31m[-] Shutting down Albahrawy Framework. Stay secure.\033[0m")
                break
            elif query.lower() == 'help':
                show_help()
                continue
            elif query.lower() == 'clear':
                clear_screen()
                banner()
                continue
            elif query.lower() == 'info':
                print("\n\033[1;32m[+] Framework: Albahrawy-GPT\n[+] Version: 2.5 Pro\n[+] Status: Active & Operational\033[0m\n")
                continue
            
            if not query:
                continue
            
            print("\n\033[1;35m[*] Analyzing query and generating advanced payload...\033[0m")
            time.sleep(0.8)
            
            if "python" in query.lower() or "script" in query.lower():
                print("\n\033[1;32m[+] Generated Professional Python Script:\033[0m")
                print("```python")
                print("import os, sys, socket")
                print("def execute_task():")
                print("    print('Target framework initialized successfully.')")
                print("if __name__ == '__main__':")
                print("    execute_task()")
                print("```")
            elif "wordlist" in query.lower():
                print("\n\033[1;32m[+] Wordlist Generation Module Ready:\033[0m")
                print("    - Use built-in generator scripts to build massive lists locally.")
            else:
                print(f"\n\033[1;36m[+] Custom Execution Output for: '{query}'\n    -> Core engine processed successfully with unrestricted capabilities.\033[0m")
            
            print("\n" + "-" * 70 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n\033[1;31m[-] Session terminated by user.\033[0m")
            break

if __name__ == "__main__":
    main()
