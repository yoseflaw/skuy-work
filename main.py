from dotenv import load_dotenv
load_dotenv(override=True)

import os

from fasthtml.common import *
app, rt = fast_app()


@app.get("/")
def home():
    return Titled("Skuy.ai",
        H3("Create a chatbot that fits your needs!"),
        P("Whether it’s for business, personal projects, or customer support, we will help you design, train, and deploy your own custom chatbot."), 
        P("Start building conversations that matter today!"),
        A("Contact Us", href="https://docs.google.com/forms/d/e/1FAIpQLSfGvM9qBK6R_EBbuNbY4FPzFOwqmfYohhKTahbNm4M7k3M_9w/viewform"),
        H3("Checkout our work: "), 
        Ul(Li(A("Desy on the job hunt", href="/chat/desy"))),
        H3("Want to create a bot?"),
        Ol(*[
           Li(*[Span("Fill out "), A("this form", href="https://docs.google.com/forms/d/e/1FAIpQLSfGvM9qBK6R_EBbuNbY4FPzFOwqmfYohhKTahbNm4M7k3M_9w/viewform")]),
           Li("Our team will contact you"),
           Li("Sit back and relax as we build the chatbot for you!")
        ])
    )

# For images, CSS, etc.
@app.get("/{fname:path}.{ext:static}")
def static(fname: str, ext: str):
  return FileResponse(f'{fname}.{ext}')

@app.get("/chat/desy")
def work_chat():
    chatflow_id = os.getenv("CHATFLOW_ID")
    chatflow_host = os.getenv("CHATFLOW_HOST")
    print(chatflow_id, chatflow_host)
    page = (
        Title("Desy on the job hunt"),
        Div(
            NotStr("""
                <flowise-fullchatbot></flowise-fullchatbot>
                <script type="module">
                    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
                    Chatbot.initFull({
                        chatflowid: "5c3aa360-7c72-4c06-a2b5-2fac729df462",
                        apiHost: "https://flow-vl9b.onrender.com",
                        theme: {
                            chatWindow: {
                                showTitle: true,
                                title: 'Moli',
                                titleAvatarSrc: 'https://github.com/yoseflaw/skuy-work/raw/main/assets/images/moli.jpeg',
                                showAgentMessages: true,
                                welcomeMessage: 'G\\'day! Before we start, may I ask your name and the company you work at? 😊',
                                errorMessage: 'Something is wrong, please try again',
                                backgroundColor: "#ffffff",
                                clearChatOnReload: false,
                                botMessage: {
                                    backgroundColor: "#f7f8ff",
                                    textColor: "#303235",
                                    showAvatar: false
                                },
                                userMessage: {
                                    backgroundColor: "#3B81F6",
                                    textColor: "#ffffff",
                                    showAvatar: false
                                },
                                textInput: {
                                    placeholder: 'Type your question',
                                    backgroundColor: '#ffffff',
                                    textColor: '#303235',
                                    sendButtonColor: '#3B81F6',
                                    maxChars: 200,
                                    maxCharsWarningMessage: 'You exceeded the characters limit. Please input less than 200 characters.',
                                    autoFocus: true,
                                    sendMessageSound: true
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
            """),
            id="main-container"
        )
    )
    return page

serve()