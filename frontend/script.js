const API_URL = "http://127.0.0.1:5000";

const dealerCardsDiv = document.getElementById("dealer-cards");
const playerCardsDiv = document.getElementById("player-cards");
const dealerScoreSpan = document.getElementById("dealer-score");
const playerScoreSpan = document.getElementById("player-score");
const messageEl = document.getElementById("game-message");
const btnStart = document.getElementById("btn-start");
const btnHit = document.getElementById("btn-hit");
const btnStand = document.getElementById("btn-stand");

const welcomeScreen = document.getElementById("welcome-screen");
const gameContainer = document.getElementById("game-container");

const modal = document.getElementById("game-over-modal");
const modalTitle = document.getElementById("modal-title");
const modalMessage = document.getElementById("modal-message");

function enterGame() {
    // Hide welcome screen with a fade out effect (optional, here just hiding)
    welcomeScreen.classList.add("hidden");

    // Show game container
    gameContainer.classList.remove("hidden");

    // Start the game logic
    startGame();
}

async function startGame() {
    try {
        const response = await fetch(`${API_URL}/start`);
        const data = await response.json();

        // Hide modal when starting new game
        modal.classList.add("hidden");

        updateUI(data);
        enableGameButtons(true);
        btnStart.style.display = "none"; // Hide main start button during game
    } catch (error) {
        console.error("Error starting game:", error);
        messageEl.textContent = "Error connecting to backend.";
    }
}

async function hit() {
    try {
        const response = await fetch(`${API_URL}/hit`, { method: "POST" });
        const data = await response.json();
        updateUI(data);
        if (data.game_over) {
            enableGameButtons(false);
            showGameOver(data.message);
        }
    } catch (error) {
        console.error("Error hitting:", error);
    }
}

async function stand() {
    try {
        const response = await fetch(`${API_URL}/stand`, { method: "POST" });
        const data = await response.json();
        updateUI(data);
        enableGameButtons(false);
        showGameOver(data.message);
    } catch (error) {
        console.error("Error standing:", error);
    }
}

function showGameOver(message) {
    // Determine title based on message content
    let title = "Game Over";
    if (message.includes("Win") || message.includes("WIN")) {
        title = "🎉 YOU WIN! 🎉";
        modalTitle.style.color = "#2ecc71"; // Green
    } else if (message.includes("Lose") || message.includes("LOSE") || message.includes("Bust") || message.includes("Dealer Wins")) {
        title = "💀 YOU LOSE 💀";
        modalTitle.style.color = "#e74c3c"; // Red
    } else if (message.includes("Push") || message.includes("Tie")) {
        title = "⚖️ PUSH (TIE) ⚖️";
        modalTitle.style.color = "#f1c40f"; // Yellow
    }

    modalTitle.textContent = title;
    modalMessage.textContent = message;

    // Small delay for effect
    setTimeout(() => {
        modal.classList.remove("hidden");
        btnStart.style.display = "inline-block"; // Show main button again if needed
        btnStart.textContent = "Restart Game";
    }, 500);
}

function updateUI(data) {
    // Render Player Cards
    renderCards(playerCardsDiv, data.player_cards);
    playerScoreSpan.textContent = data.player_score;

    // Render Dealer Cards
    if (data.dealer_cards) {
        renderCards(dealerCardsDiv, data.dealer_cards);
    }

    // Update Score
    if (data.dealer_score) {
        dealerScoreSpan.textContent = data.dealer_score;
    } else if (data.dealer_score_visible) {
        dealerScoreSpan.textContent = data.dealer_score_visible + " + ?";
    }

    // Message - Update on screen text too, but modal takes focus on end
    if (data.message) {
        messageEl.textContent = data.message;
    }
}

function renderCards(container, cards) {
    container.innerHTML = "";
    cards.forEach(card => {
        // Parse card (e.g., "♠10", "♥A")
        // Unicode suits: ♠, ♥, ♦, ♣
        // Rank: 2-10, J, Q, K, A

        // Simple parsing assuming suit is 1 char at start
        const suit = card[0];
        const rank = card.substring(1);

        const cardEl = document.createElement("div");
        cardEl.className = `card ${isRed(suit) ? 'red' : 'black'}`;

        cardEl.innerHTML = `
            <div class="card-top">${rank}${suit}</div>
            <div class="card-center">${suit}</div>
        `;
        container.appendChild(cardEl);
    });

    // If we only have 1 card (dealer start), maybe add a hidden card visual?
    // The backend sends [visible_card]. 
    // If it's the dealer container and we only have 1 card and game is NOT over (check implicitly or logic),
    // we could add a back-of-card. 
    // But getting 'game_over' state here might be cleaner. 
    // However, I'll rely on what's passed. 
    // Since 'start' returns 1 card for dealer, let's append a placeholder if container is dealer and count is 1.
    if (container.id === "dealer-cards" && cards.length === 1) {
        const hiddenCard = document.createElement("div");
        hiddenCard.className = "card hidden";
        container.appendChild(hiddenCard);
    }
}

function isRed(suit) {
    return suit === "♥" || suit === "♦";
}

function enableGameButtons(enabled) {
    btnHit.disabled = !enabled;
    btnStand.disabled = !enabled;
}
