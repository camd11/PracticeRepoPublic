label scene_consult_silas:

    # Scene Description: Engage Quartermaster Silas directly, seeking information or clarification on the ship's situation and your role.

    ```renpy
    label scene_consult_silas:
        scene bg silas_office with fade
        "The Quartermaster's office is small, bordering on claustrophobic."
        "Charts are pinned haphazardly to the bulkhead walls, and stacks of ledgers threaten to spill from the single sturdy desk."
        "The air hangs thick with the smell of brine, damp paper, and stale lamp oil."
        show silas neutral at center
        "Silas sits hunched over a logbook, his face illuminated by a flickering lantern. He looks tired but alert, his eyes sharp."
        "I rap lightly on the open doorframe."
        mc "Quartermaster Silas? Do you have a moment?"
        s "(Looks up slowly, eyes narrowing) Barely. State your business. Quickly."
        "His voice is rough, like grinding stones. Not overtly hostile, but certainly not welcoming."
        mc "I was hoping for some clarification, sir. About the ship's current situation, and where I fit into things."
        s "You 'fit in' by doing the job assigned to you, same as everyone else. Follow orders, earn your rations."
        s "As for the 'situation'..."
        s "(He sighs, rubbing his temples) Supplies are tighter than a hangman's knot. The crew's restless. The sea hasn't been kind."
        s "Is that clear enough for you? Or is there something specific burrowing under your scalp?"
        "His gaze is direct, challenging. He's weighing my intentions."
    
        menu:
            "I'm concerned about the whispers I've heard.":
                # Cautious approach
                mc "There are whispers, Quartermaster. Unease among the crew. Talk of shortages, difficult decisions."
                mc "I want to understand so I can best contribute, not add to the problems."
                s "(Studies me for a long moment, tapping a pen against the logbook) 'Contribute'. An admirable goal."
                s "Whispers can be dangerous cargo, [player_name]. More dangerous than unmarked reefs."
                s "Loyalty is the anchor in these storms. Tell me, what's your assessment of Captain Thorne's command?" # Loyalty Test
    
                menu:
                    "The Captain is decisive. That's what's needed.":
                        mc "He seems decisive. In times like these, strong leadership is crucial, even if it's unpopular."
                        s "(Nods slowly, expression unreadable) Decisive, aye. Decisions have consequences, though. Remember that."
                        s "A safe answer. Perhaps too safe."
                        jump silas_info_fragmented
    
                    "Some decisions have caused friction.":
                        mc "Honestly? Some of the recent orders seem to have caused friction. Made the hands nervous."
                        s "(His eyes narrow slightly) Friction can wear away the strongest ropes. Or start fires."
                        show silas suspicious at center
                        s "Be careful what opinions you voice, and to whom. Loose talk sinks ships."
                        jump silas_dismissed_suspicious
    
                    "I focus on my duty, not command decisions.":
                        mc "My place isn't to judge command. My loyalty is to my duties and to this ship."
                        s "(A faint, humourless smile touches his lips) Practical. Keep your head down and your hands busy."
                        s "Perhaps that's the wisest course for everyone."
                        jump silas_info_fragmented
    
            "I need to know the truth, Quartermaster.":
                # Direct approach
                mc "With respect, sir, vague answers won't cut it. How bad are things? Are the rumours true? About supplies? About... other troubles?"
                s "(Leans back slightly, eyes hardening) Bold. Or reckless."
                show silas suspicious at center
                s "Truth is a rationed commodity, same as everything else. And I decide who gets a share."
                s "Why should I trust you with more than your duty roster?" # Loyalty Test
    
                menu:
                    "Because hiding problems makes them worse.":
                        mc "Because secrets breed uncertainty and fear. If there's a real problem, knowing helps us face it."
                        s "And telling the wrong soul could start a panic, or worse."
                        s "This isn't a debating society. It's a ship clinging to survival."
                        jump silas_dismissed_suspicious
    
                    "You don't have to trust me, just the facts.":
                        mc "You don't have to trust me personally. Just trust that accurate information helps everyone."
                        s "(Scoffs softly) Facts can be twisted, [player_name]. Like rope, they can bind or hang."
                        s "I deal in logistics, not philosophy."
                        jump silas_dismissed_suspicious # Still suspicious of the direct demand
    
                    "My survival depends on this ship. That's my motive.":
                        mc "Because my survival is tied to this ship's. I have every reason to want things to go right."
                        s "(Considers this, his expression calculating) Self-interest. An honest motive, at least."
                        s "Perhaps honesty warrants a sliver of truth."
                        jump silas_info_task_possible # Might give info or task
    
            "Is there anything I can do to help?":
                # Offer help approach
                mc "Things seem strained. If there's anything useful I can do, Quartermaster, any task that needs doing, I'd like to help."
                s "(Raises an eyebrow, surprised) Offering extra work? Either you're keen or naive."
                s "What's your angle? Trying to get in good favour?"
                mc "Just trying to be useful, sir. And understand the ship's workings better."
                s "(Strokes his chin thoughtfully) Hmm. Helpfulness is rare. Very well."
                s "Perhaps there *is* something."
                jump silas_task_assigned
    
    label silas_info_fragmented:
        show silas neutral at center
        s "Very well. Since you're so concerned about contributing..."
        s "He gestures towards a messy pile of manifests near the edge of the desk. Some pages look water-stained, others torn."
        s "The official records... they're not clean. Fragmented logs. Gaps in the cargo manifests, particularly around the time we encountered that derelict."
        s "Entries that don't quite tally with the stores we have, or the stores we *should* have."
        s "Makes planning difficult. Makes trusting the numbers difficult."
        mc "Missing supplies?"
        s "Or supplies that were never logged correctly. Or logged incorrectly deliberately."
        s "That's all I'll say. Keep your eyes open. And keep this conversation to yourself."
        s "Dismissed."
        "Fragmented logs. Deliberate errors? It's a worrying piece of information."
        jump after_silas_consult
    
    label silas_info_task_possible:
        show silas neutral at center
        s "Alright. Honesty gets you this much..."
        s "He taps the logbook he was reading."
        s "The numbers aren't adding up. Water casks that should be full, aren't. Medical supplies logged that I can't find listed in the dispensary inventory."
        s "The logs are fragmented, inconsistent. Like someone's been tearing out pages or spilling ink deliberately."
        s "Perhaps... perhaps your desire for self-preservation could be useful."
        s "Take a walk past the aft storage later. Locker 7. Just... observe. See if the seals look tampered with. Report back to me. Quietly."
        mc "I understand, Quartermaster."
        s "See that you do. Don't draw attention."
        # Set a flag for the task
        $ silas_task_observe_locker = True
        "A sliver of truth, and a task to go with it. A test, no doubt."
        jump after_silas_consult
    
    label silas_task_assigned:
        show silas neutral at center # Or thoughtful if available
        s "Alright, helpful hands are welcome, if they're discreet."
        s "The sailmaker mentioned needing a precise count of spare canvas bolts – the heavy-duty storm canvas specifically."
        s "The inventory sheet says twelve, but he swears it feels lighter when he was last in the loft."
        s "Go check the sail loft. Get an accurate count. Report back directly to me, no one else."
        s "The logs," he adds, lowering his voice slightly, "have been unreliable lately. Best to verify."
        mc "Consider it done, Quartermaster."
        s "Good. Be thorough, and keep it quiet."
        # Set a flag for the task
        $ silas_task_canvas_count = True
        "A simple task, but his mention of unreliable logs again suggests something more is going on."
        jump after_silas_consult
    
    label silas_dismissed_suspicious:
        show silas suspicious at center
        s "I don't like prying questions, especially when the answers could rock the boat."
        s "Tend to your duties and keep your concerns to yourself. That's the best way to serve this ship right now."
        s "Now, leave me be. I have actual work to do."
        "He turns pointedly back to his logbook, dismissing me completely."
        "I've gained nothing but his suspicion. Need to be more careful."
        jump after_silas_consult
    
    label after_silas_consult:
        hide silas with easeoutleft
        "I step out of the Quartermaster's cramped office, the heavy air seeming to follow me."
        "Whether I gained information, a task, or just suspicion, one thing is clear: Silas is navigating troubled waters, and the ship's logs hide secrets."
        # Scene concludes, perhaps jump to ship map or next event
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
