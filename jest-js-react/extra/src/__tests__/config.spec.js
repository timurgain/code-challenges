import { multiply, divide, add, subtract } from '../math.js';

describe('Math functions', () => {
  it('should multiply two numbers, goes on test:integration', () => {
    expect(multiply(2, 3)).toBe(6);
  });
})
