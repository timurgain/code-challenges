import { multiply, divide, add, subtract } from "./math.js";

describe("math", () => {
  describe("multiply", () => {
    it("should multiply positive numbers", () => {
      // Arrange
      const expectedResult = 72;

      // Act
      const result = multiply(8, 9);

      // Assert
      expect(result).toBe(expectedResult);
    });

    it("should multiply negative numbers", () => {
      const result = multiply(-7, -9);
      expect(result).toBe(63);
    });

    it.each([
      [-2, -2, 4],
      [5, -5, -25],
    ])("should multiply positive and negative numbers", (a, b, expected) => {
      const result = multiply(a, b);
      expect(result).toBe(expected);
    });

    it("should pass different types of assertions", () => {
      const result = multiply(7, 9);
      expect(result).toBeGreaterThan(60);
      expect(result).toBeGreaterThanOrEqual(63);
      expect(result).toBeLessThan(70);
      expect(result).toBeLessThanOrEqual(63);
    });
  });
  describe("divide", () => {
    it("should devide positive numbers", () => {
      const expectedResult = 4;
      const result = divide(16, 4);
      expect(result).toBe(expectedResult);
    });
  });
  describe("add", () => {
    it.skip("should add positive numbers", () => {
      const expectedResult = 24;
      const result = add(14, 10);
      expect(result).toBe(expectedResult);
    });
  });
});
