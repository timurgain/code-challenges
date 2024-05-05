import { validatePassword } from "../validate-password.js";
import { dummyPasswords, passwordValidateErrors } from "../constants.js";

describe("validatePassword", () => {
  it("should return {success: true, errors: null} for a valid password", () => {
    const validPassword = "Password123!";
    const expectedResult = {success: true, errors: null};

    expect(validatePassword(validPassword)).toEqual(expectedResult);
  });

  it("should validate a password against minimum 8 characters", () => {
    const invalidPassword = "Pa12!";
    const validPassword = "Password123!";

    const invalidExpectedResult = {
      success: false,
      errors: passwordValidateErrors.length,
    };

    const validExpectedResult = {success: true, errors: null};

    expect(validatePassword(invalidPassword)).toEqual(invalidExpectedResult);
    expect(validatePassword(validPassword)).toEqual(validExpectedResult);
  });

  it("should validate a password against mixed case", () => {
    const invalidPassword = "password123!";
    const invalidPassword2 = "PASSWORD123!";
    const validPassword = "Password123!";

    const invalidExpectedResult = {
      success: false,
      errors: passwordValidateErrors.case,
    };

    const validExpectedResult = {success: true, errors: null};

    expect(validatePassword(invalidPassword)).toEqual(invalidExpectedResult);
    expect(validatePassword(invalidPassword2)).toEqual(invalidExpectedResult);
    expect(validatePassword(validPassword)).toEqual(validExpectedResult);
  });

  it("should validate a password against digits and characters", () => {
    const invalidPassword = "Password!";
    const invalidPassword2 = "Password";
    const validPassword = "Password123!";

    const invalidExpectedResult = {
      success: false,
      errors: passwordValidateErrors.digits,
    };

    const validExpectedResult = {success: true, errors: null};

    expect(validatePassword(invalidPassword)).toEqual(invalidExpectedResult);
    expect(validatePassword(invalidPassword2)).toEqual(invalidExpectedResult);
    expect(validatePassword(validPassword)).toEqual(validExpectedResult);
  });

  it("should validate a password against special characters", () => {
    const invalidPassword = "Password123";
    const invalidPassword2 = "Password123";
    const validPassword = "Password123!";

    const invalidExpectedResult = {
      success: false,
      errors: passwordValidateErrors.special,
    };

    const validExpectedResult = {success: true, errors: null};

    expect(validatePassword(invalidPassword)).toEqual(invalidExpectedResult);
    expect(validatePassword(invalidPassword2)).toEqual(invalidExpectedResult);
    expect(validatePassword(validPassword)).toEqual(validExpectedResult);
  });

  it("should validate a password against dummy passwords", () => {

    const invalidPassword = dummyPasswords[0];
    const validPassword = "Password123!";

    const invalidExpectedResult = {
      success: false,
      errors: passwordValidateErrors.dummy,
    };

    const validExpectedResult = {success: true, errors: null};

    expect(validatePassword(invalidPassword)).toEqual(invalidExpectedResult);
    expect(validatePassword(validPassword)).toEqual(validExpectedResult);
  });
});
