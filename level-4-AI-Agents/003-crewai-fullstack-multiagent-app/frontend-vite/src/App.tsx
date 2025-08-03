import { Container, Stack, Box } from "@mantine/core";
import InputSection from "./components/InputSection";
import EventLog from "./components/EventLog";
import FinalOutput from "./components/FinalOutput";
import useCrewOutput from "./hooks/useCrewOutput";

export default function App() {
  const { inputId, status, events, result, isLoading, handleSubmit } =
    useCrewOutput();

  return (
    <Box
      bg="gray.0"
      py="xl"
      px="sm"
      style={{ minHeight: "100vh", color: "#1a1b1e" }}
    >
      <Container size="md">
        <Stack gap="xl">
          <InputSection
            onSubmit={handleSubmit}
            isLoading={isLoading}
            currentStatus={status}
          />

          {inputId && <EventLog events={events} status={status} />}
          {status === "COMPLETE" && result && <FinalOutput result={result} />}
        </Stack>
      </Container>
    </Box>
  );
}
