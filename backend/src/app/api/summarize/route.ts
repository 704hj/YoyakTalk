import axios from "axios";

export async function POST(req: Request) {
  const { text } = await req.json();
  const response = await axios.post("http://localhost:8000/summarize", { text });
  return Response.json(response.data);
}