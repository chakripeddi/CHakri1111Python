export interface Command {
  id: number;
  text: string;
  status: 'Processing' | 'Completed' | 'Failed';
  timestamp: Date;
}