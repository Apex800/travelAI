import openai
import streamlit as st  # Replace with gradio if using Gradio

# Set up OpenAI API key
openai.api_key ="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"
def refine_user_inputs():
    st.title("AI Travel Planner")
    destination = st.text_input("Where do you want to travel?")
    days = st.number_input("How many days?", min_value=1, step=1)
    budget = st.text_input("Your budget?")
    dietary = st.text_input("Dietary preferences (e.g., vegetarian, vegan)?")
    activities = st.text_input("What activities do you enjoy?")
    mobility = st.text_input("Any mobility concerns or walking limits?")
    accommodation = st.text_input("Accommodation preference (luxury, budget, central location)?")
    return destination, days, budget, dietary, activities, mobility, accommodation

# Function: Suggest activities
def suggest_activities(destination, preferences):
    messages = [
        {"role": "system", "content": "You are a helpful travel assistant."},
        {
            "role": "user",
            "content": f"""
            Suggest top-rated attractions in {destination} and unique experiences tailored to the following preferences: {preferences}.
            Include hidden gems, must-visit landmarks, and a mix of relaxing and adventurous activities.
            """,
        },
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"].strip()

# Function: Generate itinerary
def generate_itinerary(destination, days, budget, dietary, activities, mobility, accommodation):
    messages = [
        {"role": "system", "content": "You are a helpful travel assistant."},
        {
            "role": "user",
            "content": f"""
            Create a detailed {days}-day travel itinerary for {destination}. Consider the following:
            - Budget: {budget}
            - Dietary preferences: {dietary}
            - Activities: {activities}
            - Mobility concerns: {mobility}
            - Accommodation: {accommodation}
            Provide a day-by-day breakdown, including activity timings, meal recommendations, and travel tips.
            """,
        },
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"].strip()

# Main Streamlit App
def main():
    # Collect inputs
    destination, days, budget, dietary, activities, mobility, accommodation = refine_user_inputs()
    
    # Generate itinerary on button click
    if st.button("Generate Itinerary"):
        if all([destination, days, budget, dietary, activities, mobility, accommodation]):
            itinerary = generate_itinerary(destination, days, budget, dietary, activities, mobility, accommodation)
            st.subheader("Your Itinerary:")
            st.write(itinerary)
        else:
            st.error("Please fill out all fields!")

if __name__ == "__main__":
    main()
