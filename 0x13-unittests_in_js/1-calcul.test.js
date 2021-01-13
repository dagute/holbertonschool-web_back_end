const calculateNumber = require("./1-calcul.js");
const mocha = require('mocha');
const assert = require("assert");

describe('calculateNumber', () => {
  it('returns rounded sum with SUM', () => {
    assert.strictEqual(calculateNumber(2, 2), 4);
    assert.strictEqual(calculateNumber(1.5, 3.2), 5);
    assert.strictEqual(calculateNumber(1.3, 3.7), 5);
    assert.strictEqual(calculateNumber(-1, -3), -4);
    assert.strictEqual(calculateNumber(-1.2, -3.8), -5);
  });
  it('returns rounded sum with SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 2, 4), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.7, 3), -1);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 3.6), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', -1, -3), 2);
    assert.strictEqual(calculateNumber('SUBTRACT',-1.5, -3.5), 3);
    });
    it('returns rounded sum with DIVIDE', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.7, 4.2), 0.4);
    });
    it('returns error string when DIVIDE by 0', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.7, 0), 'Error');
    });
});
