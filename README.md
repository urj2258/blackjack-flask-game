# Blackjack Web App

A professional web-based implementation of a Blackjack game using Python (Flask) and a modern Frontend.

## 📁 Structure
- **backend/**: Contains the Flask application and game logic.
    - `app.py`: The entry point for the Flask server.
    - `game_logic.py`: The core Blackjack algorithm (refactored from console version).
- **frontend/**: Contains the User Interface.
    - `index.html`: The game content.
    - `style.css`: Styling for a clean, casino-like look.
    - `script.js`: Handles communication with the backend.

## 🚀 How to Run

### 1. Backend Setup
1.  Navigate to the `backend` folder.
2.  Install requirements:
    ```sh
    pip install -r requirements.txt
    ```
3.  Run the server:
    ```sh
    python app.py
    ```
    The server will start at `http://127.0.0.1:5000`.

### 2. Frontend Setup
1.  Navigate to the `frontend` folder.
2.  Open `index.html` in your web browser. 
    (You can double-click it, or use a live server extension).

## 🎮 How to Play
- Click **Start Game** to deal cards.
- **Hit**: Take another card to get closer to 21.
- **Stand**: End your turn and let the dealer play.
- **Rules**:
    - Bust if > 21.
    - Dealer hits until 17.
    - Standard Blackjack values (J,Q,K = 10, A = 1/11).

## 🛠 Tech Stack
- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
