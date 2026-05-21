import os, re
for file in os.listdir("agents"):
    if file.endswith(".py"):
        path = os.path.join("agents", file)
        with open(path, "r") as f: content = f.read()
        
        content = content.replace("from langchain_openai import ChatOpenAI", "from langchain_google_genai import ChatGoogleGenerativeAI")
        content = re.sub(r"ChatOpenAI\(.*?\)", "ChatGoogleGenerativeAI(model=\"gemini-1.5-flash\", temperature=0.2)", content)
        
        with open(path, "w") as f: f.write(content)
