import styles from "../styles/layout.module.css";

export default function Layout(props) {
  return (
    <div className={styles.layout}>
      <h1 className={styles.title}>Basic PDF CRUD App</h1>
      <p className={styles.subtitle}>
        By{" "}
        <a
          href="http://www.linkedin.com/in/derril-filemon-a31715319"
          target="_blank"
        >
          Derril Filemon
        </a>{" "}
      </p>
      {props.children}
    </div>
  );
}
