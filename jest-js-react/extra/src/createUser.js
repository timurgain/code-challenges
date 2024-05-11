export function createUser({
  name,
  surname,
  age = 18,
  email = '',
}) {
  return {
    type: 'USER',
    name,
    surname,
    password: 'hashed-password',
    age,
    email,
  };
}
