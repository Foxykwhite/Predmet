import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { addItemToCart } from "../store/cartSlice";

interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

export default function ProductCard({ product }: { product: Product }) {
  const dispatch = useDispatch();

  const handleAddToCart = () => {
    dispatch(addItemToCart({ ...product, quantity: 1 }));
  };

  return (
    <div className="card">
      <img src="https://via.placeholder.com/150" alt={product.name} />
      <div className="card-body">
        <h5 className="card-title">{product.name}</h5>
        <p className="card-text">{product.description}</p>
        <p className="card-text">{product.price}₽</p>
        <button className="btn btn-primary" onClick={handleAddToCart}>
          Добавить в корзину
        </button>
        <Link to={`/product/${product.id}`} className="btn btn-link">
          Подробнее
        </Link>
      </div>
    </div>
  );
}