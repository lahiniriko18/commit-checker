from colorama import Fore, Style


def generate_report(results):
    total_score = 0
    for result in results:
        print(f"{Fore.CYAN}Commit: {result["commit"]}{Style.RESET_ALL}")
        print(f"Message: {result.get('message').strip()}")
        print(f"Score: {result['score']}/3")

        for item, rule in result["rules"].items():
            color = Fore.GREEN if rule["isValid"] else Fore.RED
            print(f"{item}: {color} {rule["description"]}{Style.RESET_ALL}")

        total_score += result["score"]

    print(
        f"{Fore.YELLOW} \nScore global: {total_score}/{len(results)*3} {Style.RESET_ALL}"
    )
