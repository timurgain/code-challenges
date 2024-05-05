import { validatePassword } from "../validate-password.js";
import { dummyPasswords } from "../constants.js";

describe("validatePassword", () => {
  it("should return true for a valid password", () => {
    const validPassword = "Password123!";
    expect(validatePassword(validPassword)).toBe(true);
  });

  it("should validate a password against minimum 8 characters", () => {
    const invalidPassword = "Pass123!";
    const validPassword = "Password123!";

    expect(validatePassword(invalidPassword)).toBe(false);
    expect(validatePassword(validPassword)).toBe(true);
  });

  it("should validate a password against mixed case", () => {
    const invalidPassword = "password123!";
    const invalidPassword2 = "PASSWORD123!";
    const validPassword = "Password123!";

    expect(validatePassword(invalidPassword)).toBe(false);
    expect(validatePassword(invalidPassword2)).toBe(false);
    expect(validatePassword(validPassword)).toBe(true);
  });

  it.todo("should validate a password against digits and characters", () => {
    const invalidPassword = "Password!";
    const invalidPassword2 = "Password";
    const validPassword = "Password123!";

    expect(validatePassword(invalidPassword)).toBe(false);
    expect(validatePassword(invalidPassword2)).toBe(false);
    expect(validatePassword(validPassword)).toBe(true);
  });

  it.todo("should validate a password against special characters", () => {
    const invalidPassword = "Password123";
    const invalidPassword2 = "Password123";
    const validPassword = "Password123!";

    expect(validatePassword(invalidPassword)).toBe(false);
    expect(validatePassword(invalidPassword2)).toBe(false);
    expect(validatePassword(validPassword)).toBe(true);
  });

  it.todo("should validate a password against dummy passwords", () => {
    dummyPasswords.forEach((password) => {
      expect(validatePassword(password)).toBe(false);
    });
  });
});
