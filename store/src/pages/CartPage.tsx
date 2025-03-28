import { useSelector, useDispatch } from "react-redux";
import { RootState } from "../store";
import { removeItemFromCart } from "../store/cartSlice";

export default function CartPage() {
  const cartItems = useSelector((state: RootState) => state.cart.items);
  const dispatch = useDispatch();

  return (
    <div>
      <h1>Корзина</h1>
      {cartItems.length === 0 ? (
        <p>Корзина пуста</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              {item.name} - {item.price}₽ x {item.quantity}
              <button onClick={() => dispatch(removeItemFromCart(item.id))}>Удалить</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}