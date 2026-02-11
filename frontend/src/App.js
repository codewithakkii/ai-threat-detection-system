import { useEffect, useState } from "react";
import { getSeverity, getTopRisky, getLiveAlerts } from "./api";
import SeverityChart from "./components/SeverityChart";
import TopRisky from "./components/TopRisky";
import StatusBanner from "./components/StatusBanner";
import LiveAlerts from "./components/LiveAlerts";
import ExportCSV from "./components/ExportCSV";

function App() {
  
  const [severity, setSeverity] = useState({});
  const [topRisky, setTopRisky] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
  const load = async () => {
    const sev = await getSeverity();
    const risky = await getTopRisky();
    const alertsRes = await getLiveAlerts();
    setAlerts(alertsRes.data);
    setSeverity(sev.data);
    setTopRisky(risky.data);
  };

  load(); // initial
  const t = setInterval(load, 5000); // refresh every 5 sec
  return () => clearInterval(t);
}, []);

  return (
    <div style={{ background: "#0f172a", color: "#e5e7eb", minHeight: "100vh", padding: "20px" }}>
      <h1>AI Cyber Security Monitoring Dashboard</h1>
       <StatusBanner severity={severity} />

      <SeverityChart data={severity} />
      <TopRisky data={topRisky} />
      <ExportCSV data={topRisky} />
      <LiveAlerts alerts={alerts} />

    </div>
  );
}

export default App;
