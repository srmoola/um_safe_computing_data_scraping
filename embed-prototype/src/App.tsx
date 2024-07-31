import "./App.css";
import ChatBot from "react-simple-chatbot";
import { ThemeProvider } from "styled-components";

const steps = [
  {
    id: "0",
    message: "Hey Geek!",

    trigger: "1",
  },
  {
    id: "1",

    user: true,
    trigger: "2",
  },
  {
    id: "2",

    message: "How can I help you?",
  },
];

const theme = {
  background: "#FFCB05",
  headerBgColor: "#00274C",
  headerFontSize: "20px",
  botBubbleColor: "#FFCB05",
  headerFontColor: "white",
  botFontColor: "#00274C",
  userBubbleColor: "#00274C",
  userFontColor: "#FFCB05",
};

const config = {
  floating: true,
  botAvatar: "/logo.png",
};

function App() {
  return (
    <>
      <div>Press the Icon on the Bottom Right to Open Chatbot!</div>
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
