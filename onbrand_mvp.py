import anthropic
import os
from dotenv import load_dotenv
import time
from datetime import datetime

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


def analyze_content_with_claude(content, platform, description, score):
    """Send user's content to Claude for OnBrand analysis"""
    print("📡 Connecting to OnBrand's analysis engine for analysis")
    time.sleep(4)
    print(f"🔄 Analyzing your {platform} content...")

    # Professional error handling - let's wrap API calls in try/except
    try:
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        # Platform-specific guidance dictionary 
        platform_guidance = {
            'Twitter': 'considering Twitter\'s 280-character limit and conversational tone',
            'LinkedIn': 'considering LinkedIn\'s professional context and 1300-character optimal length',
            'Email': 'considering email marketing best practices and recipient engagement',
            'Blog': 'considering blog readability, SEO, and audience retention'
        }

        # Get the right guidance for the platform, with fallback
        platform_context = platform_guidance.get(platform, f'considering {platform} best practices')

        prompt = f"""You are an experienced Head of Content analyzing content against a specific brand personality.

        BRAND PERSONALITY:
        {description}

        BRAND SCORES:
            - Casual vs Formal: {score[0]}/10
            - Playful vs Serious: {score[1]}/10  
            - Simple vs Technical: {score[2]}/10

        CONTENT TO ANALYZE:
            Platform: {platform}
            Content: "{content}"

        Please provide analysis in this exact format:

            ONBRAND SCORE: [0-100 number]/100

        ASSESSMENT: [OnBrand/OffBrand]

        KEY INSIGHTS:
            [2-3 sentences explaining why this content does or doesn't match the brand personality, {platform_context}]

        SUGGESTIONS:
            [If content is already OnBrand, say "This content aligns well with your brand personality. No changes needed." 
            Otherwise, provide 2-3 specific, actionable improvements that would make it more OnBrand while being effective on {platform}]
            """

        response = client.messages.create(
            model = "claude-sonnet-4-0",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
            )
        
        return response.content[0].text
    # Handle specific API errors with user-friendly messages
    except anthropic.APIConnectionError:
        return "⚠️ Sorry, Onbrand couldn't establish a connection right now. Please check your internet connection and try again."
    except anthropic.APIStatusError as e:
        if e.status_code == 429:  # Rate limiting
            return "⚠️ Sorry, OnBrand's analysis engine is experiencing high demand right now. Please wait a moment and try again."
        else:
            return f"⚠️ Sorry, OnBrand's analysis engine encountered an error (Status: {e.status_code}). Please try again."
    except Exception as e:  # Catch-all for any other errors
        return "⚠️ Sorry, Onbrand couldn't analyze your content right now. Please try again."


            # Content analysis workflow
def analyze_content(description, score):
        """
        Analyze user content against their brand personality
        This runs AFTER the brand personality has been confirmed and saved
        """
        first_analysis = True
    
        while True: 
            if first_analysis:
                prompt_text = "\nWould you like to analyze content against this brand personality? "
            else:
                prompt_text = "\nWould you like to analyze another piece of content against this brand personality? "

            content_choice = input(prompt_text + "Y for Yes, N for No and Exit: ").strip().upper()
                                    
    
            if content_choice == 'Y':
                first_analysis = False
                #Platform selection loop

                while True:
                    print("\nWhat platform is this content for?")
                    print("[1] Twitter (280 chars max)")
                    print("[2] LinkedIn (1300 chars recommended, 3000 max)")
                    print("[3] Email (50-125 words recommended, keep under 500 words for best results)")
                    print("[4] Blog (max 1000 words recommended for testing)")
                    print("[E] Exit to main menu")
                    platform_choice = input("Enter 1, 2, 3, 4 or E:").strip()
                    
                            
                    if platform_choice == '1':
                        platform = "Twitter"
                        char_limit = 280
                        break
                    
                    elif platform_choice == '2':
                        platform = "LinkedIn"
                        char_limit = 3000
                        break

                    elif platform_choice == '3':
                        platform = "Email"
                        char_limit = None  # No hard limit, but we'll give guidance
                        break

                    elif platform_choice == '4':
                        platform = "Blog"
                        char_limit = None  # No hard limit
                        break

                    elif platform_choice == 'E':
                        return
                    
                    else:
                            print("Invalid input. Please enter 1-4 for platforms or E to Exit.")

                    # Content entry loop with tiered validation
                while True:
                    content = input(f"\nPaste/write your {platform} content here or type 'E' to exit:\n").strip()

                    if content.upper() == 'E':
                        return
                    # Character/word counting and validation
                    char_count = len(content)
                    word_count = len(content.split())

                    if platform == "Twitter" and char_count > 280:
                        print(f"Content too long ({char_count} characters). Max 280 characters for Twitter. Please shorten and try again.")
                        continue
        
                    elif platform == "LinkedIn" and char_count > 1300:
                        print(f"Content too long ({char_count} characters). Max 1300 characters for LinkedIn. Please shorten and try again.")
                        continue
        
                    elif platform == "Email":
                        if word_count > 500:  # MVP testing limit
                            print(f"Content too long ({word_count} words). OnBrand MVP testing limit is 500 words. Please shorten and try again.")
                            continue
                        elif word_count > 150:  # Recommendation warning
                            print(f"📏 Your email is {word_count} words. Recommended: 50-150 words for best engagement. Continue anyway? (Y/N)")
                            choice = input().strip().upper()
                            if choice != 'Y':
                                continue
                        break
        
                    elif platform == "Blog":
                        if word_count > 1000:  # MVP testing limit
                            print(f"Content too long ({word_count} words). OnBrand MVP testing limit is 1000 words. Please shorten and try again.")
                            continue
                        break
                                
                    else:
                         break  # Valid content for Twitter/LinkedIn within limits


                # At this point, we should have valid content
                
                
                

                # Call Claude for analysis
                analysis_result = analyze_content_with_claude(content, platform, description, score)

                # Display the results
                print("\n" + "="*50)
                print("🗂️ ONBRAND ANALYSIS RESULTS")
                print("="*50)
                print(analysis_result)


                # Save analysis to timestamped file
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
                filename = f"analysis_{platform.lower()}_{timestamp}.txt"

                try:
                    with open(filename, 'w') as f:
                        f.write("ONBRAND CONTENT ANALYSIS\n")
                        f.write("=" * 50 + "\n\n")
                        f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                        f.write(f"Platform: {platform}\n")
                        f.write(f"Content Length: {char_count} chars, {word_count} words\n")
                        f.write(f"Content Analyzed: {content}\n\n")
                        f.write("BRAND PERSONALITY REFERENCE:\n")
                        f.write(f"Casual vs Formal: {score[0]}/10\n")
                        f.write(f"Playful vs Serious: {score[1]}/10\n") 
                        f.write(f"Simple vs Technical: {score[2]}/10\n\n")
                        f.write("ANALYSIS RESULTS:\n")
                        f.write(analysis_result)

                    print(f"\n💾 Analysis saved to '{filename}'")

                except Exception as e:
                    print(f"\n⚠️ Could not save analysis to file: {e}")
                
                
            elif content_choice == 'N':
                print("Thanks for using OnBrand! ✌🏽")
                return # <- return to main(); main will exit right after

            else:
                print("Invalid input. Enter Y for Yes or N for No and Exit")

        

def main():
    """Main program loop"""
    first_time = True

    while True:
        score = get_brand_personality_input(first_time)
        first_time = False
        print(f"Your Brand Personality:")
        print(f"Casual vs Formal: {score [0]}")
        print(f"Playful vs Serious: {score[1]}")
        print(f"Simple vs Technical: {score[2]}")

        description = generate_personality_description(score[0], score[1], score[2])
        print(f"\n{description}")

        # inner confirmation loop to accept/adjust/exit

        while True:
            confirm = input("\nIs this an accurate description of your brand personality? " 
                            "Y for Yes, N for No, E to Exit: ").strip().upper()
            
            if confirm == 'Y':
                print("✅ Saving Brand personality Description...")
                save_personality_description(description,score)
                time.sleep(2)
                print("\n🎉 Your brand personality has been saved successfully!")   

                # CALL analyze_content() here. When user says 'N' there, it returns here.
                analyze_content(description, score)

                # end the program after the analysis loop finishes
                return #exit once this loop finishes

            elif confirm == 'N':
                print("🔄 Let's adjust your brand personality parameters...")
                break # back to outer loop to re-enter sliders

            elif confirm == 'E':
                print("Thanks for using OnBrand! ✌🏽")
                return # clean exit

            else:
                print("Enter Y for Yes or N for No or E to Exit")


if __name__ == "__main__":
    main()