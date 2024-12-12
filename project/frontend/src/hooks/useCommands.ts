import { useState } from 'react';
import { Command } from '../types/command';

export const useCommands = () => {
  const [commands, setCommands] = useState<Command[]>([]);

  const addCommand = (command: Command) => {
    setCommands(prev => [...prev, command]);
  };

  const updateCommand = (id: number, updates: Partial<Command>) => {
    setCommands(prev =>
      prev.map(cmd =>
        cmd.id === id ? { ...cmd, ...updates } : cmd
      )
    );
  };

  return { commands, addCommand, updateCommand };
};