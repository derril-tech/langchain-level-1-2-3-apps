// === INPUT SECTION ===
// Allows user to submit technologies and business areas

import {
  Title,
  Text,
  Paper,
  Group,
  Stack,
  Badge,
  Button,
  Box,
} from "@mantine/core";
import { useState } from "react";

interface InputSectionProps {
  onSubmit: (technologies: string[], businessareas: string[]) => void;
  isLoading: boolean;
  currentStatus: "PENDING" | "COMPLETE" | "ERROR" | null;
}

const techOptions = ["AI Agents", "Generative AI", "Chatbots", "RPA Bots"];
const bizOptions = [
  "Marketing",
  "Human Resources",
  "Customer Support",
  "Sales",
];

export default function InputSection({
  onSubmit,
  isLoading,
  currentStatus,
}: InputSectionProps) {
  const [technologies, setTechnologies] = useState<string[]>([]);
  const [businessareas, setBusinessareas] = useState<string[]>([]);

  const toggle = (
    value: string,
    selected: string[],
    setSelected: (v: string[]) => void
  ) => {
    setSelected(
      selected.includes(value)
        ? selected.filter((v) => v !== value)
        : [...selected, value]
    );
  };

  const handleClick = () => {
    if (technologies.length === 0 || businessareas.length === 0) return;
    onSubmit(technologies, businessareas);
  };

  const statusColor =
    currentStatus === "COMPLETE"
      ? "green"
      : currentStatus === "ERROR"
      ? "red"
      : "yellow";

  return (
    <Paper
      shadow="sm"
      radius="md"
      p="lg"
      withBorder
      maw={800}
      mx="auto"
      mt="xl"
    >
      <Stack gap="md">
        <Title order={3}>🎯 Start a Research Run</Title>

        {/* Technologies */}
        <Box>
          <Text size="sm" fw={500} mb={4}>
            Technologies
          </Text>
          <Group gap="xs" wrap="wrap">
            {techOptions.map((tech) => (
              <Button
                key={tech}
                variant={technologies.includes(tech) ? "filled" : "default"}
                color="indigo"
                size="xs"
                radius="xl"
                onClick={() => toggle(tech, technologies, setTechnologies)}
              >
                {tech}
              </Button>
            ))}
          </Group>
        </Box>

        {/* Business Areas */}
        <Box>
          <Text size="sm" fw={500} mb={4}>
            Business Areas
          </Text>
          <Group gap="xs" wrap="wrap">
            {bizOptions.map((area) => (
              <Button
                key={area}
                variant={businessareas.includes(area) ? "filled" : "default"}
                color="pink"
                size="xs"
                radius="xl"
                onClick={() => toggle(area, businessareas, setBusinessareas)}
              >
                {area}
              </Button>
            ))}
          </Group>
        </Box>

        {/* Status Indicator */}
        {currentStatus && (
          <Text ta="center" size="sm">
            Status: <Badge color={statusColor}>{currentStatus}</Badge>
          </Text>
        )}

        {/* Submit Button */}
        <Button
          fullWidth
          color="green"
          onClick={handleClick}
          loading={isLoading}
          radius="md"
          size="md"
        >
          {isLoading ? "Starting..." : "Start Research"}
        </Button>
      </Stack>
    </Paper>
  );
}

/**
 * 🧠 FRONTEND NOTES — InputSection.tsx (Mantine version)
 *
 * 🔹 Purpose:
 * - Collects input for technologies and business areas
 * - Starts backend research process on submit
 *
 * 🔹 Props:
 * - `onSubmit`: handler to start backend call
 * - `isLoading`: disables button
 * - `currentStatus`: displays job status
 *
 * 🔹 UI:
 * - Uses `Paper`, `Stack`, `Group`, `Text`, `Title`, `Badge`, `Button`, `Box`
 * - Toggle-style buttons for tech/business categories
 * - Status badge shows current processing state
 *
 * 🔹 Improvements:
 * - Responsive, mobile-friendly
 * - Full Mantine layout and behavior
 * - Clear visual feedback
 */
