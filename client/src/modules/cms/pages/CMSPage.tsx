import React, { useState } from 'react';
import { Text, Paper, Container, Title, Table, Button, TextInput, Textarea } from '@mantine/core';

interface Complaint {
  category: string;
  description: string;
}

const CMSPage: React.FC = () => {
  const [complaints, setComplaints] = useState<Complaint[]>([]);
  const [category, setCategory] = useState<string>('');
  const [description, setDescription] = useState<string>('');

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    setComplaints([...complaints, { category, description }]);
    setCategory('');
    setDescription('');
  };

  return (
    <Container>
      <Title>Complaint Management System (CMS)</Title>

      <Paper shadow="xs" p="md" mt="md">
        <form onSubmit={handleSubmit}>
          <TextInput
            label="Category"
            value={category}
            onChange={(event) => setCategory(event.target.value)}
            required
          />
          <Textarea
            label="Description"
            value={description}
            onChange={(event) => setDescription(event.target.value)}
            required
          />
          <Button type="submit" mt="md">
            Submit Complaint
          </Button>
        </form>
      </Paper>

      <Paper shadow="xs" p="md" mt="md">
        <Table>
          <thead>
            <tr>
              <th>Category</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {complaints.map((complaint, index) => (
              <tr key={index}>
                <td>{complaint.category}</td>
                <td>{complaint.description}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Paper>
    </Container>
  );
};

export default CMSPage;