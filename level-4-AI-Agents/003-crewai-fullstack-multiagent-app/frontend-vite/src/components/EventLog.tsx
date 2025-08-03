// === EVENT LOG COMPONENT ===
// Shows real-time logs + status updates

import {
  Card,
  Title,
  Text,
  Badge,
  Stack,
  ScrollArea,
  Group,
  Divider,
  Box,
} from "@mantine/core";

interface Event {
  timestamp: string;
  data: string;
}

interface Props {
  status: string | null;
  events: Event[];
}

export default function EventLog({ status, events }: Props) {
  const getStatusColor = (status: string | null) => {
    switch (status) {
      case "COMPLETE":
        return "green";
      case "ERROR":
        return "red";
      default:
        return "yellow";
    }
  };

  return (
    <Card
      shadow="sm"
      padding="lg"
      radius="md"
      withBorder
      maw={800}
      mx="auto"
      mt="xl"
    >
      <Group justify="space-between" align="center">
        <Title order={4} c="gray.8">
          📡 Event Log
        </Title>
        <Badge color={getStatusColor(status)} variant="light">
          {status || "PENDING"}
        </Badge>
      </Group>

      <Divider my="sm" />

      <ScrollArea h={300} pr="md">
        <Stack gap="sm">
          {events.map((event, i) => (
            <Box key={i}>
              <Text size="xs" c="dimmed">
                {new Date(event.timestamp).toLocaleTimeString()}
              </Text>
              <Text size="sm" c="gray.9" style={{ whiteSpace: "pre-wrap" }}>
                {event.data}
              </Text>
            </Box>
          ))}
        </Stack>
      </ScrollArea>
    </Card>
  );
}

/**
 * 🧠 FRONTEND NOTES — EventLog.tsx (Mantine version)
 *
 * 🔹 Purpose:
 * - Displays a live feed of backend progress
 * - Shows CrewAI job `status`: PENDING, COMPLETE, ERROR
 * - Streams timestamped `events` from the result polling
 *
 * 🔹 Props:
 * - `status`: current job status string
 * - `events`: list of event messages with timestamps
 *
 * 🔹 Mantine Components:
 * - `Card`, `Group`, `Badge`: Layout and status header
 * - `ScrollArea`, `Stack`, `Box`: Scrollable log list and grouping
 * - `Text`, `Divider`: Time + message formatting
 *
 * 🔹 Features:
 * - Color-coded status with Mantine badges
 * - Clean, minimal layout that matches Mantine theming
 * - Scrollable list for long logs
 *
 * 🔹 UX Benefit:
 * - Helps users feel like something is actively working
 * - Especially important in multi-agent systems that take a few seconds
 */
