import { useState } from "react";

interface Workout {
  date: string;
  exercise: string;
  sets: number;
  reps: number;
  weight: number;
}

export default function WorkoutForm({ onAdd }: { onAdd: (workout: Workout) => void }) {
  const [workout, setWorkout] = useState<Workout>({
    date: "",
    exercise: "",
    sets: 0,
    reps: 0,
    weight: 0,
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setWorkout({ ...workout, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onAdd(workout);
    setWorkout({ date: "", exercise: "", sets: 0, reps: 0, weight: 0 });
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <input name="date" type="date" value={workout.date} onChange={handleChange} className="form-control mb-2" />
      <input name="exercise" placeholder="Упражнение" value={workout.exercise} onChange={handleChange} className="form-control mb-2" />
      <input name="sets" type="number" placeholder="Подходы" value={workout.sets} onChange={handleChange} className="form-control mb-2" />
      <input name="reps" type="number" placeholder="Повторения" value={workout.reps} onChange={handleChange} className="form-control mb-2" />
      <input name="weight" type="number" placeholder="Вес (кг)" value={workout.weight} onChange={handleChange} className="form-control mb-2" />
      <button type="submit" className="btn btn-primary">Добавить</button>
    </form>
  );
}