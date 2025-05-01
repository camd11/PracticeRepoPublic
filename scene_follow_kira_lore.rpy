label scene_follow_kira_lore:

    # Scene Description: Rely on Kira's knowledge of lore and history to interpret the chart symbols more conventionally.

    ```renpy
    label scene_follow_kira_lore:
    
        scene bg study with fade
        show kira thoughtful at center with dissolve
        show mc neutral at left with dissolve
    
        "The strange chart lay spread across the table, its cryptic symbols seeming to mock our attempts at understanding."
        "Kira, however, leaned closer, her finger tracing one of the markings, her brow furrowed in concentration."
    
        mc "Anything making sense, Kira? It still looks like random scribbles to me."
    
        k "Not random. Not entirely."
        k "Look here."
    
        Kira pointed to a sequence of three symbols: a stylized mountain peak, a crescent moon, and a winding river.
    
        k "Individually, they're ambiguous. But together, in this order? They appear in several historical texts describing the Old Trade Routes."
        k "Specifically, routes used during the Age of Mists – known for being treacherous, but well-documented to avoid the worst hazards."
    
        mc "So you think this chart is based on those old routes?"
    
        k "It's the most logical interpretation based on established lore. The mountain symbol corresponds to the Dragon's Tooth pass, the moon likely represents the Silent Valley – traversable only at night according to some older tales – and the river... the Serpent's Coil tributary."
    
        She traced a path on the chart following these landmarks.
    
        k "If we follow this interpretation, the path leads west, around the Shadowfen rather than through it."
        k "It will be longer. Significantly longer, perhaps adding days to our journey."
    
        mc "But safer?"
    
        k "Based on the historical accounts, yes. The documented routes were established to bypass known dangers. Whoever drew this chart might have been relying on that same knowledge."
        k "It avoids the direct, potentially faster route implied by some of the other, less decipherable symbols."
    
        mc "Those other symbols... any idea what they could mean if we *don't* follow the trade route interpretation?"
    
        k "Speculation, mostly. Whispers in fragmented texts of 'shortcuts' or 'hidden paths' known only to a few."
        k "(Sighs lightly) Often, those whispers ended with the disappearance of whoever sought them."
        k "Sticking to the known, correlating these symbols with established history and cartography... it feels like the most prudent course of action."
    
        "Her reasoning was sound. Relying on documented history felt more secure than chasing cryptic hints that could lead anywhere... or nowhere."
        "It might mean missing a shortcut, or some hidden secret the chart hinted at, but caution seemed wiser."
    
        mc "Alright. It's slower, but 'prudent' sounds good right now."
        mc "Let's plot the course based on the Old Trade Route interpretation. West, around the Shadowfen."
    
        k "(Nodding, a hint of relief in her expression) Agreed. I'll mark the key points based on the texts."
        k "It requires careful navigation, but the landmarks should be clear if the historical accounts are accurate."
    
        "Kira focused back on the chart, her analytical mind already charting the safest known path forward."
        "The lure of the unknown symbols remained, a quiet question mark hanging in the air, but for now, logic and lore would guide their steps."
    
        # End scene, next scene will likely involve starting the journey on this path.
        # Example: jump scene_journey_west_start
    
        hide kira with dissolve
        hide mc with dissolve
        scene black with fade
    
        # Placeholder for next scene or returning to a map/hub
        return
    
    ```

    # TODO: Add choices or jump to the next scene
    return
