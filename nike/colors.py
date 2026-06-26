# -*- coding: utf-8 -*-
"""
Module de couleurs pour en-têtes et texte dans le terminal (Codes ANSI).
Vous pouvez importer ce fichier ou copier son contenu au début de votre script.
"""

# --- 1. COULEURS DE BASE (TEXTE) ---
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
REVERSE = "\033[7m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# --- 2. COULEURS CLAIRES / HAUTE INTENSITÉ (TEXTE) ---
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# --- 3. COULEURS D'ARRIÈRE-PLAN (BACKGROUND) ---
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"


# --- 4. FONCTIONS PRATIQUES POUR LES EN-TÊTES ---

def rgb_text(r, g, b, text):
    """Retourne un texte en couleur True Color (RGB)."""
    return f"\033[38;2;{r};{g};{b}m{text}{RESET}"

def rgb_bg(r, g, b, text):
    """Retourne un texte avec un fond True Color (RGB)."""
    return f"\033[48;2;{r};{g};{b}m{text}{RESET}"

def print_header(title, color=BRIGHT_CYAN, style=BOLD):
    """Affiche un en-tête stylisé pour vos scripts."""
    width = 60
    print(f"{color}{style}" + "="*width)
    print(f" {title.center(width - 2)} ")
    print("="*width + f"{RESET}")


# --- 5. DEMONSTRATION AUTOMATIQUE (Si exécuté directement) ---
if __name__ == "__main__":
    print_header("DEMONSTRATION DES COULEURS TERMINAL", color=BRIGHT_GREEN)
    
    print(f"{BOLD}Styles de base :{RESET}")
    print(f"  {BOLD}Texte en Gras{RESET}")
    print(f"  {UNDERLINE}Texte Souligné{RESET}")
    print(f"  {REVERSE} Texte Inversé (Idéal pour des tags) {RESET}\n")

    print(f"{BOLD}Couleurs Standard :{RESET}")
    print(f"  {RED}Rouge{RESET}  {GREEN}Vert{RESET}  {YELLOW}Jaune{RESET}  {BLUE}Bleu{RESET}  {MAGENTA}Magenta{RESET}  {CYAN}Cyan{RESET}\n")

    print(f"{BOLD}Couleurs Haute Intensité :{RESET}")
    print(f"  {BRIGHT_RED}Rouge Cl.{RESET}  {BRIGHT_GREEN}Vert Cl.{RESET}  {BRIGHT_YELLOW}Jaune Cl.{RESET}  {BRIGHT_BLUE}Bleu Cl.{RESET}\n")

    print(f"{BOLD}Exemples d'Arrière-plans :{RESET}")
    print(f"  {BG_RED}{WHITE} Fond Rouge {RESET} {BG_GREEN}{BLACK} Fond Vert {RESET} {BG_BLUE}{WHITE} Fond Bleu {RESET}\n")

    print(f"{BOLD}Mode True Color Moderne (RGB 24-bit) :{RESET}")
    orange_text = rgb_text(255, 165, 0, "Cet orange est généré en RGB natif !")
    purple_badge = rgb_bg(138, 43, 226, f"{WHITE} BADGE VIOLET RGB {RESET}")
    print(f"  {orange_text}")
    print(f"  {purple_badge}\n")
    
    print_header("FIN DE LA DEMO - PRÊT À L'EMPLOI", color=BRIGHT_YELLOW)