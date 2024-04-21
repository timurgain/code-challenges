import { Basket, expectedFilteredBasket } from "../__mocks__/basket.mock";
import { filterArray } from "../filterArray.js";

describe("filterArray", () => {
  let callback;
  beforeEach(() => {
    callback = jest.fn();
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should not invoke callback when array is empty", () => {
    filterArray([], callback);
    expect(callback).not.toHaveBeenCalled();
  });
  it("should invoke callback for each item in the array", () => {
    const arr = [1, 2, 3];
    filterArray(arr, callback);
    expect(callback).toHaveBeenCalledTimes(arr.length);
  });

  it("should return a new array with items that pass the callback", () => {
    const hasQuontity = (item) => item.quantity > 0;
    const result = filterArray(Basket, hasQuontity);
    expect(result).toEqual(expectedFilteredBasket);
  });
});
