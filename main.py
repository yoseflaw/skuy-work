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
        Head(Title('Chat with me!')),
        Body(
            NotStr("""
                <flowise-fullchatbot></flowise-fullchatbot>
                    <script type="module">
                        import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
                        Chatbot.initFull({
                            chatflowid: "5c3aa360-7c72-4c06-a2b5-2fac729df462",
                            apiHost: "https://flow-vl9b.onrender.com",
                        })
                    </script>
            """)
        )
    )
    return page

serve()