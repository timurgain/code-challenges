import { createUser } from '../createUser.js';

describe('createUser', () => {
  it('should create a user with name and surname only', () => {
    const user = { name: 'John', surname: 'Doe' };
    expect(createUser(user)).toMatchSnapshot();
  });

  it('should create a user with all the properties', () => {
    const user = {
      name: 'John',
      surname: 'Doe',
      age: 30,
      email: 'e@em.com'
    };
    expect(createUser(user)).toMatchSnapshot();
  });
});
