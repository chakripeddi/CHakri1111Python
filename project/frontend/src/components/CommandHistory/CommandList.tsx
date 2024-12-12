import React from 'react';
import { List, ListItem, ListItemText, Paper, Typography } from '@mui/material';
import { Command } from '../../types/command';
import { formatDate } from '../../utils/dateFormatter';

interface CommandListProps {
  commands: Command[];
}

const CommandList: React.FC<CommandListProps> = ({ commands }) => {
  return (
    <Paper className="p-4">
      <Typography variant="h6" className="mb-4">
        Command History
      </Typography>
      <List>
        {commands.map((command) => (
          <ListItem key={command.id} divider>
            <ListItemText
              primary={command.text}
              secondary={`${command.status} • ${formatDate(command.timestamp)}`}
              secondaryTypographyProps={{
                className: `status-${command.status.toLowerCase()}`,
              }}
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default CommandList;