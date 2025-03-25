import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";

interface Workout {
  date: string;
  exercise: string;
  sets: number;
  reps: number;
  weight: number;
}

export default function ProgressChart({ data }: { data: Workout[] }) {
  return (
    <div className="card p-4">
      <h2 className="text-xl font-bold mb-2">График прогресса</h2>
      <LineChart width={600} height={300} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="weight" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}
