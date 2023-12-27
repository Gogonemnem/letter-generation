
# Pim Pam Pet / Ratefix Letter Generator

## Description
This project is a web-based letter generation game where players can generate random letters and categories in multiple languages. Players can score points by coming up with words that match the generated letter and category within a set time limit.

## Features
- Random letter generation
- Category selection and random category generation
- Support for multiple languages
- Player score tracking
- Countdown timer
- Celebration animations when a player reaches the max score

## Installation
To run this project locally, you'll need to have Python and Flask installed.

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/letter-generation-game.git
   ```
2. Navigate to the cloned directory:
   ```
   cd letter-generation-game
   ```
3. Install the required Python packages (preferably in a virtual environment):
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```
   python app.py
   ```

## Usage
Once the application is running, navigate to `http://localhost:5000` in your web browser to start the game.

- Add players using the "Add Player" button.
- Generate a new letter and optionally a random category.
- Each player tries to come up with words that start with the given letter and belong to the selected category.
- Update scores for each player with the `+1` and `-1` buttons.
- The game celebrates when a player reaches the maximum score.

## Customization
You can customize the categories and languages by modifying the `categories.py` file.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

