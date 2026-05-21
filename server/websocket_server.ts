import { WebSocketServer, WebSocket } from 'ws';

const PORT = 8080;
const wss = new WebSocketServer({ port: PORT });

console.log(`[*] AgentOS WebSocket Middleware running on ws://localhost:${PORT}`);

wss.on('connection', (ws: WebSocket) => {
  console.log('[+] Client connected to stream');
  
  ws.on('message', (message: string) => {
    // Broadcast the step received from Python to all frontend clients
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message.toString());
      }
    });
  });

  ws.on('close', () => {
    console.log('[-] Client disconnected');
  });
});
