export class PromiseCustom {
  STATE = {
    pending: "pending",
    rejected: "rejected",
    fulfilled: "fulfilled",
  };

  constructor(executer) {
    this.state = this.STATE.pending;
    this.value = null;
    this.reason = null;
    this.onFulfilled = null;
    this.onRejected = null;

    const resolve = (value) => {
      if (this.state !== this.STATE.pending) return;
      queueMicrotask(() => {
        this.state = this.STATE.fulfilled;
        this.value = value;
        if (this.onFulfilled) this.onFulfilled(value);
      });
    };

    const reject = (reason) => {
      if (this.state !== this.STATE.pending) return;
      queueMicrotask(() => {
        this.state = this.STATE.rejected;
        this.reason = reason;
        if (this.onRejected) this.onRejected(reason);
      });
    };

    try {
      executer(resolve, reject);
    } catch (error) {
      reject(error);
    }
  }

  static resolve(value) {
    if (value instanceof PromiseCustom) {
      return value;
    } else if (value && typeof value.then === 'function') {
      return new PromiseCustom((resolve, reject) => {
        value.then(resolve, reject);
      });
    } else {
      return new PromiseCustom(resolve => resolve(value));
    }
  }

  then(onFulfilled, onRejected) {
    return new PromiseCustom((resolve, reject) => {
      this.onFulfilled = (value) => {
        queueMicrotask(() => {
          try {
            if (onFulfilled) {
              const result = onFulfilled(value);
              resolve(result);
            } else {
              resolve(value);
            }
          } catch (error) {
            reject(error);
          }
        });
      };

      this.onRejected = (reason) => {
        queueMicrotask(() => {
          try {
            if (onRejected) {
              const result = onRejected(reason);
              reject(result);
            } else {
              reject(reason);
            }
          } catch (error) {
            reject(error);
          }
        });
      };

      if (this.state === this.STATE.fulfilled && onFulfilled)
        this.onFulfilled(this.value);
      if (this.state === this.STATE.rejected && onRejected)
        this.onRejected(this.reason);
    });
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }

  finally(onFinally) {
    return this.then(
      (value) => PromiseCustom.resolve(onFinally()).then(() => value),
      (reason) => PromiseCustom.resolve(onFinally()).then(() => {throw reason})
    );
  }
}
