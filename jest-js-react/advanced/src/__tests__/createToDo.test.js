import {
  createToDo,
  createToDoOnServer,
  RESPONSE_ERROR_MSG,
  NO_TITLE_ERROR_MSG,
} from "../createToDo.js";
import { mockTodo } from "../__mocks__/todo.mock.js";

// 0. Init

const mockID = "abcd";
const mockedV4 = jest.fn(() => mockID);

jest.mock("uuid", () => {
  return {
    ...jest.requireActual("uuid"),
    v4: () => mockedV4(),
  };
});

global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve(mockTodo),
  })
);

// 1. test

describe("createToDo", () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should return a toDo object with id, title, completed properties", () => {
    // arrange
    const title = "learn jest";
    const expectedResult = { id: mockID, title, completed: false };

    // act
    const todo = createToDo(title);

    // assert
    expect(mockedV4).toHaveBeenCalledTimes(1);
    expect(todo).toEqual(expectedResult);
  });

  it("should create todo on a server", async () => {
    const result = await createToDoOnServer("mock todo");

    expect(result).toEqual(mockTodo);
    expect(fetch).toHaveBeenCalledTimes(1);
  });

  it("should throw an error if network error", async () => {
    fetch.mockRejectedValueOnce("Network error");

    await expect(createToDoOnServer("new todo")).rejects.toMatch(
      "Network error"
    );
  });

  it("should throw an error from fn when response not ok", async () => {
    fetch.mockResolvedValueOnce({ ok: false });

    await expect(() => createToDoOnServer("new todo")).rejects.toThrow(
      RESPONSE_ERROR_MSG
    );
  });

  it("should throw an error for invalid values", () => {
    expect(() => createToDo("")).toThrow(
      NO_TITLE_ERROR_MSG
    );
  });

  it("should throw an error for invalid values, 'done'-syntax ", (done) => {
    try {
      createToDo("");
      done("should throw an error for invalid values");
    } catch (error) {
      expect(error.message).toBe(NO_TITLE_ERROR_MSG);
      done();
    }
  });
});
