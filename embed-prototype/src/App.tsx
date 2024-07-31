import "./App.css";
import ChatBot from "react-simple-chatbot";
import { ThemeProvider } from "styled-components";
import { config, theme } from "./chatbot-config";

const steps = [
  {
    id: "0",
    message: "Hey! How can I help?",
    trigger: "1",
  },
  {
    id: "1",
    user: true,
    trigger: "user-input",
  },
  {
    id: "user-input",
    message: ({ previousValue }: any) => {
      const userMessage = previousValue.toLowerCase();

      if (userMessage.includes("help")) {
        return "Sure, I can help you. What do you need assistance with?";
      } else if (userMessage.includes("issue")) {
        return "I'm sorry to hear that you're experiencing issues. Can you describe the problem in detail?";
      } else if (
        userMessage.includes("thanks") ||
        userMessage.includes("thank you")
      ) {
        return "You're welcome! Is there anything else I can assist you with?";
      } else {
        return "This is just a demo chatbot. I can't help you with that.";
      }
    },

    trigger: "1",
  },
];

function App() {
  return (
    <>
      <div>Press the Icon on the Bottom Right to Open Embedded Chatbot!</div>
      <div>
        This is just a UI prototype, press the link below to go to actual
        chatbot!
      </div>
      <a href="https://umgpt.umich.edu/maizey/Information-Assurance-AI-Chat">
        Working chatbot link
      </a>
      <ThemeProvider theme={theme}>
        <ChatBot
          headerTitle="UM SafeComputing Assistant"
          steps={steps}
          {...config}
        />
      </ThemeProvider>
    </>
  );
}

export default App;
