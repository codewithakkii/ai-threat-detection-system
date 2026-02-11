export default function TopRisky({ data }) {
  return (
    <div className="card">
      <h2 className="glow">Top Risky Processes</h2>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th align="left">Process</th>
            <th>Severity</th>
            <th>Frequency</th>
          </tr>
        </thead>
        <tbody>
          {data.map((p, i) => (
            <tr key={i}>
              <td>{p.process}</td>
              <td>
                <span className={`badge ${p.severity.toLowerCase()}`}>
                  {p.severity}
                </span>
              </td>
              <td align="center">{p.frequency}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
