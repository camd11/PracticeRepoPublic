label scene_captains_cabin:

    # Scene Description: Slip away to investigate the Captain's Cabin, searching for unsanctioned clues like charts or personal logs.

    ```renpy
    label scene_captains_cabin:
    
        scene bg captains_cabin with dissolve
        play sound "sfx/door_creak_slow.ogg"
        "The lock clicks softly, succumbing to the makeshift pick. The heavy cabin door creaks open just enough to slip through."
        "Inside, the air is thick with dust and the scent of old wood, brine, and something metallic, almost like dried blood."
        "Moonlight streams through the stern windows, illuminating dust motes dancing in the air."
        "This cabin feels frozen in time, a stark contrast to the bustling energy of the deck."
        "Charts lie rolled and scattered across a large oak desk. Strange, unfamiliar artifacts rest on shelves alongside sextants and compasses."
        "The risk is palpable. Getting caught here means more than just trouble; it could mean the brig... or worse."
        "But the need to understand... the ship, its captain, maybe even myself... outweighs the fear."
        "Where should I start looking?"
    
        menu:
            "Examine the Charts on the Desk":
                "I approach the desk, carefully avoiding a creaky floorboard."
                "The charts are old, brittle to the touch. Most depict familiar shipping lanes, marked with grease pencil."
                "But one chart, tucked beneath the others, is different. It shows a constellation of islands I don't recognize, sketched in faded ink."
                "A single island is circled crudely, with a strange symbol beside it – a serpent coiled around a broken anchor."
                play sound "sfx/paper_rustle.ogg"
                "This feels... important. Significant. Like a half-remembered dream."
                "Is this the ship's true destination? Or a secret from the Captain's past?"
                "Suddenly, footsteps echo on the deck outside the cabin door."
                play sound "sfx/footsteps_wood_nearby.ogg"
                "Heart pounding, I quickly slide the strange chart back under the others, hoping I remember its details."
                "I flatten myself against the bulkhead, hidden in the deepest shadows near the window."
                pause 3.0
                "The footsteps fade down the passageway. Whoever it was, they moved on."
                "Too close. I need to find something more concrete, or get out."
    
            "Search for a Personal Log":
                "My eyes scan the shelves and the desk, looking for a journal, a logbook – anything personal."
                "Tucked away on a shelf behind a dusty spyglass, I spot it: a leather-bound book, its cover worn smooth."
                play sound "sfx/item_pickup.ogg"
                "It's locked with a small, tarnished brass clasp."
                "Frustrating. Whatever secrets it holds are sealed away."
                "But as I turn it over, a small, dried flower falls out from between the pages. A Sea Lavender, strangely preserved."
                "It feels oddly familiar, triggering a flicker of... something. A memory just out of reach, like salt spray on the wind."
                "Why would the Captain keep this?"
                "A sharp creak from the hallway outside snaps me back to reality."
                play sound "sfx/wood_creak_sharp.ogg"
                "Instinct takes over. I shove the logbook back onto the shelf, my fingers brushing against the cold glass of the spyglass."
                "I duck behind the large captain's chair, holding my breath."
                pause 3.0
                "Silence returns, heavy and expectant. False alarm? Or did they hear me?"
                "This is too dangerous. But that flower... it meant something."
    
            "Inspect the Strange Artifacts":
                "My attention is drawn to the artifacts lining the shelves. They look out of place on a pirate vessel."
                "There's a carved wooden mask with hollow eyes, a piece of coral sculpted into an impossible shape, and a small, obsidian shard humming with a faint energy."
                play sound "sfx/subtle_hum.ogg"
                "I reach out, hesitating, then brush my fingers against the obsidian shard."
                "A jolt, like static electricity but colder, deeper, races up my arm."
                "Images flash behind my eyes – stormy seas, a flash of green light, a face obscured by shadow, whispering a name I almost recognize..."
                "[persistent.player_name]..."
                "The vision fades as quickly as it came, leaving me breathless and disoriented."
                "What was that? Was that... me? A memory?"
                "The shard feels inert now, just a cold piece of rock."
                "Suddenly, the distinct sound of a key turning in a lock rattles the far door to the Captain's private quarters within the cabin."
                play sound "sfx/key_turn_lock.ogg"
                "Panic surges. Someone's *in* the adjacent room!"
                "No time to think. I dart back towards the main cabin door, pulling it open silently."
    
        # Common pathway after initial investigation choice or if interrupted
        "My heart hammers against my ribs. I can't stay here any longer."
        "Whether it was the chart, the flower, or the shard, I found... something."
        "A fragment. An echo of a past hidden beneath the waves of the present."
        "Clutching the fragment of information – or perhaps just the memory of it – I slip back out into the dimly lit passageway."
        play sound "sfx/door_close_soft.ogg"
        "The lock clicks shut behind me, leaving the Captain's secrets undisturbed, for now."
        "But the questions linger, deeper and more turbulent than before."
    
        jump scene_return_from_cabin
    ```

    # TODO: Add choices or jump to the next scene
    return
