import { useState, useEffect } from "react";
import WorkoutForm from "./WorkoutForm";
import ProgressChart from "./ProgressChart";

interface Workout {
  date: string;
  exercise: string;
  sets: number;
  reps: number;
  weight: number;
}

export default function Home() {
  const [workouts, setWorkouts] = useState<Workout[]>([]);

  useEffect(() => {
    const savedWorkouts = localStorage.getItem("workouts");
    if (savedWorkouts) {
      setWorkouts(JSON.parse(savedWorkouts));
    }
  }, []);

  const addWorkout = (workout: Workout) => {
    const updatedWorkouts = [...workouts, workout];
    setWorkouts(updatedWorkouts);
    localStorage.setItem("workouts", JSON.stringify(updatedWorkouts));
  };

  return (
    <div>
      <h1 className="mb-4">Фитнес-трекер</h1>
      <WorkoutForm onAdd={addWorkout} />
      <ProgressChart data={workouts} />
    </div>
  );
}