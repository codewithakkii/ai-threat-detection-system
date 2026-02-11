import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const getSeverity = () => API.get("/analytics/severity");
export const getTopRisky = () => API.get("/analytics/top-risky");
export const getLiveAlerts = () => API.get("/alerts/live");
