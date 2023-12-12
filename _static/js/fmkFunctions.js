// Copyright 2021 fmckenna@berkeley.edu

var margin = { top: 0, right: 20, bottom: 0, left: 60 };
// const { eigs } = math


function mapResponse(t, disp) {
    var numPoints = t.length;
    var response = new Array(numPoints);
    for (var i = 0; i < numPoints; i++){
        response[i] = {
	    x: t[i],
	    y: disp[i]
        };
    }
    return response;
}

function mapResponseFactor(t, disp, fact) {
    var numPoints = t.length;
    var response = new Array(numPoints);
    for (var i = 0; i < numPoints; i++){
        response[i] = {
	    x: t[i],
	    y: disp[i]*fact
        };
    }
    return response;
}

function absMaxLocation(data) {
    let numPoints = data.length;
    let maxV = data[0];
    let minV = data[0];
    let minLoc = 0;
    let maxLoc = 0;
    let absMax = 0;
    let absLoc = 0;
    for (let i=1; i<numPoints; i++) {
	if (data[i] > maxV) {
	    maxV = data[i];
	    maxLoc = i;
	} else if (data[i] < minV) {
	    minV = data[i];
	    minLoc = i;
	}
	if (abs(maxV) > abs(minV)) {
	    absMax = maxV;
	    absLoc = maxLoc;
	} else {
	    absMax = minV;
	    absLoc = minLoc;
	}
    }
    return [absMax, absLoc, maxV, maxLoc, minV, minLoc];
}


function absMaxLocationObject(data) {
    
    let numPoints = data.length;
    let maxV = data[0].x;
    let minV = data[0].x;
    let minLoc = data[0].y;
    let maxLoc = data[0].y;
    let absMax = data[0].x;
    let absLoc = data[0].y;
    for (let i=1; i<numPoints; i++) {
	if (data[i].x > maxV) {
	    maxV = data[i].x;
	    maxLoc = data[i].y;
	} else if (data[i].x < minV) {
	    minV = data[i].x;
	    minLoc = data[i].y;
	}
	if (abs(maxV) > abs(minV)) {
	    absMax = maxV;
	    absLoc = maxLoc;
	} else {
	    absMax = minV;
	    absLoc = minLoc;
	}
    }
    return [absMax, absLoc, maxV, maxLoc, minV, minLoc];
}

function initAxis(svg, xScale, yScale, width, height, numTicks) {

    var xAxis = d3.axisBottom().scale(xScale).ticks(numTicks);
    var xAxisGrid = d3.axisBottom().scale(xScale).tickSize(-height).ticks(numTicks).tickFormat("");
    var yAxisGrid = d3.axisLeft().scale(yScale).tickSize(-width).ticks(numTicks).tickFormat("");
    
    // x-axis
    svg.append('g').attr('class', 'grid').attr('transform', 'translate(0,' + height + ')')
	.call(xAxisGrid);          
    svg.append('g').attr('class', 'x axis').attr('transform', 'translate(0,' + height + ')')
	.call(xAxis);
    
    // y-axis
    svg.append('g').attr('class', 'grid').attr('transform', 'translate(' + 0 + ',0)')
	.call(yAxisGrid);
    
    svg.append('g').attr('class', 'y axis').attr('transform', 'translate(' + 0 + ',0)')
	.call(yAxis);
    
}


// list of eigen values square matrix (allow non symmetric)
function eigenvalues(n, k, m) {


    const K = Array.from(k);
    const M = Array.from(m);


    var A = Array.from(k);
    const idx = (x, y) => y * n + x;
    for (let i = 0; i < n; i++)
	for (let j = 0; j < n; j++)	
	    A[idx(i, j)] = K[idx(i,j)]/M[i];

    var arr = [];
    var rows = n;
    for (var i = 0; i < rows; i++) {
	arr[i] = [];
	for (var j = 0; j < rows; j++) {
	    arr[i][j] = A[i * rows + j];
	}
    }
    
    const ans = eigs(arr);
    var eigenValues = ans.values;

    for (let i=0; i<n; i++) {
	let smallest = eigenValues[i];
	let current = smallest;
	let loc = i;
	for (let j=i+1; j<n; j++) {
	    if (eigenValues[j] < smallest) {
		smallest = eigenValues[j];
		loc = j;
	    }
	}
	if (loc != i) {
	    eigenValues[i]=smallest;
	    eigenValues[loc]=current;
	}
    }

    // for tri-diagonal K matrices
    let eigenVectors = [];
    let eigV = Array.from(m);
    for (let i=0; i<n; i++) {
	var lambda = eigenValues[i];
	eigV[0]=1.0;
	eigV[1] = -(K[idx(0,0)]-lambda*M[0])/K[idx(0,1)];
	for (let k=2; k<n; k++) {
	    eigV[k] = -((K[idx(k-1,k-1)]-lambda*M[k-1])*eigV[k-1]+
			K[idx(k-1,k-2)]*eigV[k-2])/K[idx(k-1,k)];
	}
	// normalize: Mn=1
	var mn = 0.0;
	for (let k=0; k<n; k++)
	    mn = mn + M[k]*eigV[k]*eigV[k];
	var divisor = 1.0/Math.sqrt(mn);
	for (let k=0; k<n; k++)
	    eigV[k] = eigV[k]*divisor;
	eigenVectors[i] = Array.from(eigV);
    }

    // return
    return [eigenValues, eigenVectors];
}


