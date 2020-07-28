// setup for any 2d canvas script
const canvas = document.getElementById('canvas');
const undo = document.getElementById('undo')
const ctx = canvas.getContext('2d')

let painting = false;

// store all of the points of the canvas in the curves array
let curves = [];
let curve = [];

function getMousePos(canvas, evt) {
    let rect = canvas.getBoundingClientRect();
    return {
      x: parseInt(evt.clientX - rect.left),  // we do not want fractional pixels for our mouse position
      y: parseInt(evt.clientY - rect.top)
    };
}

function setAlpha(data, pos, alpha) {
    data[300*pos.y*4 + pos.x*4 + 3] = alpha;
}

// () => defines an anonymous function that takes no arguments  
canvas.addEventListener('mousedown', () => {
    painting = true;
    console.log('painting...');
})

canvas.addEventListener('mouseup', () => {
    painting = false;
    console.log('painting terminated.');
    curves.push(curve)
    curve = [];
})

canvas.addEventListener('mousemove', (evt) => {
    if (!painting) {
        return;
    }
    ctx.lineWidth = 1;
    let pos = getMousePos(canvas, evt);
    
    ctx.fillRect(pos.x, pos.y, 1, 1);
    curve.push(pos);
});

undo.addEventListener('click', () => {
    let imageData = ctx.getImageData(0, 0, 300, 150);
    // remove the last curve by making it transparent

    let lastCurve = curves.pop();  // removes and returns, works as expected

    for (let index = 0; index < lastCurve.length; index++) {
        const pos = lastCurve[index];

        console.log('old:', imageData.data[300*pos.y*4 + pos.x*4 + 3]);    
        setAlpha(imageData.data, pos, 0);   
        console.log('new:', imageData.data[300*pos.y*4 + pos.x*4 + 3]); 
    }
    ctx.putImageData(imageData, 0, 0);
});
