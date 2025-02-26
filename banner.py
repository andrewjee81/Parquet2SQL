# banner.py
import time
from colorama import init, Fore

# Initialize colorama for Windows compatibility
init(autoreset=True)

class Banner:
    def __init__(self, delay=0.02, color=Fore.GREEN, sig_color=Fore.MAGENTA):
        self.delay = delay
        self.color = color
        self.sig_color = sig_color

    def typewriter_effect(self, text, color):
        """Prints text with a typewriter effect and specified color."""
        for char in text:
            print(color + char + Fore.RESET, end="", flush=True)
            time.sleep(self.delay)
        print()  # Move to the next line after printing

    def display_cli_art(self):
        """Displays the ASCII art banner."""
        print(self.color + "*" * 68 + Fore.RESET)  # Print border line
        art = """
                            ┏┓           ┏┓┏┓┏┓┏┓
                            ┃┃┏┓┏┓┏┓┏┏┓╋┏┛┗┓┃┃┃
                            ┣┛┗┻┛ ┗┫┗┻┗ ┗┗━┗┛┗┻┗┛
                            ┗"""
        sig = """                          @saturnx571\n"""

        self.typewriter_effect(art, self.color)
        self.typewriter_effect(sig, self.sig_color)
        print(self.color + "*" * 68 + Fore.RESET)  # Print border line again
        self.typewriter_effect("\nInitializing...\n", Fore.WHITE)
        time.sleep(3)  # Pause before continuing
