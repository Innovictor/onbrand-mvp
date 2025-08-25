# App welcomes users to OnBrand
Print "Welcome to OnBrand MVP - Let's define your brand personality"

# Main program loop
Loop until user exits:

    # Create function called get_brand_personality_input
    Function get_brand_personality_input:

        Get casual_formal_score
        Loop until valid input:
            Print "For Casual (0) vs Formal (10), enter number that corresponds to how casual or formal your brand should sound"
            Get user input
            If user enters invalid input (negative numbers or numbers greater than 10):

                Print "numbers should be from 0 to 10"
                Continue loop
            If user enters invalid input (letters or symbols):
                Print "integers from 0 to 10"
                Continue loop
            If user enters valid input:
                Store casual_formal_score = user_input
                Break loop


        Get Playful_serious_score
        Loop until valid input:
            Print "For Playful (0) vs Serious (10), enter number that corresponds to how playful or serious your brand should sound"
                Get user input
            If user enters invalid input (negative numbers or numbers greater than 10):

                Print "numbers should be from 0 to 10"
                Continue loop
            If user enters invalid input (letters or symbols):
                Print "integers from 0 to 10"
                Continue loop
            If user enters valid input:
                Store playful_serious_score = user_input
                Break loop


        Get simple_technical_score
        Loop until valid input:
            Print "For Simple (0) vs Technical (10), enter number that corresponds to how simple or technical your brand should sound"
                Get user input
            If user enters invalid input (negative numbers or numbers greater than 10):

                Print "numbers should be from 0 to 10"
                Continue loop
            If user enters invalid input (letters or symbols):
                Print "integers from 0 to 10"
                Continue loop
            If user enters valid input:
                Store simple_technical_score = user_input
                Break loop
        
        Return casual_formal_score, playful_serious_score, simple_technical_score from get_brand_personality_input function

    Print "Generating personality description"

    # Generate brand personality description using Claude API

    Ask Claude to create a brand personality description for a brand with the following details:
        - casual_formal_score of [score] where 0 is extremely casual, 5 is neither casual nor formal and 10 is extremely formal
        - playful_serious_score of [score] where 0 is extremely playful, 5 is neither playful nor serious and 10 is extremely serious
        - simple_technical_score of [score] where 0 is extremely simple, 5 is neither simple nor technical and 10 is extremely technical

    Tell Claude to return a brand personality description that synthesizes a unique brand voice based on the blend of scores.
    Enrich the brand personality analysis with insights across the following thoughts:
        - How do these traits complement each other?
        - Where do they create contrast or tension? If there's any potential tension, note that the tension can be productive and makes the voice more interesting and human
        - Are there moments when one trait type might be more dominant than the others?
    
    Get brand_personality_description from Claude API

        # Confirmation loop
        Loop until user confirms or adjusts:
            Print brand_personality_description to user
            Print "Is this an accurate description of your brand? Y for Yes, N for No"

            
            Loop until valid input:
                Get user input
                If user enters invalid input (not Y or N):
                    Print "Enter Y for Yes and N for No"
                    Continue loop
                If user enters Y:
                    Print "Saving Brand Personality Description"
                    Save brand_personality_description to text file named "BPD"
                    Break confirmation loop
                If user enters N:
                    Print "Adjust brand personality parameters"
                    Break to outer loop (return to get_brand_personality_input)



