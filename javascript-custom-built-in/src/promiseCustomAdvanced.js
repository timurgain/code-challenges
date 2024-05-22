const STATE = {
  PENDING: "pending",
  FULFILLED: "fulfilled",
  REJECTED: "rejected",
};

export class PromiseCustom {
  #thenCallbacks = [];
  #catchCallbacks = [];
  #state = STATE.PENDING;
  #value;

  constructor(callback) {
    try {
      callback(this.#onSuccess, this.#onFail);
    } catch (error) {
      this.reject(error);
    }
  }

  #runCallbacks() {
    if (this.#state === STATE.FULFILLED) {
      this.#thenCallbacks.this.#thenCallbacks = [];
    }

    if (this.#state === STATE.REJECTED) {
      this.#catchCallbacks.forEach((fn) => {
        fn(this.#value);
      });
      this.#catchCallbacks = [];
    }
  }

  #onSuccess(value) {
    if (this.#state !== STATE.PENDING) return;
    this.#value = value;
    this.#state = STATE.FULFILLED;
  }

  #onFail(value) {
    if (this.#state !== STATE.PENDING) return;
    this.#value = value;
    this.#state = STATE.REJECTED;
  }

  then(callback) {
    this.#thenCallbacks.push(callback);
    this.#runCallbacks();
  }

  catch(callback) {
    this.#catchCallbacks.push(callback);
    this.#runCallbacks();
  }
}
