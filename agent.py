from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

# This data is hidden to the LLM itself
sensitive_data = {'rhoai_password': os.getenv("RHOAI_PASSWORD")}

# Initialize the model, e.g.
# llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(os.getenv('GEMINI_API_KEY'))) - if using ollama, api_key will not be needed
task = f"""
   ### Prompt for Data Scientist Assistant - Red Hat OpenShift AI

**Objective:**
Visit the [RHOAI dashboard]({os.getenv("RHOAI_DASHBOARD_URL")}), go to the model registry section, register a new model called gemini-2.0-flash

**Important:**
- If you are required to log in, use the {os.getenv("RHOAI_IDP")} identity provider with username {os.getenv("RHOAI_USERNAME")} and password rhoai_password
- If you don't see the Model registry section anywhere, try looking under the Models section
---

### Step 1: Navigate to the Website
- Open the [RHOAI dashboard]({os.getenv("RHOAI_DASHBOARD_URL")}).
- If required, log in as {os.getenv("RHOAI_USERNAME")}
- If required, ignore the security warning

---

### Step 2: Navigate to Model registry page
- You should be able to find a link to the model registry page on the left navbar
- If you do not see it right away, try looking under the Models section
- Once you get to the model registry page, if there is a "loading" message try waiting for a bit, and if the page doesn't fully load in a reasonable time try refreshing until you see the fully loaded page
- If there are models already registered, check their names and ensure that in the next step you use a different name

---

### Step 3: Register a new model
- Start the process of registering a new model
- When filling out the details, give it the name gemini-2.0-flash + current time
- **Important:** After filling in any of the fields, confirm that the UI does not show you an error message like "Model name already exists". If it does, try using a different value.
- In the description, leave a short message saying who you are and what you're doing
- If there are any other required fields, put any data you want there
- The storage details are not important for now, you can use placeholder values
- Remember to click the button after filling out the details to ensure the model is actually registered

---

### Step 4: Confirm model has been registered
- Once you've registered the model, navigate back to the Model registry page and confirm the model has been successfully registered


**Important:** Ensure efficiency and accuracy throughout the process."""


async def main():
    agent = Agent(
        task=task,
        llm=llm,
        sensitive_data=sensitive_data
    )
    result = await agent.run()
    print(result)

asyncio.run(main())