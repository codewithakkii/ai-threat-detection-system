import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

export default function SeverityChart({ data }) {
  const chartData = Object.keys(data).map(key => ({
    name: key,
    value: data[key]
  }));

  return (
    <BarChart width={400} height={250} data={chartData}>
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="value" fill="#00e5ff" />
    </BarChart>
  );
}
