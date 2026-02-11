export default function StatusBanner({ severity }) {
  const hasHigh = severity.High > 0;
  const hasMedium = severity.Medium > 0;

  const text = hasHigh
    ? "CRITICAL INCIDENT DETECTED"
    : hasMedium
    ? "POTENTIAL RISK DETECTED"
    : "No critical incidents detected";

  const color = hasHigh ? "#ef4444" : hasMedium ? "#f59e0b" : "#22c55e";

  return (
    <div className="card" style={{ borderColor: color }}>
      <h3 style={{ color, margin: 0 }}>{text}</h3>
    </div>
  );
}
