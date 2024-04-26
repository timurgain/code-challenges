import axios from 'axios';


export async  function getToDos() {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/todos');
    return response.data;
  } catch (error) {
    console.error(error);
    return [];
  }
}
