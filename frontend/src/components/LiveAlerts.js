export default function LiveAlerts({ alerts }) {
  return (
    <div className="card">
      <h2 className="glow">Live Alerts</h2>
      {alerts.length === 0 && <p>No active alerts</p>}

      {alerts.map((a, i) => (
        <div key={i} style={{ marginBottom: "10px" }}>
          <span className={`badge ${a.severity.toLowerCase()}`}>
            {a.severity}
          </span>
          <b> {a.process}</b>
          <div style={{ fontSize: "13px", opacity: 0.85 }}>{a.message}</div>
        </div>
      ))}
    </div>
  );
}
