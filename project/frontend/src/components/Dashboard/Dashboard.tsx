import React, { useState, useEffect } from 'react';
import { Container, Grid, Paper } from '@mui/material';
import VoiceRecorder from '../VoiceInput/VoiceRecorder';
import CommandList from '../CommandHistory/CommandList';
import TaskProgress from '../TaskProgress/TaskProgress';
import { useAuth } from '../../hooks/useAuth';
import { useCommands } from '../../hooks/useCommands';
import { Command } from '../../types/command';

const Dashboard: React.FC = () => {
  const { user } = useAuth();
  const { commands, addCommand, updateCommand } = useCommands();
  const [activeCommand, setActiveCommand] = useState<Command | null>(null);

  const handleRecordingComplete = async (audioBlob: Blob) => {
    const formData = new FormData();
    formData.append('audio', audioBlob);
    
    try {
      const response = await fetch('/api/process-command', {
        method: 'POST',
        body: formData,
      });
      
      const result = await response.json();
      const newCommand = {
        id: Date.now(),
        text: result.text,
        status: 'Processing',
        timestamp: new Date(),
      };
      
      addCommand(newCommand);
      setActiveCommand(newCommand);
    } catch (error) {
      console.error('Error processing command:', error);
    }
  };

  return (
    <Container maxWidth="lg" className="py-8">
      <Grid container spacing={4}>
        <Grid item xs={12} md={8}>
          <Paper className="p-6">
            <VoiceRecorder onRecordingComplete={handleRecordingComplete} />
            {activeCommand && (
              <TaskProgress
                command={activeCommand}
                onStatusUpdate={updateCommand}
              />
            )}
          </Paper>
        </Grid>
        <Grid item xs={12} md={4}>
          <CommandList commands={commands} />
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;