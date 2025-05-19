# ✅ Frontend – To-Do List App (Next.js)

[👉 Try the Live Demo](https://langchain-level-1-2-3-apps.vercel.app/)

This Level 3 project is the **frontend** for a full-stack To-Do List App built using **Next.js**. It connects to a FastAPI backend and uses PostgreSQL to store and manage tasks.

The app features a modern, styled UI, real-time task updates with debounced saving, and filters for active, completed, or all todos. It showcases frontend-backend integration, scoped CSS modules, and React state handling.

---

## 🧩 Concepts Used

- **Next.js** — for server-rendered React with optimized routing and deployment support.
- **React Hooks** — `useState`, `useEffect`, `useRef`, and `useCallback` for managing state and side effects.
- **Scoped CSS Modules** — component-level styling via `.module.css` files.
- **Debouncing** — using Lodash to limit API update frequency while typing.
- **Component Composition** — clean separation between `ToDoList`, `ToDo`, and `Layout` components.
- **Dynamic Filtering** — switch between all, active, and completed todos using UI filters.

---

## ▶️ How to Run

1. **Clone the repository** and navigate to the frontend project folder:

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd langchain-level-1-2-3-apps/level-3/01-to-do-app/frontend-nextjs/todo-app
```

2. **Install dependencies** using npm:

```bash
npm install
```

3. **Create a .env.local file** in the root of the todo-app folder:

```.env
NEXT_PUBLIC_API_URL=https://langchain-level-1-2-3-apps.onrender.com

```

4. Start the development server:

```bash
npm run dev
```

## 🔐 Setup Your Backend API

This frontend app depends on a backend API built with **FastAPI** and a **PostgreSQL** database.

To ensure everything works correctly:

1. Deploy the backend FastAPI app to [Render.com](https://render.com).
2. Your backend should be live at: [https://langchain-level-1-2-3-apps.onrender.com](https://langchain-level-1-2-3-apps.onrender.com)

3. Confirm the `/todos` route is working by visiting:

[https://langchain-level-1-2-3-apps.onrender.com/todos](https://langchain-level-1-2-3-apps.onrender.com/todos)
You should see a list of todos (or an empty list `[]` if the table is empty).

4. Make sure your frontend `.env.local` file has the following:

```env
NEXT_PUBLIC_API_URL=https://langchain-level-1-2-3-apps.onrender.com
```

---

## ▶️ Recreate the PostgreSQL `todos` Table

If you're resetting your backend or starting fresh, use the following SQL to recreate the required `todos` table:

```sql
CREATE TABLE todos (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  completed BOOLEAN DEFAULT false
);
```

## 🛠️ Setup Notes

This project is part of the **LangChain Level 3 Apps Collection**, focusing on full-stack development and frontend/backend integration.

Frontend stack and environment:

- **Next.js 14+**
- **React 18+**
- **Lodash (for debounce)**
- **Scoped CSS Modules**
- **Hosted on Vercel**
- **Connected to a FastAPI + PostgreSQL backend on Render**

This frontend demonstrates best practices in state management, API interaction, component design, and dynamic updates — preparing you for scalable and maintainable full-stack apps.

---

## 📁 File Structure

```text
todo-app/
├── components/
│ ├── layout.js # Page layout wrapper with consistent styling
│ └── todo.js # Individual ToDo item component
│
├── pages/
│ └── index.js # Main ToDo list page (uses Layout and ToDoList)
│
├── public/
│ └── delete-outline.svg # Trash icon used for the delete button
│
├── styles/
│ ├── layout.module.css # CSS styles for layout component
│ ├── todo-list.module.css # CSS styles for the main ToDo list view
│ └── todo.module.css # CSS styles for individual ToDo items
│
├── .env.local # Local environment variable file (API URL)
├── package.json # Project metadata and dependencies
└── README.md # You're reading it
```
