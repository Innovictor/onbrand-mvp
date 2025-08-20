import anthropic
import os
from dotenv import load_dotenv
import time

load_dotenv()



def get_brand_personality_input(is_first_time=True):
    """Get brand personality settings from user via 3 sliders"""
    if is_first_time:
        print("Welcome to OnBrand - Let's define your brand personality")
    print()

    # Initialize variable before the loop
    
    
    # Get casual_formal_score
    while True:
        print("For Casual (0) vs Formal (10), enter number that corresponds to how casual or formal your brand should sound")
        user_input = input("Enter your score (0-10): ")


        try:
            score = int(user_input)
            if score < 0 or score > 10:
                print("numbers should be from 0 to 10")
                continue
            else:
                casual_formal_score = score
                break
        except ValueError:
            print("integers from 0 to 10 only")



     # Get playful_serious_score
    while True:
        print("For Playful (0) vs Serious (10), enter number that corresponds to how playful or serious your brand should sound")
        user_input = input("Enter your score (0-10): ")


        try:
            score = int(user_input)
            if score < 0 or score > 10:
                print("numbers should be from 0 to 10")
                continue
            else:
                playful_serious_score = score
                break
        except ValueError:
            print("integers from 0 to 10 only")


      # Get simple_technical_score
    while True:
        print("For Simple (0) vs Technical (10), enter number that corresponds to how simple or technical your brand should sound")
        user_input = input("Enter your score (0-10): ")


        try:
            score = int(user_input)
            if score < 0 or score > 10:
                print("numbers should be from 0 to 10")
                continue
            else:
                simple_technical_score = score
                break
        except ValueError:
            print("integers from 0 to 10 only")

    return casual_formal_score, playful_serious_score, simple_technical_score

    

def generate_personality_description(casual_formal, playful_serious, simple_technical):
    """Generate brand personality description using Claude API"""
    print("\n🤖 Analyzing your brand personality... (this may take a few seconds)")
    time.sleep(4)

    print("✨ Generating your unique brand voice description...")
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )

    prompt = f"""Create a brand personality description for a brand with the following details:

        - Casual-Formal Scale: {casual_formal}/10 (where 0-4 = casual territory, 5 = neutral, 6-10 = formal territory)
        - Playful-Serious Scale: {playful_serious}/10 (where 0-4 = playful territory, 5 = neutral, 6-10 = serious territory)  
        - Simple-Technical Scale: {simple_technical}/10 (where 0-4 = simple territory, 5 = neutral, 6-10 = technical territory)
        Based on these scores, this brand is:
            - Casual-leaning or Formal-leaning (score of {casual_formal})
            - Playful-leaning or Serious-leaning (score of {playful_serious})
            - Simple-leaning or Technical-leaning (score of {simple_technical})
        Return a brand personality description that synthesizes a unique brand voice based on the blend of scores. 
        Enrich the brand personality analysis with insights across the following thoughts:
            - How do these traits complement each other?
            - Where do they create contrast or tension? If there's any potential tension, note that the tension can be productive and the tension actually makes the voice more interesting and human
            - Are there moments when one trait type might be more dominant than the others?
            IMPORTANT: Provide the response in plain text format only. Do not use markdown formatting, asterisks, or hashtags. Use simple text formatting only.
            """


    response = client.messages.create(
            model="claude-sonnet-4-0",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
        )
    return response.content[0].text



def save_personality_description(description, score):
    """ Save brand personality description to file"""
    with open("brand_personality_description.txt", "w") as file:
        file.write(f"BRAND PERSONALITY DESCRIPTION\n")
        file.write(f"=" * 50 + "\n\n")
        file.write(f"Brand Scores:\n")
        file.write(f"Casual vs Formal: {score[0]}\n")
        file.write(f"Playful vs Serious: {score[1]}\n") 
        file.write(f"Simple vs Technical: {score[2]}\n\n")
        file.write("Description:\n")
        file.write(description)
    print("Brand personality saved to 'brand_personality_description.txt'")



def main():
    """Main program loop"""
    first_time = True

    while True:
        score = get_brand_personality_input(first_time)
        first_time = False
        print(f"\Your Brand Personality:")
        print(f"Casual vs Formal: {score [0]}")
        print(f"Playful vs Serious: {score[1]}")
        print(f"Simple vs Technical: {score[2]}")

        description = generate_personality_description(score[0], score[1], score[2])
        print(f"\n{description}")

        while True:
            confirm = input("\nIs this an accurate description of your brand personality? Y for Yes, N for No, E to Exit: ").strip().upper()
            if confirm == 'Y':
                print("✅ Saving Brand personality Description...")

                save_personality_description(description,score)
                time.sleep(2)
                print("\n🎉 Your brand personality has been saved successfully!")
                print("Thanks for using OnBrand! ✌🏽")
                return 
            elif confirm == 'N':
                print("🔄 Let's adjust your brand personality parameters...")
                break
            elif confirm == 'E':
                print("Thanks for using OnBrand! ✌🏽")
                exit()
            else:
                print("Enter Y for Yes or N for No or E to Exit")



if __name__ == "__main__":
    main()