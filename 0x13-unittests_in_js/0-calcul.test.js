const calculateNumber = require("./0-calcul.js");
const mocha = require('mocha');
const assert = require("assert");

describe('calculateNumber', () => {
  it('returns rounded sum', () => {
  assert.strictEqual(calculateNumber(2, 2), 4);
  assert.strictEqual(calculateNumber(1.5, 3.2), 5);
  assert.strictEqual(calculateNumber(1.3, 3.7), 5);
  assert.strictEqual(calculateNumber(-1, -3), -4);
  assert.strictEqual(calculateNumber(-1.2, -3.8), -5);
  });
});
