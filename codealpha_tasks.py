import random

def play_hangman():

    words = ["python", "code", "alpha", "flask", "numpy" , "Ahmad" ]
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0

    max_incorrect = 6
    
    print("==========================================")
    print("      --- Task 1: Hangman Game ---")
    print("==========================================")
    
    while incorrect_guesses < max_incorrect:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f" Current word: {display_word.strip()}")
        print(f"Attempts left: {max_incorrect - incorrect_guesses}")
        
        if "_" not in display_word:
            print("🎉 Congratulations! You won!")
            return
            
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")
            
    print(f"❌ Game Over! The word was: '{secret_word}'")

def track_portfolio():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 400,
        "AMZN": 175
    }
    
    print("==========================================")
    print("  --- Task 2: Stock Portfolio Tracker ---")
    print("==========================================")
    print("Available stocks and prices:", stock_prices)
    portfolio = {}
    
    while True:
        stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break
        if stock_name not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
        except ValueError:
            print("Please enter a valid number")
            continue
            
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    total_investment = 0
    print("--- Stock Portfolio Summary ---")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"Stock: {stock} | Qty: {qty} | Price: ${price} | Total: ${value}")
        
    print(f"💰 Total Portfolio Value: ${total_investment}")
    
    with open("portfolio_report.txt", "w", encoding="utf-8") as f:
        f.write(f"Total Investment Value: ${total_investment}\n")
    print("Report saved to 'portfolio_report.txt'.")

def simple_chatbot():
    print("==========================================")
    print("      --- Task 4: Basic Chatbot ---")
    print("==========================================")
    print("Bot: Hi! I am your simple chatbot. (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["hello", "hi"]:
            print("Bot: Hi there! How can I help you today?")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I'm fine, thanks for asking!")
        elif user_input in ["bye", "goodbye"]:
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: Sorry, I am a simple rule-based bot and didn't understand that.")

def main():
    while True:
        print("==========================================")
        print("    CodeAlpha Python Tasks Selector")
        print("==========================================")
        print("1. Task 1: Hangman Game")
        print("2. Task 2: Stock Portfolio Tracker")
        print("3. Task 4: Basic Chatbot")
        print("4. Exit")
        
        choice = input("Select a task to run (1-4): ")


        if choice == '1':
            play_hangman()
        elif choice == '2':
            track_portfolio()
        elif choice == '3':
            simple_chatbot()
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 4.")

if __name__ == "__main__":
    main()
