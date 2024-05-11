/** @type {import('jest').Config} */
const config = {
  verbose: true,
  collectCoverage: true,
  collectCoverageFrom: [
    '<rootDir>/src/**/*.{js,ts}',
    '!<rootDir>/src/**/*.mock.*',
  ],
  testMatch: [
    '<rootDir>/src/**/*.test.{js,ts}',
  ],
  setupFiles: [
    '<rootDir>/internal/jest/jest.setup.js',
  ],
  setupFilesAfterEnv: [
    '<rootDir>/internal/jest/setup-tests.js',
    '<rootDir>/internal/jest/custom-matchers.js',
  ],

  globals: {
    __DEV__: true,
  },

  testEnvironment: 'jsdom',

  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    }
  }
};

module.exports = config;
