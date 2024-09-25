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
                            chatflowid: \"""" + chatflow_id + """\",
                            apiHost: \"""" + chatflow_host + """\",
                        })
                    </script>
            """)
        )
    )
    return page

serve()