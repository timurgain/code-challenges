import { multiply } from './multiply';

describe('multiply', () => {
  it('should multiply positive numbers', () => {
    // Arrange
    const expectedResult = 72;

    // Act
    const result = multiply(8, 9);

    // Assert
    expect(result).toBe(expectedResult);
  });

  it('should multiply negative numbers', () => {
    const result = multiply(-7, -9);
    expect(result).toBe(63);
  });


  it('should multiply positive and negative numbers', () => {
    const result = multiply(-7, 8);
    expect(result).toBe(-56);
  });

  it('should pass different types of assertions', () => {
    const result = multiply(7, 9);
    expect(result).toBeGreaterThan(60);
    expect(result).toBeGreaterThanOrEqual(63);
    expect(result).toBeLessThan(70);
    expect(result).toBeLessThanOrEqual(63);
  })
})

describe('object tests', () => {
  it('should be equal objects', () => {

    // Arrenge
    const expectObj = { a: 15, b: 8 };

    // Act
    const resultObj = {a: multiply(3, 5), b: multiply(2, 4)};

    // Assert
    expect(resultObj).toEqual(expectObj);
    expect(Object.keys(resultObj)).toHaveLength(2);
    expect(Object.values(resultObj)).toContain(15);
    expect(Object.values(resultObj)).not.toContain(9);
    expect(resultObj).not.toBeNull();


  })
})

