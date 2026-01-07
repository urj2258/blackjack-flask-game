from flask import Flask, jsonify, session, request
from flask_cors import CORS
import game_logic

app = Flask(__name__, static_folder='../frontend', static_url_path='')
# Key for session signing - needed for Flask sessions to work
app.secret_key = 'super_secret_blackjack_key' 
CORS(app) # Enable CORS for frontend communication

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/start', methods=['GET'])
def start_game():
    # Setup new game
    deck, player, dealer = game_logic.setupGame()
    
    # Store state in session
    session['deck'] = deck
    session['player'] = player
    session['dealer'] = dealer
    session['game_over'] = False
    
    # Calculate initial scores
    player_score = game_logic.cardValues(player)
    dealer_score_initial = game_logic.cardValues([dealer[1]]) # Show only one card initially? 
    # Actually, standard blackjack shows one up card. 
    # But for simplicity and matching the logic: 
    # The original code hid the first card (index 0) and showed index 1?
    # Original: "printCard(dealer, hideCard = True)" -> hides index 0.
    
    return jsonify({
        'player_cards': player,
        'dealer_cards': [dealer[1]], # Send only visible card
        'player_score': player_score,
        'dealer_score_visible': game_logic.cardValues([dealer[1]]), 
        'game_over': False,
        'message': "Game Started! Hit or Stand?"
    })

@app.route('/hit', methods=['POST'])
def hit():
    if 'deck' not in session or session.get('game_over'):
        return jsonify({'error': 'Game over or not started'}), 400

    deck = session['deck']
    player = session['player']
    
    # Draw card
    if deck:
        player.append(deck.pop())
    
    score = game_logic.cardValues(player)
    
    game_over = False
    message = "Hit or Stand?"
    
    if score > 21:
        game_over = True
        message = "Bust! You went over 21."
        session['game_over'] = True
    
    session['deck'] = deck # Save changes
    session['player'] = player
    
    return jsonify({
        'player_cards': player,
        'player_score': score,
        'game_over': game_over,
        'message': message
    })

@app.route('/stand', methods=['POST'])
def stand():
    if 'deck' not in session or session.get('game_over'):
        return jsonify({'error': 'Game over or not started'}), 400
        
    deck = session['deck']
    dealer = session['dealer']
    player = session['player']
    
    # Dealer plays
    game_logic.dealerTurn(dealer, deck)
    
    dealer_score = game_logic.cardValues(dealer)
    player_score = game_logic.cardValues(player)
    
    result = ""
    if dealer_score > 21:
        result = "Dealer Bust! You Win!"
    else:
        outcome = game_logic.comparison(dealer_score, player_score)
        if outcome == "WIN":
            result = "You Win!"
        elif outcome == "PUSH":
            result = "Push (Tie)."
        else:
            result = "Dealer Wins."
            
    session['game_over'] = True
    session['deck'] = deck
    session['dealer'] = dealer
    
    return jsonify({
        'player_cards': player,
        'dealer_cards': dealer, # Reveal all
        'player_score': player_score,
        'dealer_score': dealer_score,
        'game_over': True,
        'message': result
    })

if __name__ == '__main__':
    app.run(debug=True)
