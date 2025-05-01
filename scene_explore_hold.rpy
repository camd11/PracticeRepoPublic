label scene_explore_hold:

    # Scene Description: Descend into the damp, shadowy hold of the galleon, searching for answers or supplies.

    ```renpy
    label scene_explore_hold:
    
        scene bg ship_hold with dissolve
        # Assuming no specific character sprite is visible initially, focusing on atmosphere.
    
        "The air grows heavy and thick as I descend the rickety stairs into the galleon's hold."
        "Each step groans under my weight, echoing unnervingly in the cavernous space below."
        "The smell hits me first – stale water, mildew, rotting wood, and something else… something metallic and faintly unpleasant."
        "Lantern light pushes back the oppressive darkness only slightly, revealing towering stacks of crates and rows of barrels, their shapes distorted by shadow."
        "Water drips steadily somewhere nearby, a constant, maddening rhythm against the deeper creaks and groans of the ship's timbers."
        "Every shadow seems deeper than it should be, potentially hiding anything."
        "My objective is clear: find something, *anything*, that explains what happened here, or what supplies remain."
    
        # Player explores
        "My boots squelch slightly on the damp planks. The lantern beam dances across surfaces slick with moisture."
        "The silence between the ship's noises feels heavy, watchful."
    
        menu:
            "Examine the crates near the port side.":
                "I move towards the nearest stack of crates, piled high and lashed together, though some ropes look frayed."
                "Most are marked with faded shipping manifests, detailing mundane cargo – textiles, dried fish, iron tools."
                "One crate, however, jammed awkwardly near the bottom, bears a different mark."
                "It's a crudely scratched symbol, not belonging to any merchant house I recognize. A spiral converging on a single, sharp point."
                "I try to shift it, but it's wedged tight. Whatever's inside remains a mystery for now, but the symbol itself is unsettling."
                "A sudden skittering sound echoes from deeper within the crate stack. Rats, hopefully."
                $ hold_clue_found = "Strange Symbol"
    
            "Investigate the barrels along the aft bulkhead.":
                "I make my way towards the rear of the hold, where barrels stand in uneven rows."
                "Many seem to be water barrels, judging by the damp rings around their bases, but others are sealed tight."
                "I tap on a few. Some sound reassuringly full, others worryingly empty."
                "One barrel, half-hidden behind others, feels sticky to the touch."
                "Holding the lantern closer, I see a dark, viscous substance has leaked from a crack in the wood. It smells acrid, unnatural."
                "It's definitely not bilge water or rum. What were they transporting?"
                "A low groan emanates from the bulkhead itself, as if the ship is complaining under immense strain."
                $ hold_clue_found = "Strange Substance"
    
            "Check the dark, cluttered corner near the bow.":
                "My attention is drawn to the forward-most corner, a place the lantern light struggles to penetrate fully."
                "It seems to be a dumping ground for discarded items – frayed nets, broken planks, scraps of sailcloth."
                "I carefully step over the debris, lantern held high."
                "Partially buried beneath a pile of damp canvas, I spot something."
                "It's a small, leather-bound book. A journal or logbook? It's heavily water-damaged, the cover warped and stained."
                "I pry it open carefully. Most pages are fused together or the ink has run into illegible blurs."
                "One page, however, near the back, has a few mostly readable lines..."
                "\"...sea claims its due... sacrifice... below... whispers... driving them mad... must seal...\""
                "The rest dissolves into watery marks. Seal what? Who was being driven mad?"
                "A cold draft snakes its way from the very planks beneath my feet, raising goosebumps."
                $ hold_clue_found = "Damaged Logbook"
    
        # After the choice
        "The air feels colder now, the shadows longer."
        "A loud CRACK echoes from somewhere above, followed by the strained screech of timber."
        "Is the ship settling, or is something else happening?"
        "I've found something, at least. A piece of the puzzle, however small and disturbing."
        "Staying down here much longer feels unwise. The hold seems to be watching, waiting."
        "Time to return to the relative safety of the upper decks."
    
        # Scene ends, potentially jump to another label like 'return_from_hold'
        # jump return_from_hold
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
