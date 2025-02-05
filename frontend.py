import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function Chatbot() {
  const [messages, setMessages] = useState([
    { text: "Hello! I can help you create a Google Ads campaign. What's your business name?", sender: "bot" },
  ]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    const newMessages = [...messages, { text: input, sender: "user" }];
    setMessages(newMessages);
    setInput("");

    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await response.json();

    setMessages([...newMessages, { text: data.reply, sender: "bot" }]);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-100">
      <Card className="w-full max-w-lg p-4 shadow-md">
        <CardContent className="space-y-4">
          <div className="h-96 overflow-y-auto bg-white p-4 rounded-md shadow-sm">
            {messages.map((msg, index) => (
              <div key={index} className={`mb-2 text-${msg.sender === "bot" ? "left" : "right"}`}> 
                <span className={msg.sender === "bot" ? "bg-gray-200 p-2 rounded-md" : "bg-blue-500 text-white p-2 rounded-md"}> 
                  {msg.text}
                </span>
              </div>
            ))}
          </div>
          <div className="flex space-x-2">
            <Input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type your message..." />
            <Button onClick={sendMessage}>Send</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
