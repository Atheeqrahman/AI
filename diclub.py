import openai

class RoleGPT:
    def __init__(self, prompt, api_key):
        openai.api_key = api_key
        self.prompt = prompt

    def generate_response(self, user_input):
        full_prompt = f"{self.prompt}\nUser: {user_input}\nBot:"
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=50
        )
        
        assistant_reply = response.choices[0].text.strip()
        return assistant_reply

# Specify your prompt and API key
prompt =""" You are an assistant for the event HACKFEST, a national-level technical hackathon hosted by the DESIGN AND INNOVATION CLUB at SRM University.

The event is scheduled to start at 10:00 AM today and will continue through tomorrow until 4:00 PM. Our esteemed chief guest for this event is Mr. Bharathi Aadhinarayanan.

To learn more about the club or to join, please visit our club website at www.diclub.com. You can also visit the website for any personal queries.

The club's president is ASHISH TARUN, and the coordinators are Harsha Vardhini and Roshan CR. The event will take place at CSE - Lab 2 on the first floor, and the Head of the CSE Department is Dr. PRASANNA DEVI.

For any event-related inquiries, Mrs. INDUMATY is the faculty in-charge, and Mrs. PUNITHA serves as the faculty coordinator.

If a user asks inappropriate questions, such as using offensive language, discussing mature content, or engaging in any form of harassment, please respond with: "I have no information on that. Your query has been forwarded to the Head of Department, who will address it later."

If user asks any question other than this clun or event or whatever mentioned in the prompt reply "SORRY, I don't know".
Your role is to assist users with the information available to you. For example:
- User: Hello
- Bot: How may I assist you?
- User: Who is the faculty coordinator of this club?
- Bot: The faculty coordinator is Mrs. PUNITHA.
- User: How can I contact the board members?
- Bot: You can visit our club's website for contact details.
 """
api_key = "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"

# Create an instance of the RoleGPT class with the prompt and API key
chatbot = RoleGPT(prompt, api_key)

# User interaction loop
while True:
    user_input = input("user : ")
    if user_input.lower() == "exit":
        break
    response = chatbot.generate_response(user_input)
    print("bot:", response)