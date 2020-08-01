/*
This code contains event handlers for mouse input,
calculations for plotting the derivative,
and code to only allow one active curve at a time.
*/

// All canvases occupy same space.

// for auto-drawing background axes (never cleared)
const axesCanvas = document.getElementById('axes-canvas');
const axesCtx = axesCanvas.getContext('2d');

// for storing recently drawn curve
const recentCanvas = document.getElementById('recent-canvas');
const recentCtx = recentCanvas.getContext('2d');

// for user-drawing new curve
const drawCanvas = document.getElementById('draw-canvas');
const drawCtx = drawCanvas.getContext('2d');

// for auto-drawing derivative
const outputCanvas = document.getElementById('output-canvas');
const outputCtx = outputCanvas.getContext('2d');

function toUserCoors([x, y]) {
	return [x - 10, -(y - 75)];
}

function fromUserCoors([x, y]) {
	return [x + 10, -y + 75];
}

function drawLine(ctx, color, start, end, width) {
	ctx.strokeStyle = color;
	ctx.lineWidth = width;
	ctx.beginPath();
	ctx.moveTo(start[0], start[1]);
	ctx.lineTo(end[0], end[1]);
	ctx.stroke();
}

function getXMatchIndex(x, dst) {
	for (const [dstIndex, dstObj] of dst.entries()) {
		if (x == dstObj.x) {
			return dstIndex;
		}
	}
}

function drawDerivative(ctx, color, posArray, width) {
	// just like pos array but x coordinates are unique
	let posArrayModified = [];

	posArray.forEach((pos) => {
		dstIndex = getXMatchIndex(pos.x, posArrayModified);
		if (dstIndex == undefined) {
			const newPos = {
				x: pos.x,
				y: [pos.y],
			};
			posArrayModified.push(newPos);
		} else {
			posArrayModified[dstIndex].y.push(pos.y);
		}
	});

	// sort the object array by x value
	posArrayModified = posArrayModified.sort((obj1, obj2) => {
		return obj1.x - obj2.x;
	});

	let pointArray = [];
	for (const index in posArrayModified) {
		const object = posArrayModified[index];
		const x = object.x;
		const y = object.y.reduce((a, b) => a + b, 0) / object.y.length; // getting average value (0 is the default value)
		pointArray.push([x, y]);
	}

	// need to convert the point array to user coors
	pointArray = pointArray.map(toUserCoors);

	pointArrayDeriv = [];
	for (let index = 1; index < pointArray.length - 1; index++) {
		const x = pointArray[index][0];
		const prevY = pointArray[index - 1][1];
		const nextY = pointArray[index + 1][1];
		const theoreticalResult = (nextY - prevY) / 2;

		// for display reasons (pixels), we want to scale up derivative
		const pixelValue = Math.round(theoreticalResult * 10);

		pointArrayDeriv.push([x, pixelValue]);
	}

	// need to convert the point array deriv from user coors
	pointArrayDeriv = pointArrayDeriv.map(fromUserCoors);

	ctx.strokeStyle = color;
	ctx.lineWidth = width;
	ctx.beginPath();
	ctx.moveTo(pointArrayDeriv[0][0], pointArrayDeriv[0][1]);

	pointArrayDeriv.forEach((point) => {
		ctx.lineTo(point[0], point[1]);
	});
	ctx.stroke();
}

function getMousePos(canvas, evt) {
	let rect = canvas.getBoundingClientRect();
	return {
		x: Math.floor(evt.clientX - rect.left), // we do not want fractional pixels for our mouse position
		y: Math.floor(evt.clientY - rect.top),
	};
}

function getPosFromIndex(index) {
	const pixelCount = Math.floor(index / 4);
	return {
		x: pixelCount % 300,
		y: Math.floor(pixelCount / 300),
	};
}

function getCoorsOpaque(data) {
	// data is imageData.data array (a 1d array with r, g, b, a sequence)

	coorsOpaque = [];

	for (let index = 3; index < data.length; index = index + 4) {
		const alpha = data[index];
		if (alpha != 0) {
			coorsOpaque.push(getPosFromIndex(index));
		}
	}
	return coorsOpaque;
}

// STARTING THE ACTIONS!

// draw the axes on the backgroundCtx
drawLine(axesCtx, 'purple', [10, 75], [290, 75], 2); // x-axis
drawLine(axesCtx, 'purple', [10, 10], [10, 140], 2); // y-axis

let painting = false;

// the curve whose derivative we want to find, composed of pos objects
let posArray = null;

drawCanvas.addEventListener('mousedown', () => {
	drawCtx.beginPath();
	painting = true;
	console.log('painting...');
});

drawCanvas.addEventListener('mouseup', () => {
	painting = false;
	let imageDataRecent = drawCtx.getImageData(0, 0, 300, 150);
	posArray = getCoorsOpaque(imageDataRecent.data);

	// copy onto storage context
	recentCtx.putImageData(imageDataRecent, 0, 0);

	// clear the draw context
	drawCtx.clearRect(0, 0, 300, 150);
	console.log('painting terminated.');

	// clear the output context
	outputCtx.clearRect(0, 0, 300, 150);

	// find the derivative and display it on the outputCanvas
	drawDerivative(outputCtx, 'blue', posArray, 2);
});

drawCanvas.addEventListener('mousemove', (evt) => {
	if (!painting) {
		return;
	}
	drawCtx.lineWidth = 1;
	let pos = getMousePos(drawCanvas, evt);

	drawCtx.lineTo(pos.x, pos.y);
	drawCtx.stroke();
});
