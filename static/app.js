const boardEl = document.getElementById('board')
const statusEl = document.getElementById('status')
const newBtn = document.getElementById('new')

async function fetchState(){
  const res = await fetch('/state')
  return res.json()
}

function renderGrid(grid){
  boardEl.innerHTML = ''
  // grid is rows x cols (6 x 7)
  for(let r=0;r<grid.length;r++){
    for(let c=0;c<grid[0].length;c++){
      const cell = document.createElement('div')
      cell.className = 'cell'
      const v = grid[r][c]
      if(v===0) cell.classList.add('empty')
      if(v===1) cell.classList.add('player')
      if(v===-1) cell.classList.add('ai')
      cell.dataset.col = c
      // make top row clickable to select column
      if(r===0){
        cell.style.cursor='pointer'
        cell.addEventListener('click', ()=> onColumnClick(c))
      }
      boardEl.appendChild(cell)
    }
  }
}

async function onColumnClick(col){
  try{
    const res = await fetch('/move', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({column: col})
    })
    const data = await res.json()
    if(!res.ok){
      statusEl.textContent = data.error || 'error'
      return
    }
    renderGrid(data.grid)
    if(data.winner!==null && data.winner!==undefined){
      if(data.winner===0) statusEl.textContent = 'Draw'
      else if(data.winner===1) statusEl.textContent = 'You win!'
      else statusEl.textContent = 'AI wins :('
    } else {
      statusEl.textContent = `AI moved to column ${data.ai_move + 1}`
    }
  }catch(e){
    statusEl.textContent = 'Network error'
    console.error(e)
  }
}

newBtn.addEventListener('click', async ()=>{
  await fetch('/new', {method:'POST'})
  const s = await fetchState()
  renderGrid(s.grid)
  statusEl.textContent = 'New game'
})

// initial load
fetchState().then(s=>{
  renderGrid(s.grid)
  statusEl.textContent = 'Your turn (red) — click the top cells to play a column.'
})
