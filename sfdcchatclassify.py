from openai import OpenAI # Import the OpenAI class from the openai module to interact with the OpenAI API
import os

# Retrieve the OpenAI API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")
GPT_MODEL = "gpt-3.5-turbo"

# Define the prompt template for classifying customer service chat messages
prompt_template = """
Please classify the following customer service chat into one of the following categories: Sales, Billing, Account Issues, Technical Issues, or General. Based on the customer's message, assign the most appropriate category.

Examples:
1. Customer: "I'm interested in learning more about your premium subscription plan and its benefits."
   Classification: Sales

2. Customer: "I was charged twice for my last purchase. Can you help me with a refund?"
   Classification: Billing

3. Customer: "I can't log into my account even after resetting my password."
   Classification: Account Issues

4. Customer: "The app keeps crashing every time I try to open it. What should I do?"
   Classification: Technical Issues

5. Customer: "What are your customer service hours?"
   Classification: General

Now, classify the following customer chat:

Customer: "{customer_message}"
Classification:
"""

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

# Function to classify customer chat messages
def classify_customer_chat(customer_message):
    # Format the prompt with the given customer message
    prompt = prompt_template.format(customer_message=customer_message)
    
    # Call the OpenAI API to get the classification
    response = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': customer_message},
        ],
        model=GPT_MODEL,
        temperature=0, # Control the randomness of the output
        max_tokens=200, # Limit the length of the response
        top_p=0.5, # Use nucleus sampling
        n=1, # Number of completions to generate
        stop="Translate:", # Stop generating once the specified token is encountered
        frequency_penalty=0.6, # Penalize new tokens based on their existing frequency
        presence_penalty=0.8 # Penalize new tokens based on whether they appear in the text so far
    )
    
    # Extract the classification from the API response
    classification = response.choices[0].message.content
    return classification

# Test data for classification
test_messages = [
    "I'm interested in learning more about your premium subscription plan and its benefits.",
    "I was charged twice for my last purchase. Can you help me with a refund?",
    "I can't log into my account even after resetting my password.",
    "The app keeps crashing every time I try to open it. What should I do?",
    "What are your customer service hours?",
    "Do you offer any discounts for bulk purchases?",
    "Can I upgrade my current plan to a premium plan?",
    "Why was my credit card declined?",
    "I need a copy of my last invoice.",
    "How do I change the email address on my account?",
    "I accidentally deleted my account, can it be restored?",
    "The website is not loading on my browser.",
    "I'm getting an error code 500 when I try to access my account.",
    "Can you tell me about your company’s privacy policy?",
    "Where can I find the user manual for your product?"
]

# Classify each test message and print the results
for message in test_messages:
    classification = classify_customer_chat(message)
    print(f"Customer message: {message}")
    print(f"Classification: {classification}\n")

print('\nNow test your own - enter QUIT to come out ******\n')

# Start an infinite loop for user input
while True:
    # Prompt the user for input
    user_input = input("Enter the issue in detail (type 'quit' to exit):\n ")
    
    # Check if the input is the quit keyword
    if user_input.lower() == 'quit':
        # Exit the loop
        print("Exiting the loop. Goodbye!")
        break
    else:
        # Print the user input
        print(f"You entered: {user_input}")
        # Classify the user input and print the result
        res = classify_customer_chat(user_input)
        print(f"The output (classification): {res}")
