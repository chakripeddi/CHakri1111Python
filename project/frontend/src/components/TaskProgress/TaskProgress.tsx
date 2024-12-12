import React from 'react';
import { LinearProgress, Typography, Paper } from '@mui/material';
import { Command } from '../../types/command';

interface TaskProgressProps {
  command: Command;
  onStatusUpdate: (id: number, updates: Partial<Command>) => void;
}

const TaskProgress: React.FC<TaskProgressProps> = ({ command, onStatusUpdate }) => {
  return (
    <Paper className="mt-4 p-4">
      <Typography variant="subtitle1" className="mb-2">
        Processing: {command.text}
      </Typography>
      <LinearProgress 
        variant="indeterminate"
        className={`status-${command.status.toLowerCase()}`}
      />
      <Typography variant="caption" className="mt-2 block">
        Status: {command.status}
      </Typography>
    </Paper>
  );
};

export default TaskProgress;