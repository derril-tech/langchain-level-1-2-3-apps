import styles from "../styles/layout.module.css";

export default function Layout(props) {
  return (
    <div className={styles.layout}>
      <h1 className={styles.title}>Full Stack App using ChatGPT</h1>
      <p className={styles.subtitle}>
        By{" "}
        <a
          href="https://www.linkedin.com/in/derril-filemon-a31715319"
          target="_blank"
        >
          Derril Filemon
        </a>{" "}
      </p>
      <p className={styles.subtitle}>Create Poems with your To Do Tasks</p>
      {props.children}
    </div>
  );
}
