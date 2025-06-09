import styles from "../styles/layout.module.css";

export default function Layout(props) {
  return (
    <div className={styles.layout}>
      <h1 className={styles.title}>PDF CRUD App with LLM & Orchestration</h1>
      <p className={styles.subtitle}>
        By{" "}
        <a
          href="https://www.linkedin.com/in/derril-filemon-a31715319"
          target="_blank"
        >
          Derril Filemon
        </a>
      </p>
      {props.children}
    </div>
  );
}
