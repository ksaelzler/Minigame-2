import random
import time

def generate_question():
    """Generate a random math question."""
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    answer = eval(question) # Safe for controlled inputs
    return question, answer
  
def ask_question(player):
    """Ask a math question to the player."""
    question, correct_answer = generate_question()
    print(f"{player}, solve: {questoin} = ?")
    
    try:
        answer = int(input("Your answer: "))
        return answer == correct_answer
    except ValueError:
        print("Invalid input! No points for this one.")
        return False

def play_game(players, time_limit=20):
    """Main game loop, players answer questions within a time limit."""
    scores = {player: 0 for player in players}
    start_time = time.time()
    
    while time.time() - start_time < time_limit:
        for player in players:
            if time.time() - start_time >= time_limit:
                break
            if ask_questions(player):
                print("Correct!")
                scores[player] += 1
            else:
                print("Incorrect!")
    return scores
    
    def main():
        print("Welcome to Math Madness!")
        num_players = int(input("Enter number of players (2-4): "))
        
        if num_players < 2 or num_players > 4:
            print("Invalid number of players. Please choose between 2 and 4.")
            return
        
        players = [input(f"Enter name for Player {i+1}: ") for i in range(num_players)]
        
        time_limit = int(input("Enter name for Player {i+1}: ") for i in range(num_players)]
        print("\nGet ready to solve math problems!")
        time.sleep(2)
        
        scores = play_game(players, time_limit)
        display_results(scores)
        
if __name__ == "__main__":
    main()
