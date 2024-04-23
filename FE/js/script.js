function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function initBoardGame(){
    return [null, null, null, null, null, null, null, null, null]
}

function setWinner(winner){
    var apiUrl = 'http://127.0.0.1:5000/api/setResultMatch';
    // Get item
    let username = sessionStorage.getItem('username');

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            username: username,
            winner: winner
        })//TODO change username
    })
    .then(response => response.json())
    .catch(error => {
        console.error('Error:', error);
    });
}

let boardGame = initBoardGame()

const winningCombinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Orizzontali
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Verticali
    [0, 4, 8], [2, 4, 6]            // Diagonali
];

document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('tic-tac-toe-board');
    const undoButton = document.getElementById('undo');
    const restartButton = document.getElementById('restart');
    const closeButton = document.getElementById('close');
    const game = document.getElementById("game-container")
    const loginContainer = document.getElementsByClassName('login-container')[0]

    let moves = [];
    let currentPlayer = 'O';
    let gameActive = true;

    // Inizializza la scacchiera
    for (let i = 0; i < 9; i++) {
        let cell = document.createElement('div');
        cell.addEventListener('click', () => makeMove(cell, i));
        board.appendChild(cell);
    }

    

    function checkForWin() {
        for (let i = 0; i < winningCombinations.length; i++) {
            const [a, b, c] = winningCombinations[i];
            if (board.children[a].textContent && board.children[a].textContent === board.children[b].textContent && board.children[a].textContent === board.children[c].textContent) {
                gameActive = false;
                drawLine(i); // Funzione per disegnare la linea
                setWinner(board.children[a].textContent == 'X' ? 'AI' : 'HUMAN')
                return;
            }
        }
    }

    function checkForDraw() {
        console.log(boardGame)
        for (let i = 0; i < 9; i++){
            if (boardGame[i] == null) return;
        }

        setWinner('DRAW')
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
            if (aiMove != null){
                board.children[aiMove].textContent = 'X';
                moves.push(aiMove);
                boardGame[aiMove] = 'X'
            }
            

            checkForWin()
            checkForDraw()

        })
        .catch(error => {
            console.error('Error:', error);
        });


        
    }

    undoButton.addEventListener('click', () => {
        if (moves.length === 0 || !gameActive) return;
        let lastMove = moves.pop();
        boardGame[lastMove] = null
        board.children[lastMove].textContent = '';

        lastMove = moves.pop();
        boardGame[lastMove] = null
        board.children[lastMove].textContent = '';

        // Rimuovi eventuali linee disegnate
        let line = board.querySelector('.line');
        if (line) line.remove();

        gameActive = true;

    });

    restartButton.addEventListener('click', () => {
        moves = [];
        boardGame = initBoardGame();
        gameActive = true;
        Array.from(board.children).forEach(cell => {
            if (cell.className !== 'line') cell.textContent = '';
        });
        currentPlayer = 'O';
        let line = board.querySelector('.line');
        if (line) line.remove();
    });

    closeButton.addEventListener('click', () => {
        boardGame = initBoardGame();
        moves = [];
        for (let i = 0; i < board.children.length; i++){
            board.children[i].textContent = '';
        }
        gameActive = True;
        document.getElementById('message').textContent = '';
        sessionStorage.removeItem('username');
        let line = board.querySelector('.line');
        if (line) line.remove();
        game.style.display = 'none';
        loginContainer.style.display = 'block';
    });
});


