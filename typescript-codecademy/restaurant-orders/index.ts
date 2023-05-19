import { restaurants, Restaurant } from "./restaurants";
import { orders, Order, PriceBracket } from "./orders";

function getMaxPrice(price: PriceBracket) {
  switch (price) {
    case PriceBracket.low:
      return 10;
    case PriceBracket.Medium:
      return 20;
    case PriceBracket.High:
      return 30;
  }
}

function getOrders(price: PriceBracket, orders: Order[][]): Order[][] {
  let filteredOrders: Order[][] = [];
  for (let i = 0; i < orders.length; i++) {
    filteredOrders.push(
      orders[i].filter((order) => order.price <= getMaxPrice(price))
    );
  }
  return filteredOrders;
}

/// Add your printOrders() function below:
function printOrders(restaurants: Restaurant[], orders: Order[][]): void {
  const res = restaurants.reduce((result, restaurant, index) => {
    if (orders[index].length > 0) {
      result += restaurant.name + "\n";
      orders[index].forEach(
        (order) => (result += `- ${order.name}: $${order.price}\n`)
      );
    }
    return result;
  }, "").slice(0, -1);

  console.log(res)
}

// Main
const elligibleOrders = getOrders(PriceBracket.low, orders);
printOrders(restaurants, elligibleOrders);
