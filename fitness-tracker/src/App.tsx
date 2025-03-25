import { Routes, Route } from "react-router-dom";
import Home from "./Home";

export default function App() {
  return (
    <div className="container mt-4">
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}
