// canvas and drawCanvas will occupy the same space
// specified in the CSS
const canvas = document.getElementById('canvas'); // for interactions with the element
const backgroundCanvas = document.getElementById('background-canvas');
const outputCanvas = document.getElementById('output-canvas');
const drawCanvas = document.getElementById('draw-canvas');

const ctx = canvas.getContext('2d'); // for drawing functions
const backgroundCtx = backgroundCanvas.getContext('2d');
const outputCtx = outputCanvas.getContext('2d');
const drawCtx = drawCanvas.getContext('2d');

function toUserCoors(x, y) {
	return [x - 10, -(y - 75)];
}

function fromUserCoors(x, y) {
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

// draw the axes on the backgroundCtx
drawLine(backgroundCtx, 'purple', [10, 75], [290, 75], 2); // x-axis
drawLine(backgroundCtx, 'purple', [10, 10], [10, 140], 2); // y-axis

// draw the axes on the outputCtx
drawLine(outputCtx, 'purple', [10, 75], [290, 75], 2); // x-axis
drawLine(outputCtx, 'purple', [10, 10], [10, 140], 2); // y-axis

function drawDerivative(ctx, color, curve, width) {
	// transform the points to a new coordinate system where
	// [10, 75] is the origin

	// internally convert the pos.x, pos.y into a dictionary {x1:y1, x2:y2}
	let curveDict = {}; // by having a dictionary, we are making a one to one mapping
	curve.forEach((pos) => {
		let [newx, newy] = toUserCoors(pos.x, pos.y);
		curveDict[newx] = newy;
	});

	// now that we have a one to one mapping, get the [x, y] values from the dictionary
	// note that javascript keys are always strings
	curveOneToOne = [];
	for (const x in curveDict) {
		curveOneToOne.push([parseInt(x), curveDict[x]]);
	}
	console.log(curveOneToOne);
	// 2d array with x y
	derivCurve = [];
	for (let index = 1; index < curveOneToOne.length - 1; index++) {
		const x = curveOneToOne[index][0];
		const prevY = curveOneToOne[index][1];
		const nextY = curveOneToOne[index + 1][1];
		const theoreticalResult = (nextY - prevY) / 2;

		// for display reasons (pixels), we want to scale up derivative
		const pixelValue = Math.round(theoreticalResult * 10);

		derivCurve.push([x, pixelValue]);
	}
	console.log(derivCurve);
	drawReadyDerivCurve = [];
	derivCurve.forEach((point) => {
		drawReadyDerivCurve.push(fromUserCoors(point[0], point[1]));
	});

	ctx.strokeStyle = color;
	ctx.lineWidth = width;
	ctx.beginPath();
	ctx.moveTo(drawReadyDerivCurve[0][0], drawReadyDerivCurve[0][1]);

	drawReadyDerivCurve.forEach((point) => {
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
	let pixelCount = Math.floor(index / 4);
	return {
		x: pixelCount % 300,
		y: Math.floor(pixelCount / 300),
	};
}

function getCoorsOpaque(data) {
	// data is imageData.data array

	coorsOpaque = [];

	for (let index = 3; index < data.length; index = index + 4) {
		const alpha = data[index];
		if (alpha != 0) {
			coorsOpaque.push(getPosFromIndex(index));
		}
	}
	return coorsOpaque;
}

let painting = false;

// this is where we store our final result: the curve whose derivative we want to find
curve = null;

drawCanvas.addEventListener('mousedown', () => {
	drawCtx.beginPath();
	painting = true;
	console.log('painting...');
});

drawCanvas.addEventListener('mouseup', () => {
	painting = false;
	let imageDataRecent = drawCtx.getImageData(0, 0, 300, 150);
	curve = getCoorsOpaque(imageDataRecent.data);

	// copy onto storage context
	ctx.putImageData(imageDataRecent, 0, 0);

	// clear the draw context
	drawCtx.clearRect(0, 0, 300, 150);
	console.log('painting terminated.');

	// clear the output context
	outputCtx.clearRect(0, 0, 300, 150);

	// find the derivative and display it on the outputCanvas
	drawDerivative(outputCtx, 'blue', curve, 2);
});

drawCanvas.addEventListener('mousemove', (evt) => {
	if (!painting) {
		return;
	}
	drawCtx.lineWidth = 1;
	let pos = getMousePos(canvas, evt);

	drawCtx.lineTo(pos.x, pos.y);
	drawCtx.stroke();
});
