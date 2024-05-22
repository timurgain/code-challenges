import { PromiseCustom } from '../promiseCustom';

describe('PromiseCustom', () => {
  it('should resolve', async () => {
    const promiseResolved = new PromiseCustom((resolve) => {
      resolve('resolved');
    });

    const result = await promiseResolved;

    expect(result).toBe('resolved');
  });

  it('should reject', async () => {
    const promiseRejected = new PromiseCustom((_, reject) => {
      reject('rejected');
    });

    try {
      await promiseRejected;
    } catch (error) {
      expect(error).toBe('rejected');
    }
  });

  it('should resolve with then', async () => {
    const promiseResolved = new PromiseCustom((resolve) => {
      resolve('resolved');
    });

    const result = await promiseResolved.then((value) => value);

    expect(result).toBe('resolved');
  });

  it('should reject with catch', async () => {
    const promiseRejected = new PromiseCustom((_, reject) => {
      reject('rejected');
    });

    try {
      await promiseRejected.catch((error) => error);
    } catch (error) {
      expect(error).toBe('rejected');
    }
  });

  it('should resolve with then chaining', async () => {
    const promiseResolved = new PromiseCustom((resolve) => {
      resolve('resolved');
    });

    const result = await promiseResolved
      .then((value) => value)
      .then((value) => value);

    expect(result).toBe('resolved');
  });

  it('should run finally', async () => {
    const promiseResolved = new PromiseCustom((resolve) => {
      resolve('resolved');
    });

    const result = await promiseResolved
      .then((value) => value)
      .finally(() => 'finally');

    expect(result).toBe('resolved');
  });
});
