import React, { useEffect, useState } from 'react';

function App() {
  const [backendStatus, setBackendStatus] = useState(null);
  const [backendData, setBackendData] = useState(null);
  const [error, setError] = useState(null);

  // Replace with your deployed backend URL
  const API_BASE = "https://your-backend-service.onrender.com/api";

  useEffect(() => {
    // Test backend connectivity
    fetch(`${API_BASE}/listings`)
      .then((res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setBackendData(data);
        setBackendStatus('✅ Backend reachable');
      })
      .catch((err) => {
        setBackendStatus('❌ Backend unreachable');
        setError(err.message);
      });
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>🧪 Diagnostic Marketplace App</h1>

      {/* Test CSS */}
      <div style={{ margin: '20px 0', padding: '20px', backgroundColor: '#f0f0f0', borderRadius: '8px' }}>
        <h2>CSS Test</h2>
        <p>If you see this box styled with gray background and padding, CSS is loading correctly.</p>
      </div>

      {/* Backend status */}
      <div style={{ margin: '20px 0' }}>
        <h2>Backend Status</h2>
        <p>{backendStatus || 'Checking backend...'}</p>
        {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      </div>

      {/* Backend Data */}
      <div style={{ margin: '20px 0' }}>
        <h2>Sample Listings</h2>
        {backendData ? (
          <pre>{JSON.stringify(backendData, null, 2)}</pre>
        ) : (
          <p>No data received yet.</p>
        )}
      </div>
    </div>
  );
}

export default App;
