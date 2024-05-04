import axios from "axios";
import { getToDos } from "../getToDos";

const spyAxiosGet = jest.spyOn(axios, "get");
const spyConsoleLog = jest.spyOn(console, "error");

describe("getToDos", () => {

  afterEach(() => {
    jest.clearAllMocks();
  })

  it("should return 200 todos, that is how https://jsonplaceholder works", async () => {
    const result = await getToDos();
    expect(spyAxiosGet).toHaveBeenCalledTimes(1);
    expect(result).toHaveLength(200);
  });

  it("should return an empty array if there is an error", async () => {
    const errorMsg = "Network Error";
    // spyAxiosGet.mockImplementationOnce(() => Promise.reject(errorMsg));
    spyAxiosGet.mockRejectedValueOnce(errorMsg);

    const result = await getToDos();
    expect(spyConsoleLog).toHaveBeenCalledWith(errorMsg);
    expect(result).toEqual([]);
  });
});
