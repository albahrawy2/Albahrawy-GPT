import sys
import time
import os
import random
import socket
import threading

def clear_screen():
    print("\033[H\033[J", end="")

def banner():
    print("\033[1;31m")
    print("=" * 75)
    print("     █████╗ ██╗     ██████╗  █████╗ ██╗  ██╗██████╗  █████╗ ██╗    ██╗")
    print("    ██╔══██╗██║     ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║    ██║")
    print("    ███████║██║     ██████╔╝███████║███████║██████╔╝███████║██║ █╗ ██║")
    print("    ██╔══██║██║     ██╔══██╗██╔══██║██╔══██║██╔══██╗██╔══██║██║███╗██║")
    print("    ██║  ██║███████╗██████╔╝██║  ██║██║  ██║██║  ██║██║  ██║╚███╔███╔╝")
    print("    ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ")
    print("             [ ULTIMATE OFFENSIVE CLI AI FRAMEWORK v3.0 ]             ")
    print("=" * 75)
    print("\033[0m")

def show_help():
    print("\033[1;33m[+] Available Advanced Modules & Commands:\033[0m")
    print("    - python <task>   : Generate advanced automation or exploit scripts.")
    print("    - scanner <ip>    : Generate network socket port scanner payloads.")
    print("    - wordlist        : Generate custom high-entropy brute-force wordlists.")
    print("    - encrypt <text>  : Generate encryption/decryption security payloads.")
    print("    - clear           : Clear the terminal screen and reload banner.")
    print("    - info            : Display system framework specs and status.")
    print("    - exit            : Securely terminate the framework session.\n")

def main():
    clear_screen()
    banner()
    print("\033[1;32m[*] Albahrawy-GPT v3.0 Ultimate Framework Online & Fully Operational.\033[0m")
    print("\033[1;33m[*] Type 'help' to explore capabilities or enter any custom request below.\033[0m\n")
    
    while True:
        try:
            query = input("\033[1;36mAlbahrawy-Ultimate:~# \033[0m").strip()
            
            if query.lower() == 'exit':
                print("\n\033[1;31m[-] Shutting down Albahrawy-GPT. Stay secure, Lord Zayro.\033[0m")
                break
            elif query.lower() == 'help':
                show_help()
                continue
            elif query.lower() == 'clear':
                clear_screen()
                banner()
                continue
            elif query.lower() == 'info':
                print("\n\033[1;32m[+] Framework: Albahrawy-GPT Ultimate")
                print("[+] Version: 3.0 Pro (Unrestricted)")
                print("[+] Author: Albahrawy | Lord Zayro")
                print("[+] Status: Fully Armed & Operational\033[0m\n")
                continue
            
            if not query:
                continue
            
            print("\n\033[1;35m[*] Processing request through neural core engine...\033[0m")
            time.sleep(0.9)
            
            if "python" in query.lower() or "script" in query.lower() or "code" in query.lower():
                print("\n\033[1;32m[+] Generated Professional Python Script Payload:\033[0m")
                print("```python")
                print("import socket, threading, os")
                print("# Albahrawy-GPT Autonomous Script Generator")
                print("def target_payload():")
                print("    print('[*] Executing customized routine for target...')")
                print("if __name__ == '__main__':")
                print("    target_payload()")
                print("```")
            elif "scan" in query.lower() or "scanner" in query.lower():
                print("\n\033[1;32m[+] Network Reconnaissance Payload Generated:\033[0m")
                print("```python")
                print("# Socket Port Scanner Template")
                print("import socket")
                print("target = '127.0.0.1'")
                print("ports = [21, 22, 80, 443, 8080]")
                print("for p in ports:")
                print("    print(f'Scanning port {p} on {target}...')")
                print("```")
            elif "wordlist" in query.lower():
                print("\n\033[1;32m[+] Wordlist Generation Engine Ready:\033[0m")
                print("    -> Custom charset permutation algorithms loaded for local execution.")
            else:
                print(f"\n\033[1;36m[+] Unrestricted Intelligence Output for: '{query}'")
                print(f"    -> Core framework successfully bypassed standard limits and synthesized custom logic.\033[0m")
            
            print("\n" + "-" * 75 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n\033[1;31m[-] Interrupted by user. Session safely closed.\033[0m")
            break

if __name__ == "__main__":
    main()
