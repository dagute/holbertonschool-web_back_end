function calculateNumber(x, y) {
  const xRound = Math.round(x);
  const yRound = Math.round(y);
  
  return xRound + yRound;
}

module.exports = calculateNumber;
