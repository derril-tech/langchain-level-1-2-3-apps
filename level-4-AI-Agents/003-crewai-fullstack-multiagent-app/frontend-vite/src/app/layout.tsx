// === GLOBAL APP LAYOUT ===
// Wraps all pages with consistent Header and Mantine styling

import { Toaster } from "react-hot-toast";
import { ColorSchemeScript, Container } from "@mantine/core";
import Header from "../components/Header";
import { metadata } from "./metadata";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <ColorSchemeScript />
      </head>
      <body
        style={{
          backgroundColor: "#f8f9fa",
          color: "#1a1b1e",
          minHeight: "100vh",
          margin: 0,
        }}
      >
        <Header />
        <Container size="md" py="xl">
          {children}
        </Container>
        <Toaster position="top-right" />
      </body>
    </html>
  );
}
