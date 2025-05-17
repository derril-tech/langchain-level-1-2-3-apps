// Import scoped styles from a CSS module file
import styles from "../styles/todo-list.module.css";

// Import React hooks and lodash debounce utility
import { useState, useEffect, useCallback, useRef } from "react";
import { debounce } from "lodash";

// Import the child component that represents a single to-do item
import ToDo from "./todo";

// Main ToDoList component
export default function ToDoList() {
  // Holds the list of to-do items
  const [todos, setTodos] = useState(null);

  // Controlled input state for the main input field
  const [mainInput, setMainInput] = useState("");

  // Tracks the current filter (e.g., show All, Active, or Completed tasks)
  const [filter, setFilter] = useState();

  // Reference to avoid multiple fetches on initial render
  const didFetchRef = useRef(false);

  // Runs once on initial render to fetch the list of todos
  useEffect(() => {
    if (didFetchRef.current === false) {
      didFetchRef.current = true;
      fetchTodos();
    }
  }, []);

  // Fetch to-do items from the API, with optional filtering by completed status
  async function fetchTodos(completed) {
    let path = "/todos";
    if (completed !== undefined) {
      path = `/todos?completed=${completed}`;
    }
    const res = await fetch(process.env.NEXT_PUBLIC_API_URL + path);
    const json = await res.json();
    setTodos(json);
  }

  // Wrap the updateTodo function in a debounced wrapper to avoid rapid API calls
  const debouncedUpdateTodo = useCallback(debounce(updateTodo, 500), []);

  // Handles updating a to-do item when it is changed (checkbox or text field)
  function handleToDoChange(e, id) {
    const target = e.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;
    const copy = [...todos];
    const idx = todos.findIndex((todo) => todo.id === id);
    const changedToDo = {
      ...todos[idx],
      [name]: value,
    };
    copy[idx] = changedToDo;
    debouncedUpdateTodo(changedToDo);
    setTodos(copy);
  }

  // Sends an API request to update a specific to-do item
  async function updateTodo(todo) {
    const data = {
      name: todo.name,
      completed: todo.completed,
    };
    await fetch(process.env.NEXT_PUBLIC_API_URL + `/todos/${todo.id}`, {
      method: "PUT",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  // Sends an API request to create a new to-do item
  async function addToDo(name) {
    const res = await fetch(process.env.NEXT_PUBLIC_API_URL + `/todos/`, {
      method: "POST",
      body: JSON.stringify({
        name: name,
        completed: false,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (res.ok) {
      const json = await res.json();
      const copy = [...todos, json];
      setTodos(copy);
    }
  }

  // Sends a delete request to remove a to-do item from the list
  async function handleDeleteToDo(id) {
    const res = await fetch(process.env.NEXT_PUBLIC_API_URL + `/todos/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (res.ok) {
      const idx = todos.findIndex((todo) => todo.id === id);
      const copy = [...todos];
      copy.splice(idx, 1);
      setTodos(copy);
    }
  }

  // Updates the value of the main input field
  function handleMainInputChange(e) {
    setMainInput(e.target.value);
  }

  // Handles the Enter key press to add a new to-do item
  function handleKeyDown(e) {
    if (e.key === "Enter") {
      if (mainInput.length > 0) {
        addToDo(mainInput);
        setMainInput("");
      }
    }
  }

  // Updates the filter state and fetches new filtered todos
  function handleFilterChange(value) {
    setFilter(value);
    fetchTodos(value);
  }

  return (
    <div className={styles.container}>
      {/* Input field for adding new todos */}
      <div className={styles.mainInputContainer}>
        <input
          className={styles.mainInput}
          placeholder="What needs to be done?"
          value={mainInput}
          onChange={handleMainInputChange}
          onKeyDown={handleKeyDown}
        />
      </div>

      {/* Show loading text while data is being fetched */}
      {!todos && <div>Loading...</div>}

      {/* Render each to-do item */}
      {todos && (
        <div>
          {todos.map((todo) => (
            <ToDo
              key={todo.id}
              todo={todo}
              onDelete={handleDeleteToDo}
              onChange={handleToDoChange}
            />
          ))}
        </div>
      )}

      {/* Filter buttons for viewing All, Active, or Completed todos */}
      <div className={styles.filters}>
        <button
          className={`${styles.filterBtn} ${
            filter === undefined && styles.filterActive
          }`}
          onClick={() => handleFilterChange()}
        >
          All
        </button>
        <button
          className={`${styles.filterBtn} ${
            filter === false && styles.filterActive
          }`}
          onClick={() => handleFilterChange(false)}
        >
          Active
        </button>
        <button
          className={`${styles.filterBtn} ${
            filter === true && styles.filterActive
          }`}
          onClick={() => handleFilterChange(true)}
        >
          Completed
        </button>
      </div>
    </div>
  );
}

/*
Notes – ToDoList Component in React/Next.js

1. `useState`  
   → A React hook that lets components store and update state (e.g., the todos list, input value, filters).  
   → When state changes, the component re-renders with the updated data.

2. `useEffect`  
   → Runs side effects after render. Here, it's used to fetch todos on first load (similar to componentDidMount).

3. `useRef`  
   → Provides a way to persist values across renders without causing re-renders.  
   → In this case, we use it to track if the initial fetch already happened.

4. `debounce` from Lodash  
   → Prevents a function from being called too frequently.  
   → Useful when typing—waits 500ms after the last change before calling `updateTodo`.

5. `fetchTodos()`  
   → Retrieves to-do items from the API and stores them in state. Can also filter by completed status.

6. `addToDo()`, `updateTodo()`, and `handleDeleteToDo()`  
   → These are all API functions to create, update, or delete items via HTTP calls (POST, PUT, DELETE).

7. `handleMainInputChange` and `handleKeyDown`  
   → These manage the controlled input field and allow adding todos with the Enter key.

8. `props.children`  
   → Not used here but useful in components like Layout to wrap other components.

9. `todos.map()`  
   → Loops over each to-do and renders a `<ToDo />` component for it.  
   → Each needs a unique `key` (e.g., the todo’s id) for React's diffing system.

10. Filter buttons  
   → Toggle the displayed list between all, active (not completed), and completed todos.

In short:  
This is a fully interactive to-do list app in React with CRUD operations and filter options, connected to a REST API. It uses state, effects, event handling, and conditional rendering—all fundamental concepts in React.
*/
