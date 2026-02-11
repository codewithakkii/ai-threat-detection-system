export default function ExportCSV({ data }) {
  const download = () => {
    const header = "process,severity,frequency\n";
    const rows = data
      .map(d => `${d.process},${d.severity},${d.frequency}`)
      .join("\n");

    const blob = new Blob([header + rows], { type: "text/csv" });
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "threat_report.csv";
    a.click();
  };

  return <button onClick={download}>⬇ Export Threat Report</button>;
}
