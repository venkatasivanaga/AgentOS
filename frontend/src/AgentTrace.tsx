import React, { useState, useEffect } from 'react';

export const AgentTrace = () => {
  const [steps, setSteps] = useState<any[]>([]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8080');
    
    ws.onmessage = (event) => {
      const newStep = JSON.parse(event.data);
      setSteps((prev) => [...prev, newStep]);
    };
    
    return () => ws.close();
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'monospace', background: '#1e1e1e', color: '#00ff00', borderRadius: '8px' }}>
      <h2 style={{ color: '#ffffff', marginBottom: '16px' }}>AgentOS Live Trace</h2>
      {steps.length === 0 && <p style={{ color: '#888' }}>Waiting for tasks...</p>}
      {steps.map((step, i) => (
        <div key={i} style={{ marginBottom: '8px' }}>
          <span style={{ color: '#4da6ff' }}>[{step.agent}]</span> {step.action} 
          <span style={{ color: '#888', marginLeft: '10px' }}>({step.duration_ms}ms)</span>
        </div>
      ))}
    </div>
  );
};
