import { dummyPasswords, passwordValidateErrors } from "./constants";

export function validatePassword(password) {
  if (password.length < 8) {
    return {
      success: false,
      errors: passwordValidateErrors.length,
    };
  }

  if (!/[a-z]/.test(password) || !/[A-Z]/.test(password)) {
    return {
      success: false,
      errors: passwordValidateErrors.case,
    };
  }

  if (!/\d/.test(password)) {
    return {
      success: false,
      errors: passwordValidateErrors.digits,
    };
  }

  if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
    return {
      success: false,
      errors: passwordValidateErrors.special,
    };
  }

  if (dummyPasswords.includes(password)) {
    return {
      success: false,
      errors: passwordValidateErrors.dummy,
    };
  }

  return { success: true, errors: null };
}
