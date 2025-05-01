label scene_rival_encounter:

    # Scene Description: A tense encounter with Rival Captain 'Stormblade' Elena, who believes you hold something of hers.

    ```renpy
    label scene_rival_encounter:
    
        scene bg misty_docks with dissolve
        # Assuming 'misty_docks' is a defined background image
        # Add a fog overlay if available
        # show screen fog_overlay
    
        "A heavy fog rolled in off the water, blanketing the docks in an eerie silence. The usual bustle of the port was muffled, shapes indistinct in the grey."
        "The air felt thick, charged with an unseen tension."
    
        show kai concerned at left with moveinleft
        pause 0.5
    
        kai "Something feels off, Captain. This fog... it's unnatural."
        mc "Stay sharp, Kai. Ports like these breed trouble, especially when visibility is low."
    
        "Suddenly, a figure materialized from the swirling mist ahead, solidifying into a sharp, imposing silhouette."
        "Tall, clad in dark, practical seafaring gear, with a hand resting ominously on the hilt of the cutlass at her hip."
    
        show elena angry at right with moveinright
        # Assuming 'elena angry' is a defined sprite for Elena
    
        elena "(Voice sharp as broken glass) Well, well. Look what the tide dragged in. Fancy meeting you here, Captain."
    
        kai "(Stepping slightly forward) State your business. We mean no trouble."
        elena "(Ignoring Kai, eyes fixed on MC) Trouble finds those who carry stolen goods. Isn't that right?"
    
        mc "Elena 'Stormblade'. Still chasing shadows, I see."
        elena "(A humorless smirk) The only shadow I'm chasing is the one you cast when you ran off with what's rightfully mine."
    
        kai "Captain? What is she talking about?"
        mc "(To Kai) An old rival. Seems her memory is as foggy as this dock."
    
        elena "(Eyes narrow, hand tightening on her sword hilt) My memory is perfectly clear. The Azure Shard expedition. The chaos. The map fragment you took from Captain Vorlag's cabin after... after the incident."
        elena "That fragment belongs to *me*. It was my father's legacy!"
    
        "Her voice was low, trembling slightly with controlled fury. The air crackled between you."
        "Kai shifted his weight, ready for a fight, his gaze flicking between you and the dangerous rival captain."
    
        mc "Vorlag's fragment? Elena, your father gave that piece to me himself, just before the cave-in. He said..."
    
        elena "(Cutting off) Lies! You took advantage of the chaos! Scurried away while others fought for their lives!"
        elena "I won't let you profit from that tragedy. Hand it over. Now."
    
        menu:
            "\"I don't have what you're looking for, Elena.\"":
                mc "I don't have it. Whatever fragment Vorlag had, it was lost in the collapse, along with him."
                elena "(Scoffs) Convenient. You always were a coward and a liar."
                show elena furious at right
                elena "Fine. If you won't return it willingly, I'll pry it from your ship piece by piece if I have to!"
                elena "This isn't over. Not by a long shot."
                "She glared, radiating menace, before turning sharply and melting back into the fog as quickly as she appeared."
                hide elena with moveoutright
                kai "Captain... Do you really not have it?"
                mc "It's... complicated, Kai. Let's get back to the ship. Quickly."
    
            "\"Your memory is flawed. Vorlag trusted *me*.\"":
                mc "Your grief clouds your judgment, Elena. Vorlag gave me the fragment for safekeeping. He knew *you* weren't ready."
                show elena furious at right
                elena "(Voice rising) How dare you! You twist his memory to suit your greed!"
                elena "Ready? I was his daughter! That map is my birthright!"
                "Her hand flashed to her cutlass, drawing it with a menacing scrape of steel."
                play sound "sfx/sword_unsheath_metal.ogg" # Example sound path
                show elena drawn_weapon at right # Assuming a sprite variant
                elena "Give it back, or prepare to join my father in the depths!"
                kai "(Drawing his own blade) Back off, Stormblade! You won't threaten my Captain!"
                # This could lead into a combat sequence or a tense standoff scene next.
                "The confrontation hung heavy in the mist, the gleam of drawn steel sharp against the grey."
    
            "\"Maybe we can discuss this somewhere more private?\"":
                mc "This isn't the time or place, Elena. Too many ears, too much fog."
                mc "If you truly believe I have something of yours, let's find a neutral spot. Talk this through."
                show elena skeptical at right
                elena "(Eyes narrow, assessing) Trying to lure me into a trap? Your usual tactics."
                elena "..."
                elena "Fine. The Drunken Kraken tavern, back room. One hour. Come alone."
                mc "Just me and you. No tricks."
                elena "If you're not there, or if I smell a rat... I'll assume you've made your choice. And I'll make mine."
                "She held your gaze for a moment longer, then vanished back into the fog."
                hide elena with moveoutright
                kai "Captain, is that wise? Meeting her alone?"
                mc "It's a risk. But maybe... maybe we can resolve this without more bloodshed."
    
        # Scene continuation based on choice, or jump to another label.
        # For now, ending the scene here after the choice interaction.
        "The encounter left a chill in the air colder than the fog itself."
        "Elena's threat, or her offer, hung heavy as you considered your next move."
    
        return # End the scene
    ```

    # TODO: Add choices or jump to the next scene
    return
