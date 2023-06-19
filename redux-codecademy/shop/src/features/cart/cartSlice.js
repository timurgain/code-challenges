// action creators

export const addItem = (itemToAdd) => {
  return {
    type: 'cart/addItem',
    payload: itemToAdd,
  };
};

export const changeItemQuantity = (name, newQuantity) => {
  return {
    type: 'cart/changeItemQuantity',
    payload: {name, newQuantity }
  }
}

// initial state

const initialCart = {};

// reducer

export const cartReducer = (cart = initialCart, action) => {

  switch (action.type) {

    case 'cart/addItem': {
      const { name, price } = action.payload;
      const quantity = cart[name] ? cart[name].quantity + 1 : 1;
      const newItem = { price, quantity };
      return {
        ...cart,
        [name]: newItem
      };
    }

    case 'cart/changeItemQuantity': {
      const { name, newQuantity } = action.payload;
      const itemUpdated = {...cart[name], quantity: newQuantity}
      return {...cart, [name]: itemUpdated};
    }

    default: {
      return cart;
    }
  }
};
