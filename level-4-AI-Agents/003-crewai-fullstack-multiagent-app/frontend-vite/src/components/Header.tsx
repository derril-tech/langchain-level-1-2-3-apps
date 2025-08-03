// === GLOBAL HEADER COMPONENT ===
// Displays app title and future navigation elements using Mantine

import { Container, Title, Text, Paper, Group } from "@mantine/core";

export default function Header() {
  return (
    <Paper
      shadow="sm"
      radius={0}
      py="sm"
      px="lg"
      withBorder
      style={{
        background:
          "linear-gradient(to right, var(--mantine-color-indigo-6), var(--mantine-color-pink-5))",
        color: "white",
      }}
    >
      <Container size="lg">
        <Group justify="space-between" align="center" wrap="wrap">
          <Title order={2} fw={700} style={{ color: "white" }}>
            🚀 CrewAI Researcher
          </Title>
          <Text size="sm" style={{ color: "white", opacity: 0.9 }}>
            Powered by <strong>GPT-4o</strong> + <strong>CrewAI</strong>
          </Text>
        </Group>
      </Container>
    </Paper>
  );
}

/**
 * 🧠 FRONTEND NOTES — Header.tsx (Mantine version)
 *
 * 🔹 Purpose:
 * - Displays a consistent app title and subtitle across all pages
 *
 * 🔹 Structure:
 * - `Paper`: styled header bar with gradient background
 * - `Container` and `Group`: ensure layout remains centered and spaced
 * - `Title`: shows main app heading
 * - `Text`: shows subheading (GPT-4o + CrewAI)
 *
 * 🔹 Styling:
 * - Gradient from indigo to pink using Mantine colors
 * - White foreground text with spacing and responsiveness
 *
 * 🔹 Benefits:
 * - Clean and elegant branding area
 * - Flexible layout for future navigation or action buttons
 */
