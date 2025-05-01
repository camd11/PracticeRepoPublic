label scene_rumor_mill:

    # Scene Description: Gather rumors in the tavern.

    ```renpy
    label scene_rumor_mill:
    
        scene bg tavern
        # Assuming a barkeep sprite exists with tags like 'neutral' and 'thoughtful'
        # And a position 'behind_counter'
        show barkeep neutral behind_counter
    
        "The Rusty Flagon bustled with its usual evening crowd. The air hung thick with the smell of cheap ale, roasted meat, and pipe smoke."
        "Laughter erupted from one corner, while a hushed, serious conversation took place in another. A perfect place to catch stray words on the wind."
    
        p "I should see what information I can glean while I'm here."
    
        "I walked up to the sturdy wooden bar, catching the eye of the portly man polishing a mug."
    
        p "An ale, if you please."
    
        b "Coming right up."
    
        "The barkeep drew a foaming tankard and slid it across the counter."
        "He gave me a considering look, the kind that sized up newcomers."
    
        b "Haven't seen you around much. Just passing through?"
    
        p "Something like that. Trying to get the lay of the land."
    
        b "Aye, plenty 'lay' around here. Depends what kind you're looking for."
    
        "This seemed like a good opening."
    
        menu:
            "Ask about recent happenings.":
                p "Anything interesting been going on lately? Seems a lively place."
    
                b "(Leaning closer) Lively, aye. And tense. Folks are whispering about the old watchtower again."
                b "Lights seen up there at night, they say. Strange ones. Nobody's gone up to look, not since..."
                b "Well, best leave old ghosts lie, eh?"
                p "Lights... Interesting. Thanks."
                b "Don't mention it. Just be careful if you go poking around."
    
            "Ask about any notable travelers.":
                p "Seen any interesting folk pass through? Besides myself, of course."
    
                b "(Chuckles) Always got comedians. Nah, been quieter than usual on the main road."
                b "Too quiet, some reckon. That merchant caravan from Silverstream is overdue by three days now."
                b "Old Man Hemlock expects his spices sharpish. Getting grumpier by the hour, he is."
                p "A missing caravan? Doesn't sound good."
                b "Happens. Weather, bandits... or worse. Who knows?"
    
            "Try to eavesdrop on nearby patrons.":
                p "Just enjoying the atmosphere for now."
                "I took a slow sip of my ale, trying to tune my ears to the conversations nearby."
    
                "From a table to my left, two grizzled men spoke in low tones."
                pt1 "...told him, don't go into the Whispering Woods after dark. Not now."
                pt2 "He never listens. Thinks those old tales are just stories."
                pt1 "Maybe. But somethin' spooked my dog near the edge last night. Whining and tucking its tail like the devil himself was there."
    
                "Further down the bar, a woman was complaining loudly."
                unknown "Honestly! The price of grain these days. It's robbery! And with the Duke's tax collector sniffing around again..."
    
                "Fragmented whispers, but they painted a picture of unease."
                p "(Thinking) Woods... taxes... the usual concerns, perhaps something more."
    
            "Just finish the drink and leave.":
                p "Just needed a quick drink. Thanks."
                b "Suit yourself. Safe travels."
                "I finished the ale quickly, the taste unremarkable."
                "No point lingering if I wasn't going to dig for information."
                jump scene_rumor_mill_end # Use jump to skip the final wrap-up dialogue
    
        # Common path after gathering some info (unless player chose to leave immediately)
        p "(Thinking) That's a start. Seems there are a few threads dangling around this town."
        "I finished the rest of my ale, the buzz of the tavern a low hum in the background."
        b "Anything else for you?"
        p "Not tonight. Thanks for the drink and the chat."
        b "Anytime. Watch your step out there."
    
    label scene_rumor_mill_end:
        "Leaving the warmth and noise of the Rusty Flagon behind, I stepped back out into the cool night air."
        # Optionally hide characters or transition out
        # hide barkeep
    
        # End of scene
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
