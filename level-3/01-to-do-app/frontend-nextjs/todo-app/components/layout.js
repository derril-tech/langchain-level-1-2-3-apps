// Import the CSS module for styling. This keeps styles scoped to this component.
import styles from "../styles/layout.module.css";

// Define a React functional component called Layout that receives `props`
export default function Layout(props) {
  return (
    // Apply a layout container style from the CSS module
    <div className={styles.layout}>
      {/* Render the main page title with a CSS class for styling */}
      <h1 className={styles.title}>To Do</h1>

      {/* Render any child components or content passed inside <Layout> ... </Layout> */}
      {props.children}
    </div>
  );
}

/*
Notes – Layout Component in React with CSS Modules

1. `import styles from '../styles/layout.module.css'`
   → This imports styles from a CSS module file. 
   → CSS Modules scope the styles to this specific component to avoid global style conflicts.

2. `export default function Layout(props)`
   → Defines a functional React component named `Layout`.
   → The `props` parameter is used to access content or data passed from a parent component.

3. `<div className={styles.layout}>`
   → This creates a <div> with a CSS class applied using the scoped `styles.layout`.
   → The styling comes from the imported CSS module file.

4. `<h1 className={styles.title}>To Do</h1>`
   → Renders an `<h1>` header with the text "To Do", styled via `styles.title`.

5. `{props.children}`
   → This special React syntax renders whatever is passed between the `<Layout>...</Layout>` tags.
   → It makes the layout flexible and reusable by allowing dynamic content insertion.

In short: 
This component provides a styled wrapper for page content with a heading, and can wrap any content passed into it through `props.children`. It's a reusable pattern for consistent page structure.
*/
