label scene_quarterdeck_summons:

    # Scene Description: An urgent summons calls you to the quarterdeck. Silas awaits, perhaps with orders or questions.

    ```renpy
    label scene_quarterdeck_summons:
    
        scene bg quarterdeck with dissolve
        play sound "sfx/wind_strong_loop.ogg" fadein 1.0 volume 0.6
    
        "The salt spray stung my face as I climbed the final steps to the quarterdeck. The summons had been sharp, urgent."
        "Below, the grey sea churned, mirroring the unease twisting in my gut."
    
        show silas stern at center with easeinleft
    
        "Silas stood near the railing, his back straight as the mainmast, gazing out at the turbulent water. His usual meticulous appearance seemed slightly ruffled by the persistent wind whipping across the deck."
        "He didn't turn immediately as I approached, his silence amplifying the tension."
    
        mc "Quartermaster Silas? You summoned me?"
    
        "He finally turned, his eyes sharp and assessing. There were no pleasantries today."
        s "Took you long enough. We don't have time for dawdling."
    
        "His voice was clipped, carrying easily over the howl of the wind."
        s "Something's come up. Something that requires... discretion."
    
        "He stepped closer, lowering his voice slightly, though his gaze remained intense."
        s "Intelligence suggests a nearby patrol vessel isn't where it's supposed to be. Vanished from its expected route."
    
        mc "Vanished? Pirates? Or something else?"
    
        s "That's the question, isn't it? It could be misfortune. Or it could be they've turned coat, waiting to ambush vessels like ours."
        s "Worse, it could be a sign of something bigger brewing in these waters."
    
        "He scanned the horizon again, briefly, before fixing his gaze back on me."
        s "The Captain wants eyes on the situation, but sending a scout boat is too obvious, too risky if it's a trap."
        s "We need someone to go ashore at the next port, Port Azure, ostensibly for supplies. Quietly ask around, listen to the dock chatter, see if anything about the patrol ship 'Sea Serpent' comes up."
    
        "His eyes narrowed, pinning me in place."
        s "It needs to look routine. No suspicion drawn. But I need reliable information, not dockside rumours passed off as fact."
        s "You've got a way about you. People talk. But are you sharp enough to sift the truth from the lies?"
    
        menu:
            "This sounds dangerous. What if they're watching the port?":
                mc "Going ashore alone seems risky, Quartermaster. If they *have* turned or are waiting, Port Azure could be crawling with their eyes."
                s "Risk is the currency of this life. Of course, it's dangerous. That's why I'm asking *you*."
                s "Are you capable of handling it, or should I find someone else who understands the stakes?"
                mc "I understand the stakes. I can handle it."
                s "Good. Don't disappoint me. Gather legitimate supplies first, make it look convincing. Then listen."
                jump scene_quarterdeck_summons_accepted
    
            "I understand. I'll be discreet and thorough.":
                mc "Consider it done, Quartermaster. I'll blend in, gather what I can find."
                s "(Nodding slowly) See that you do. Discretion is paramount. Report only to me, and only when we are well clear of the port."
                s "Get what you can about the 'Sea Serpent'. Crew disposition, last known heading, any unusual activity reported."
                jump scene_quarterdeck_summons_accepted
    
            "What makes you think I'm suited for this kind of work?":
                mc "Why me, Quartermaster? This sounds more like a job for one of the seasoned spies, not... well, me."
                s "Because the seasoned spies are known faces. You're not. You can fade into the background."
                s "And I've seen how you watch, how you listen when you think no one notices. Don't mistake my assigning duties for blindness."
                s "Now, are you up to the task or not?"
                mc "I won't let you down. I'll do it."
                s "See that you don't. The safety of this ship could depend on what you learn."
                jump scene_quarterdeck_summons_accepted
    
    
    label scene_quarterdeck_summons_accepted:
        "He gave a curt nod, the matter seemingly settled in his mind."
        s "We make port within the day. Prepare yourself. Get the necessary requisition forms from the purser – make it look official."
        s "Don't fail, [player_name]. The currents are turning strange."
    
        "He turned back to the sea, his stance rigid once more, leaving me alone with the wind and the weight of his orders."
        hide silas stern with easeoutright
        "A vanished patrol ship... This felt like the edge of something far larger, and far more dangerous, than simple piracy."
    
        stop sound fadeout 1.0
        # Consider adding a flag here: persistent.task_port_azure_intel = True
        # Jump to a scene preparing for port or back to ship navigation/hub
        # For now, just return
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
