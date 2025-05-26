# PDF Manager Frontend

This is the frontend of the **PDF Manager App**, built with **Next.js** and deployed to **Vercel**. It connects to a FastAPI backend (hosted on Render) and allows users to upload and manage PDF files in a GCS bucket.

---

### 🌐 Live App

- **Frontend Vercel URL:** [https://pdf-manager-app.vercel.app](https://pdf-manager-app.vercel.app)
- **Deployment-specific URL:** [https://pdf-manager-l89tdxsbp-derrils-projects.vercel.app](https://pdf-manager-l89tdxsbp-derrils-projects.vercel.app)

---

### 🛠 Tech Stack

- **Framework:** Next.js (React)
- **Deployment:** Vercel
- **Backend API:** FastAPI (Render)
- **Cloud Storage:** Google Cloud Storage (GCS)

---

### ⚙️ Local Development

#### 1. Clone the repo

```bash
git clone https://github.com/derril-tech/langchain-level-1-2-3-apps.git
cd YOUR_FRONTEND_REPO
```

#### 2. Install dependencies

```bash
npm install
```

#### 3. Create a `.env.local` file

Create a `.env.local` file in the root of the project and add:

```
NEXT_PUBLIC_API_URL=https://pdf-manager-hb9i.onrender.com
```

> Replace the value if your backend URL is different.

#### 4. Run the dev server

```bash
npm run dev
```

Then visit: [http://localhost:3000](http://localhost:3000)

---

### 🚀 Deploy on Vercel

This app is configured for seamless deployment to [Vercel](https://vercel.com).

#### Environment variable:

| Name                  | Value                                   |
| --------------------- | --------------------------------------- |
| `NEXT_PUBLIC_API_URL` | `https://pdf-manager-hb9i.onrender.com` |

#### Steps:

1. Push your frontend code to a GitHub repo
2. Go to Vercel → "New Project"
3. Import your repo
4. Add the env variable shown above
5. Click **Deploy**

---

### 📦 Features

- Upload PDFs to GCS
- Store and retrieve metadata from PostgreSQL via FastAPI
- Display uploaded PDFs in a list
- Responsive and ready for expansion (delete, preview, etc.)

---

### ✨ Author

Built by Derril Filemon — full-stack AI engineer & developer  
🇳🇱 Dutch | 🇳🇴 Norwegian | 🇸🇪 Living in Sweden
