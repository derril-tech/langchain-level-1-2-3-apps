// Import Next.js optimized image component
import Image from "next/image";

// Import scoped styles for the todo item
import styles from "../styles/todo.module.css";

// Stateless functional component that receives a todo object and event handlers as props
export default function ToDo(props) {
  // Destructure todo item, change handler, and delete handler from props
  const { todo, onChange, onDelete } = props;

  return (
    // Container for a single to-do row, styled via CSS module
    <div className={styles.toDoRow} key={todo.id}>
      {/* Checkbox for marking a task as completed or not */}
      <input
        className={styles.toDoCheckbox}
        name="completed" // Will be used as key when updating todo state
        type="checkbox"
        checked={todo.completed} // Reflects the current completion state
        value={todo.completed}
        onChange={(e) => onChange(e, todo.id)} // Calls parent handler with change event and todo ID
      />

      {/* Text input field for editing the name/title of the task */}
      <input
        className={styles.todoInput}
        autoComplete="off" // Prevents browser from autofilling
        name="name"
        type="text"
        value={todo.name}
        onChange={(e) => onChange(e, todo.id)} // Updates name as user types
      />

      {/* Delete button with icon – calls delete handler when clicked */}
      <button className={styles.deleteBtn} onClick={() => onDelete(todo.id)}>
        <Image src="/delete-outline.svg" width="24" height="24" />
      </button>
    </div>
  );
}

/*
Notes – ToDo Component in React with Next.js

1. `import Image from 'next/image'`
   → This is Next.js's built-in component for optimized image rendering.
   → It helps load images faster and with better performance across devices.

2. `import styles from '../styles/todo.module.css'`
   → Imports scoped CSS styles using a CSS Module.
   → This ensures styles are only applied to this component and don't conflict globally.

3. `export default function ToDo(props)`
   → Defines a functional React component that accepts `props` from its parent.
   → Here, the props include the todo item object and event handler functions.

4. `const { todo, onChange, onDelete } = props;`
   → Destructures the individual properties from the props object for cleaner access in JSX.

5. `<input type="checkbox" ... />`
   → Renders a checkbox that reflects the "completed" state of the todo.
   → When changed, it calls the `onChange` function passed from the parent.

6. `<input type="text" ... />`
   → Renders a text input to edit the name of the todo item.
   → Also calls the same `onChange` handler with the new text value.

7. `<button onClick={...}><Image ... /></button>`
   → Renders a button with a trash icon that, when clicked, deletes the todo item.
   → Calls the `onDelete` function with the specific todo's ID.

In short:
This component is a single to-do item row, showing a checkbox to toggle completion, a text field to rename the task, and a delete button. It receives all data and handlers via props, making it clean, reusable, and easy to test.
*/
