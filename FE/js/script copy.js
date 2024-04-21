function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

let initBoardGame = [null, null, null, null, null, null, null, null, null]
let boardGame = initBoardGame

document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('tic-tac-toe-board');
    const undoButton = document.getElementById('undo');
    const restartButton = document.getElementById('restart');
    const closeButton = document.getElementById('close');

    let moves = [];
    let currentPlayer = 'X';
    let gameActive = true;

    // Inizializza la scacchiera
    for (let i = 0; i < 9; i++) {
        let cell = document.createElement('div');
        cell.addEventListener('click', () => makeMove(cell, i));
        board.appendChild(cell);
    }

    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Orizzontali
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Verticali
        [0, 4, 8], [2, 4, 6]            // Diagonali
    ];

    function checkForWin() {
        for (let i = 0; i < winningCombinations.length; i++) {
            const [a, b, c] = winningCombinations[i];
            if (board.children[a].textContent && board.children[a].textContent === board.children[b].textContent && board.children[a].textContent === board.children[c].textContent) {
                gameActive = false;
                drawLine(i); // Funzione per disegnare la linea
                return;
            }
        }
    }

    function drawLine(index) {
        let line = document.createElement('div');
        line.classList.add('line');
        if (index < 3) line.classList.add('horizontal');
        else if (index < 6) line.classList.add('vertical', );
        else line.classList.add('diagonal-' + (index === 6 ? 'down' : 'up'));
        line.style.display = 'block';
        if (index === 0) line.style.top = '50px';
        else if (index === 1) line.style.top = '155px';
        else if (index === 2) line.style.top = '260px';
        else if (index === 3) line.style.left = '50px';
        else if (index === 4) line.style.left = '155px';
        else if (index === 5) line.style.left = '260px';
        board.appendChild(line);
    }

    function makeMove(cell, index) {
        if (!gameActive || cell.textContent || moves.includes(index)) return;
        cell.textContent = currentPlayer;
        moves.push(index);
        boardGame[index] = currentPlayer

        var apiUrl = 'http://127.0.0.1:5000/api/makeMove';


        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ boardGame: boardGame })
        })
        .then(response => response.json())
        .then(async (data) => {
            aiMove = data.aiMove;
            
            console.log("ok")
            document.getElementById('message').textContent = data.message;
            document.getElementById('message').style.color = 'red';
    
            await sleep(1000)
    
            loginContainer.style.display = 'none';
            game.style.display = 'flex';
        })
        .catch(error => {
            console.error('Error:', error);
        });


        // checkForWin();
        if (gameActive) {
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        }
    }

    undoButton.addEventListener('click', () => {
        if (moves.length === 0 || !gameActive) return;
        let lastMove = moves.pop();
        boardGame[lastMove] = null
        board.children[lastMove].textContent = '';
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        gameActive = true;
        // Rimuovi eventuali linee disegnate
        let line = board.querySelector('.line');
        if (line) line.remove();
    });

    restartButton.addEventListener('click', () => {
        moves = [];
        boardGame = initBoardGame;
        gameActive = true;
        Array.from(board.children).forEach(cell => {
            if (cell.className !== 'line') cell.textContent = '';
        });
        currentPlayer = 'X';
        let line = board.querySelector('.line');
        if (line) line.remove();
    });

    closeButton.addEventListener('click', () => {
        board.innerHTML = '';
        document.getElementById('game-container').remove();
    });
});


