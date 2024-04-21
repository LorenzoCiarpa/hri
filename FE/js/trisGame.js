export function checkForWin(board, winningCombinations, gameActive) {
    for (let i = 0; i < winningCombinations.length; i++) {
        const [a, b, c] = winningCombinations[i];
        if (board.children[a].textContent && board.children[a].textContent === board.children[b].textContent && board.children[a].textContent === board.children[c].textContent) {
            gameActive = false;
            drawLine(i); // Funzione per disegnare la linea
            return;
        }
    }
}

export function drawLine(board, index) {
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

export function undo(board, moves, currentPlayer, gameActive) {
    if (moves.length === 0 || !gameActive) return;
    let lastMove = moves.pop();
    board.children[lastMove].textContent = '';
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    gameActive = true;
    // Rimuovi eventuali linee disegnate
    let line = board.querySelector('.line');
    if (line) line.remove();
}

export function restart(board, gameActive, currentPlayer) {
    moves = [];
    gameActive = true;
    Array.from(board.children).forEach(cell => {
        if (cell.className !== 'line') cell.textContent = '';
    });
    currentPlayer = 'X';
    let line = board.querySelector('.line');
    if (line) line.remove();
}

export function close(board) {
    board.innerHTML = '';
    document.getElementById('game-container').remove();
}

 