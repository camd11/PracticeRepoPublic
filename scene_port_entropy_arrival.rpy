label scene_port_entropy_arrival:

    # Scene Description: The Ghost Ship docks at the chaotic, dimly lit Port Entropy, a haven for pirates and smugglers.

    ```renpy
    label scene_port_entropy_arrival:
    
        scene bg port_entropy with dissolve
        play music "audio/music/port_entropy_theme.ogg" # Assuming a suitable track exists
    
        "The Ghost Ship slid into a mooring berth like a phantom weaving through fog, its spectral timbers barely creaking amidst the cacophony of Port Entropy."
        "Lanterns cast long, dancing shadows across rickety wooden docks slick with sea spray and spilled grog. The air hung thick with the smell of brine, cheap rum, tar, and something vaguely metallic, like old blood."
        "Shouts, drunken laughter, and arguments in a dozen tongues echoed between leaning shanties and warehouses built from salvaged wrecks."
    
        show silas cautious at left with easeinleft
        show kira wary at right with easeinright
    
        silas "Port Entropy. Aptly named. Keep your wits sharp and your coin purse hidden, Jax."
        kira "The energy here... it's frantic. Like a thousand desperate stories shouting over each other."
        kira "Old charts sometimes mark this place as 'The Last Anchorage,' a place where maps ended and mysteries began."
    
        jax "(Internal) Mysteries and trouble. Feels like both are waiting for us here."
        "I scanned the crowded docks. Faces here were hard, etched with desperation or cold calculation. Deals were being struck in shadowed alcoves, heavy sacks exchanged hands quickly, and watchful eyes tracked every newcomer."
    
        silas "We need supplies, and more importantly, information. Word travels fast in a cesspit like this, but it costs."
        silas "Brokers operate out of the taverns and back alleys. They trade in secrets, rumours... fragments. Just like the ones we seek."
        kira "But tread carefully. Information here can be a lure, a trap woven from half-truths."
    
        "My gaze snagged on a figure half-hidden in the gloom near the gangplank of a newly arrived, black-sailed brigantine further down the quay."
        "Long, dark coat, a glint of steel at the hip... something about the stance seemed familiar."
        "Could it be... Elena? Stormblade?"
        "The figure turned their head slightly, obscured by shadow and distance. The moment stretched, then they melted back into the throng."
    
        jax "(Internal) Was that her? Or is this place just making me see ghosts?"
        silas "Jax? Eyes forward. Getting spooked already won't help."
        kira "He's right. This port preys on uncertainty."
    
        silas "We need actionable intelligence. The fragmented log mentioned a 'Whispering Market' here - likely where brokers congregate. But charging straight in might attract the wrong kind of attention."
        kira "We could also try to blend in first, gather ambient chatter in a place like the 'Drowned Rat' tavern. Less direct, potentially safer."
    
        menu:
            "Seek out an information broker directly.":
                silas "Bold. Very well. Stay alert. We head towards the 'Whispering Market'."
                jax "\"Let's get straight to it. Time might be against us.\""
                "Silas nodded curtly, his hand resting near his sidearm."
                jump scene_port_entropy_market_approach # Assumes next label
    
            "Try the 'Drowned Rat' tavern first, observe.":
                kira "A prudent approach. Sometimes the quietest whispers hold the most truth."
                jax "\"Let's ease our way in. Get the lay of the land at the tavern first.\""
                silas "Fine. But don't mistake cheap ale for reliable sources. Keep your ears open and your mouth shut."
                jump scene_port_entropy_tavern_entry # Assumes next label
    
            "Keep a low profile, secure the ship first.":
                silas "Pragmatic. Our vessel is... conspicuous. Ensuring it's secure while we gather supplies makes sense."
                jax "\"Let's make sure the ship is safe and gather basic supplies before sticking our necks out.\""
                kira "Understood. Security first."
                "We turned back towards the Ghost Ship, the chaotic energy of Port Entropy pressing in from all sides."
                jump scene_port_entropy_secure_ship # Assumes next label
    
        # Fallback or common exit point if jumps aren't defined yet
        "The air crackled with unseen threats and veiled promises. Port Entropy welcomed us with a dangerous embrace."
        # End of scene, awaiting next jump or fade out
    
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
