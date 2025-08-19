# App welcomes users to OnBrand 
Print  "Hi, I'm OnBrand, I will help you nail brand tone and voice everytime."

# Program asks user to set 3 brand personality sliders:

   Print "For Casual (0) vs Formal (10), enter number that corresponds to how casual or formal your brand should sound".
   # User can only input integers 0 to 10. 
   Loop until valid input:
      If user enters invalid input negative numbers or numbers greater than 10, print "numbers should be from 0 to 10".
      If user enters invalid output like letter or sign; print "integers from 0 to 10 only"
      

If user enters valid input, 
   save value in fuction called CasFor 
   Print "Continue to next personality"
  
Print "For Playful (0) vs Serious (10), enter number that corresponds to how playful or serious your brand should sound".
   # User can only input integers 0 to 10. 
      If user enters invalid input negative numbers or numbers greater than 10, print "numbers should be from 0 to 10".
      If user enters invalid output like letter or sign; print "integers from 0 to 10 only"

If user enters valid input, 
   save value in fuction called PlaSer 
   Print "Continue to next personality"

Print "For Simple (0) vs Technical (10), enter number that corresponds to how simple or techincal your brand should sound".
   # User can only input integers 0 to 10. 
      If user enters invalid input negative numbers or numbers greater than 10, print "numbers should be from 0 to 10".
      If user enters invalid output like letter or sign; print "integers from 0 to 10 only"

If user enters valid input, 
   save value in fuction called SimTec 
   
Print "Generating personality description"

For program to generate and shows brand personality description based on slider combination

Create new function called CasFor_PlaSer_SimTec that takes input from the CasFor, PlaSer, and SimTec values above and include them in a prompt to Claude API. 

Ask Claude to create a brand personality description for a brand with the following details:
   a CasFor (Casual-Formal) Index of X where 0 is extremely casual, 5 is neither casual nor formal and 10 is extremely formal.
   and
   a PlaSer (Playful-Serious) Index of X where 0 is extremely playful, 5 is neither playful nor serious and 10 is extremely serious.
   and
   a SimTec (Simple-Technical) Index of X where 0 is extremely simple, 5 is neither simple nor technical and 10 is extremely technical.
Tell Claude to return a brand personality description that synthesizes a unique brand voice based on the CasFor_PlaSer_SimTec index. Enrich the brand personality analysis with insights across the following thoughts:

   How do these traits complement each other?
   Where do they create contrast or tension? If there's any potential tension, note that the tension can be productive and the tension is actually makes the voice more interesting and human. 
   Are there moments when one trait type might be more dominant than the others?

Present the brand personality description to the user  and print "Is this an accurate description for your brand? Y for Yes, N for No"
    # User can only input letters Y to N. 
      If user enters invalid input such as numbers or other letters other than "Y" or "N", print "Enter Y for Yes or N for No"
      If user enters Y
         Print "Saving Brand Personality Description"
         Save "Brand Personality Description in a text file named "BPD"
      If user enters N
        Print "Adjust brand personality parameters" 
        And return to
        # Program asks user to set 3 brand personality sliders:

   Print "For Casual (0) vs Formal (10), enter number that corresponds to how casual or formal your brand should sound".


