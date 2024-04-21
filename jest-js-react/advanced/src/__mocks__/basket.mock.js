export const Basket = [
  {
    id: 1,
    name: "Apple",
    price: 1.5,
    quantity: 1,
  },
  {
    id: 2,
    name: "Banana",
    price: 2.5,
    quantity: 0,
  },
  {
    id: 3,
    name: "Orange",
    price: 3.5,
    quantity: 2,
  },
  {
    id: 4,
    name: "Grapes",
    price: 4.5,
    quantity: 3,
  },
  {
    id: 5,
    name: "Mango",
    price: 5.5,
    quantity: 0,
  },
];

export const expectedFilteredBasket = [
  {
    id: 1,
    name: "Apple",
    price: 1.5,
    quantity: 1,
  },
  {
    id: 3,
    name: "Orange",
    price: 3.5,
    quantity: 2,
  },
  {
    id: 4,
    name: "Grapes",
    price: 4.5,
    quantity: 3,
  },
];
