import React, { Component, ErrorInfo, ReactNode } from 'react';
import { Alert, AlertTitle, Button } from '@mui/material';

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Uncaught error:', error, errorInfo);
  }

  public render() {
    if (this.state.hasError) {
      return (
        <Alert 
          severity="error"
          action={
            <Button 
              color="inherit" 
              size="small"
              onClick={() => window.location.reload()}
            >
              RELOAD PAGE
            </Button>
          }
        >
          <AlertTitle>Something went wrong</AlertTitle>
          {this.state.error?.message || 'An unexpected error occurred'}
        </Alert>
      );
    }

    return this.props.children;
  }
}