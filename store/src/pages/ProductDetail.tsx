import { useParams } from "react-router-dom";

export default function ProductDetail() {
  const { id } = useParams();
  return <div>Информация о товаре с ID: {id}</div>;
}