import React from 'react';
import { Box, Heading, Text, SimpleGrid, Flex } from '@chakra-ui/react';

const tasks = {
  todo: [
    { id: 1, title: 'Tarea 1', description: 'Descripción de la tarea 1' },
    { id: 2, title: 'Tarea 2', description: 'Descripción de la tarea 2' }
  ],
  inProgress: [
    { id: 3, title: 'Tarea 3', description: 'Descripción de la tarea 3' },
    { id: 4, title: 'Tarea 4', description: 'Descripción de la tarea 4' }
  ],
  done: [
    { id: 5, title: 'Tarea 5', description: 'Descripción de la tarea 5' },
    { id: 6, title: 'Tarea 6', description: 'Descripción de la tarea 6' }
  ]
};

const Column = ({ title, tasks }) => (
  <Box bg="gray.50" p={4} borderRadius="md" boxShadow="md">
    <Heading as="h2" size="md" mb={4}>{title}</Heading>
    <Flex direction="column" gap={4}>
      {tasks.map(task => (
        <Box key={task.id} bg="white" p={4} borderRadius="md" boxShadow="sm">
          <Heading size="sm">{task.title}</Heading>
          <Text mt={2}>{task.description}</Text>
        </Box>
      ))}
    </Flex>
  </Box>
);

function App() {
  return (
    <Box p={8} bg="gray.100" minH="100vh">
      <Heading mb={8}>Tablero de Proyecto</Heading>
      <SimpleGrid columns={3} spacing={6}>
        <Column title="Por hacer" tasks={tasks.todo} />
        <Column title="En progreso" tasks={tasks.inProgress} />
        <Column title="Completado" tasks={tasks.done} />
      </SimpleGrid>
    </Box>
  );
}

export default App;
