import anthropic
import os
from dotenv import load_dotenv
import time

load_dotenv()
print(f"DEBUG: API key exists: {os.getenv('ANTHROPIC_API_KEY') is not None}")
print(f"DEBUG: API key length: {len(os.getenv('ANTHROPIC_API_KEY', ''))}")


def get_brand_personality_input():
    """Get brand personality settings from user via 3 sliders"""
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
    time.sleep(2)

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
            - Are there moments when one trait type might be more dominant than the others?"""


    response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
        )
    return response.content[0].text


def main():
    """Main program loop"""
    score = get_brand_personality_input()
    print(f"\Your Brand Personality:")
    print(f"Casual vs Formal: {score [0]}")
    print(f"Playful vs Serious: {score[1]}")
    print(f"Simple vs Technical: {score[2]}")

    description = generate_personality_description(score[0], score[1], score[2])
    print(f"\n{description}")


if __name__ == "__main__":
    main()