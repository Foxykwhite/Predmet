import { Link } from "react-router-dom";
import ProductCard from "../components/ProductCard";

const products = [
  { id: 1, name: "Товар 1", price: 100, description: "Описание товара 1" },
  { id: 2, name: "Товар 2", price: 200, description: "Описание товара 2" },
];

export default function Home() {
  return (
    <div>
      <h1 className="mb-4">Продукты</h1>
      <div className="row">
        {products.map((product) => (
          <div key={product.id} className="col-4 mb-4">
            <ProductCard product={product} />
          </div>
        ))}
      </div>
    </div>
  );
}