from flask import Flask, render_template, request, session, redirect, url_for
import random
import string

# Assuming categories.py contains the original English categories and their translations
from categories import categories, translations

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session data
MAX_SCORE = 10  # Example value

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'players' not in session:
        session['players'] = {}
    if 'won_categories' not in session:
        session['won_categories'] = {}
    if 'max_score_reached' not in session:
        session['max_score_reached'] = False


    # Retrieve the last generated letter, or generate a new one if it doesn't exist
    random_letter = session.get('last_letter', random.choice(string.ascii_uppercase))
    selected_languages = session.get('selected_languages', ['English'])
    random_category = session.get('last_category')
    translated_categories = session.get('last_translated_categories', {})

    # Check if max score is reached and pass it to the template
    max_score_reached = session.get('max_score_reached', False)

    # Retrieve or set the default state of the random category checkbox
    random_category_checkbox = session.get('random_category_checkbox', False)

    if request.method == 'POST':
        if request.form.get('new_letter'):
            # Generate a new letter
            random_letter = random.choice(string.ascii_uppercase)
            session['last_letter'] = random_letter

            # Update the state of the random category checkbox
            random_category_checkbox = 'random_category' in request.form
            session['random_category_checkbox'] = random_category_checkbox

            if random_category_checkbox:
                # Generate a new random category
                base_category = random.choice(categories)
                random_category = base_category
                translated_categories = {}
                selected_languages = request.form.getlist('languages')

                # Translate to other selected languages if necessary
                if len(selected_languages) > 1 or 'English' not in selected_languages:
                    for lang in selected_languages:
                        translated_categories[lang] = translations[lang].get(base_category, "N/A")
                if 'English' in selected_languages and len(selected_languages) == 1:
                    translated_categories = {}

                # Store the new values in the session
                session['last_category'] = random_category
                session['last_translated_categories'] = translated_categories
                session['selected_languages'] = selected_languages

    session.modified = True
    return render_template('index.html', letter=random_letter, 
                           languages=translations.keys(), 
                           selected_languages=selected_languages, 
                           players=session['players'], 
                           won_categories=session['won_categories'], 
                           random_category=random_category,
                           translated_categories=translated_categories, 
                           random_category_checkbox=random_category_checkbox,
                           max_score_reached=session['max_score_reached'])


@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form.get('player_name')
    if player_name:
        session['players'][player_name] = 0  # Start with a score of 0
        session.modified = True  # Indicate that the session needs to be saved
    return redirect(url_for('index'))


@app.route('/remove_player/<player_name>')
def remove_player(player_name):
    if player_name in session['players']:
        session['players'].pop(player_name, None)
        # After removing a player, re-evaluate the max_score_reached flag
        session['max_score_reached'] = any(score >= MAX_SCORE for score in session['players'].values())
        session.modified = True  # Indicate that the session needs to be saved
    return redirect(url_for('index'))

@app.route('/update_score/<player_name>')
def update_score(player_name):
    score = request.args.get('score', 0, type=int)
    if player_name in session['players']:
        session['players'][player_name] += score
        # Check if any player has reached or exceeded the max score
        session['max_score_reached'] = any(score >= MAX_SCORE for score in session['players'].values())
        session.modified = True
    return redirect(url_for('index'))

@app.route('/reset_scores')
def reset_scores():
    for player in session['players']:
        session['players'][player] = 0
    # Reset the max_score_reached flag as all scores are reset
    session['max_score_reached'] = False
    session.modified = True
    return redirect(url_for('index'))

@app.route('/reset_player_score/<player_name>')
def reset_player_score(player_name):
    if player_name in session['players']:
        session['players'][player_name] = 0
        # Re-evaluate the max_score_reached flag after resetting the player's score
        session['max_score_reached'] = any(score >= MAX_SCORE for score in session['players'].values())
        session.modified = True
    return redirect(url_for('index'))

@app.route('/refresh')
def refresh():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    