from dotenv import load_dotenv
load_dotenv(override=True)

import os

from fasthtml.common import *
app = FastHTML()

@app.get("/")
def home():
    chatflow_id = os.getenv("CHATFLOW_ID")
    chatflow_host = os.getenv("CHATFLOW_HOST")
    print(chatflow_id, chatflow_host)
    page = Html(
        Head(Title('Desy on the job hunt')),
        Body(
            NotStr("""
                <div id="outer" style="width:100%; display: flex;justify-content: center;">
                    <div id="inner" style="border: 0.05em solid black;">
                        <flowise-fullchatbot></flowise-fullchatbot>
                    </div>
                </div>
                <script type="module">
                    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
                    Chatbot.initFull({
                        chatflowid: "5c3aa360-7c72-4c06-a2b5-2fac729df462",
                        apiHost: "https://flow-vl9b.onrender.com",
                        theme: {
                            chatWindow: {
                                showTitle: true,
                                title: 'Moli',
                                titleAvatarSrc: 'https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/google-messages.svg',
                                showAgentMessages: true,
                                welcomeMessage: 'G\\'day! Before we start, may I ask your name and the company you work at? 😊',
                                errorMessage: 'Something is wrong, please try again',
                                backgroundColor: "#ffffff",
                                //backgroundImage: 'enter image path or link', // If set, this will overlap the background color of the chat window.
                                height: 700,
                                width: 400,
                                fontSize: 16,
                                //starterPrompts: ['What is a bot?', 'Who are you?'], // It overrides the starter prompts set by the chat flow passed
                                //starterPromptFontSize: 15,
                                clearChatOnReload: false, // If set to true, the chat will be cleared when the page reloads.
                                botMessage: {
                                    backgroundColor: "#f7f8ff",
                                    textColor: "#303235",
                                    showAvatar: true,
                                    avatarSrc: "https://raw.githubusercontent.com/zahidkhawaja/langchain-chat-nextjs/main/public/parroticon.png",
                                },
                                userMessage: {
                                    backgroundColor: "#3B81F6",
                                    textColor: "#ffffff",
                                    showAvatar: true,
                                    avatarSrc: "https://raw.githubusercontent.com/zahidkhawaja/langchain-chat-nextjs/main/public/usericon.png",
                                },
                                textInput: {
                                    placeholder: 'Type your question',
                                    backgroundColor: '#ffffff',
                                    textColor: '#303235',
                                    sendButtonColor: '#3B81F6',
                                    maxChars: 200,
                                    maxCharsWarningMessage: 'You exceeded the characters limit. Please input less than 200 characters.',
                                    autoFocus: true, // If not used, autofocus is disabled on mobile and enabled on desktop. true enables it on both, false disables it on both.
                                    sendMessageSound: true,
                                    // sendSoundLocation: "send_message.mp3", // If this is not used, the default sound effect will be played if sendSoundMessage is true.
                                    receiveMessageSound: true,
                                    // receiveSoundLocation: "receive_message.mp3", // If this is not used, the default sound effect will be played if receiveSoundMessage is true. 
                                },
                                feedback: {
                                    color: '#303235',
                                },
                                footer: {
                                    textColor: '#303235',
                                    text: 'Contact',
                                    company: 'Desy',
                                    companyLink: 'mailto:desyonthejobhunt@gmail.com',
                                }
                            }
                        }
                    })
                </script>
            """)
        )
    )
    return page

serve()