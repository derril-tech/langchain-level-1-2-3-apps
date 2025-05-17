// Import the <Head> component from Next.js to manage the <head> section of the HTML document
import Head from "next/head";

// Import a custom layout component that wraps page content with a consistent structure
import Layout from "../components/layout";

// Import the ToDoList component which likely renders the list of tasks
import ToDoList from "../components/todo-list";

// Define the default export for this page, which Next.js will treat as the homepage (index.js under /pages)
export default function Home() {
  return (
    <div>
      {/* Head allows you to add elements to the <head> of your HTML page dynamically */}
      <Head>
        <title>Full Stack Book To Do</title>{" "}
        {/* Title that appears in the browser tab */}
        <meta name="description" content="Full Stack Book To Do" />{" "}
        {/* Meta tag for SEO and browser context */}
        <link rel="icon" href="/favicon.ico" />{" "}
        {/* The favicon shown in the browser tab */}
      </Head>

      {/* Layout wraps the main page content to provide consistent header/footer or styling */}
      <Layout>
        {/* This component handles displaying the actual to-do list */}
        <ToDoList />
      </Layout>
    </div>
  );
}

/*
Beginner Notes – Home Page Component in Next.js

1. `import Head from 'next/head'`
   → This lets us manage HTML <head> elements (like title, meta tags, favicon) inside a React component.
   → It’s essential for customizing SEO, browser tab title, and page metadata per route.

2. `import Layout from '../components/layout'`
   → Imports a reusable layout component to wrap our content in a consistent design.
   → Helps enforce shared structure (like headers, footers, spacing) across multiple pages.

3. `import ToDoList from '../components/todo-list'`
   → This component likely displays the actual list of to-do items.
   → By separating it into its own file, we make the app more modular and easier to maintain.

4. `export default function Home()`
   → This is a React component called `Home`, and it's the default export of this file.
   → In a Next.js app, files in the `/pages` directory automatically become routes—so this is the homepage.

5. `<Head> ... </Head>`
   → This JSX block updates the HTML <head> for the current page.
   → It allows per-page customization of metadata, which is useful for SEO and usability.

6. `<Layout> ... </Layout>`
   → Wraps the main content inside a reusable layout component.
   → This avoids duplicating layout code across multiple pages (e.g., headers, page padding).

7. `<ToDoList />`
   → The main content of the homepage—renders the list of tasks for users to view and manage.
   → Keeping it separate makes the code cleaner and allows for easier updates or testing.

In short:
This `Home` page sets up the foundation of a to-do app by using reusable components for layout and task display, while also managing SEO-related tags through Next.js’s `<Head>` component.
*/
