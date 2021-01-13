const calculateNumber = require("./1-calcul.js");
const mocha = require('mocha');
const assert = require("assert");

describe('calculateNumberWithType', () => {
  it('returns rounded sum with SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('returns rounded sum with SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('returns rounded sum with DIVIDE', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('divide with b == 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'ERROR');
  });
});
