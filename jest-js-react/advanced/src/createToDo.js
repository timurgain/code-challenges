import { v4 } from "uuid";

export const RESPONSE_ERROR_MSG = "Cannot create todo";
export const NO_TITLE_ERROR_MSG = "ToDo title is required";

export function createToDo(title) {
  if (!title) {
    throw new Error(NO_TITLE_ERROR_MSG);
  };

  return {
    id: v4(),
    title,
    completed: false,
  };
}

export async function createToDoOnServer(title) {
  const response = await fetch("https://jsonplaceholder.typicode.com/todos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(createToDo(title)),
  });

  if (!response.ok) throw new Error(RESPONSE_ERROR_MSG);
  return response.json();
}
