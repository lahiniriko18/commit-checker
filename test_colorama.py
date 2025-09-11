from colorama import Fore, Style

print(Fore.RED+"C'est un texte en rouge"+Style.RESET_ALL)

s="Lahiniriko\nNatolotriniavo\nJeremia"
v=any(len(i)==11 for i in s.splitlines())
print(v)