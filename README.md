# Number Guessing Game

## Overview

The Number Guessing Game is a simple and fun web-based game where players try to guess a randomly generated number between 1 and 100 within 7 attempts. The game provides feedback on whether the guess is too high or too low and displays the remaining chances. If the player guesses the correct number or exhausts all chances, the game reveals the result.

## Features

- **Random Number Generation**: A random number between 1 and 100 is generated for each session.
- **Chances**: Players have 7 attempts to guess the correct number.
- **Feedback**: Players receive feedback after each guess, indicating whether their guess is too high or too low.
- **Session Management**: The game uses Django sessions to keep track of the number to guess, remaining chances, and the number of attempts.
- **Play Again Option**: Players can restart the game after finishing a session.
- **User-Friendly Interface**: Clean and intuitive UI with styled buttons and icons for a better gaming experience.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Font Awesome for icons

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game
   ```

2. **Set Up the Environment**
   Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Game**
   Open your browser and go to:
   ```
   http://127.0.0.1:8000/game/
   ```

## File Structure

- `game/views.py`: Contains the logic for the game.
- `templates/home.html`: Home page template with a welcome message.
- `templates/playground.html`: Gameplay template for guessing the number.
- `static/`: Contains CSS files for styling the game.
- `urls.py`: Maps URLs to the corresponding views.

## How to Play

1. Navigate to the home page and click "Let's start the game".
2. On the playground page, enter your guess and click "Submit Guess".
3. Receive feedback on your guess and keep guessing until you win or exhaust all attempts.
4. If you finish a game, click "Play Again!" to start a new session.

## Screenshots

### Home Page
![Home Page](https://github.com/MaheswaranT/Number_Guessing_Game/blob/main/static/img/Home.png)

### Gameplay Page
![Gameplay Page](https://github.com/MaheswaranT/Number_Guessing_Game/blob/main/static/img/Playground.png)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments

- [Font Awesome](https://fontawesome.com/) for providing icons.
- Django for the backend framework.
- Random module for generating random numbers.

## Author

**Maheswaran**  
[GitHub Profile](https://github.com/MaheswaranT)

---
Enjoy playing the Number Guessing Game! Have fun guessing!

