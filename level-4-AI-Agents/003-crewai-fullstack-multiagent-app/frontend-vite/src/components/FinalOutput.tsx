// === FINAL OUTPUT ===
// Renders the result JSON: blog + video links grouped by business area

import {
  Card,
  Title,
  Text,
  Stack,
  Group,
  Divider,
  Anchor,
  Box,
} from "@mantine/core";
import { BookOpen, Youtube } from "lucide-react";

interface FinalOutputProps {
  result: {
    [businessArea: string]: {
      blog_articles?: { title: string; url: string }[];
      youtube_videos?: { title: string; url: string }[];
    };
  } | null;
}

export default function FinalOutput({ result }: FinalOutputProps) {
  if (!result || typeof result !== "object") {
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
        <Text c="red.7" size="sm">
          ⚠️ No results available. The output may be malformed or missing.
        </Text>
      </Card>
    );
  }

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
      <Title order={4} mb="md">
        ✅ Final Results
      </Title>

      <Stack gap="xl">
        {Object.entries(result).map(([businessArea, data]) => (
          <Box key={businessArea}>
            <Title order={5} c="indigo.7" mb="xs">
              📌 {businessArea}
            </Title>

            {/* Blog Articles */}
            <Text size="sm" fw={600} c="gray.7" mb={4}>
              <Group gap={6} align="center">
                <BookOpen size={16} /> Blog Articles
              </Group>
            </Text>
            <Stack pl="md" gap="xs">
              {(data.blog_articles ?? []).map((article, index) => (
                <Anchor
                  key={index}
                  href={article.url}
                  target="_blank"
                  size="sm"
                >
                  {article.title}
                </Anchor>
              ))}
            </Stack>

            {/* YouTube Videos */}
            <Text size="sm" fw={600} c="gray.7" mt="sm" mb={4}>
              <Group gap={6} align="center">
                <Youtube size={16} /> YouTube Videos
              </Group>
            </Text>
            <Stack pl="md" gap="xs">
              {(data.youtube_videos ?? []).map((video, index) => (
                <Anchor key={index} href={video.url} target="_blank" size="sm">
                  {video.title}
                </Anchor>
              ))}
            </Stack>

            <Divider my="lg" />
          </Box>
        ))}
      </Stack>
    </Card>
  );
}

/**
 * 🧠 FRONTEND NOTES — FinalOutput.tsx (Mantine version)
 *
 * 🔹 Purpose:
 * - Displays the final structured output from the CrewAI system
 * - Grouped by business area (e.g., "Marketing")
 *
 * 🔹 Output Format:
 * result = {
 *   "Marketing": {
 *     blog_articles: [{ title, url }, ...],
 *     youtube_videos: [{ title, url }, ...]
 *   },
 *   ...
 * }
 *
 * 🔹 Mantine Components:
 * - `Card`, `Title`, `Text`, `Anchor`, `Stack`, `Divider`, `Group`, `Box`
 * - `lucide-react` icons: `BookOpen`, `Youtube`
 *
 * 🔹 Features:
 * - Lists blog articles and YouTube videos with clickable links
 * - Uses Mantine styling for layout and responsiveness
 * - Separated by dividers between business areas
 *
 * 🔹 UX Benefits:
 * - Users can easily explore structured results
 * - Mobile-friendly, accessible, and well-organized presentation
 */
