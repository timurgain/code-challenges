import { toUpper, toLower, capitalize } from "./strings.js";

describe("Strings", () => {
  beforeAll(() => {
    console.log("Before all tests");
  });

  afterAll(() => {
    console.log("After all tests");
  });

  it.each([
    ["hello", "HELLO"],
    ["paper", "PAPER"],
  ])("should make Uppercase", (input, expected) => {
    const result = toUpper(input);
    expect(result).toBe(expected);
  });

  it.each([
    ["HELLO", "hello"],
    ["PAPER", "paper"],
  ])("should make Lowercase", (input, expected) => {
    const result = toLower(input);
    expect(result).toBe(expected);
  });

  it.each([
    ["hello", "Hello"],
    ["paper", "Paper"],
  ])("should capitalize", (input, expected) => {
    const result = capitalize(input);
    expect(result).toBe(expected);
  });
});
