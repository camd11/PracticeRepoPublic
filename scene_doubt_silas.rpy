label scene_doubt_silas:

    # Scene Description: Politely decline or question Silas's task, raising suspicion but maintaining autonomy.

    ```renpy
    label scene_doubt_silas:
    
        scene bg silas_office
        show silas expectant at center
    
        mc "Silas... about the task you asked me to undertake."
        mc "I've been thinking it over, and I must admit, I have some reservations."
    
        s "Reservations?"
        s "(Frowning slightly) I explained the necessity quite clearly, I thought. What seems to be the issue?"
        show silas neutral at center
    
        mc "It's not the goal itself, necessarily. But the method you've proposed... it feels indirect. Perhaps even unnecessarily convoluted."
        mc "Are you certain this is the most straightforward way? Or perhaps... the only way you're willing to share?"
    
        show silas annoyed at center
        s "Are you questioning my judgment? I have my reasons for outlining the procedure as I did."
        s "Reasons I don't feel obliged to share in exhaustive detail. I require discretion and execution, not interrogation."
    
        mc "(Meeting his gaze firmly) With respect, Silas, I'm not comfortable acting on incomplete information, especially when something feels... off."
        mc "Blind trust isn't my strength. If I'm to proceed, I need a clearer understanding of why this specific path is crucial."
    
        s "(Scoffs softly) Clarity. Everyone wants clarity, but few appreciate the complexities involved."
        s "If you lack the conviction to follow instructions based on my experience and position, then perhaps you aren't suited for this particular endeavor after all."
        show silas stern at center
    
        mc "Perhaps not, if it requires abandoning my own judgment entirely."
        mc "I understand your position, but I can't proceed as instructed under these circumstances."
        mc "I'll have to find another way to address the situation, one that aligns better with... my own approach."
    
        s "Find another way?"
        s "(His voice drops, cold and dismissive) Do as you please. But don't expect my resources or assistance if you choose to disregard my counsel."
        s "You are charting your own course now. See where it leads you."
    
        mc "I intend to."
        mc "(Turning away) Thank you for your time, Silas."
    
        "Silas watches me go, his expression unreadable but radiating disapproval."
        "The air feels heavy with unspoken tension. His door closes softly behind me, but the feeling of friction remains."
        "He won't help further down that path. It's clear I need to find my own information, my own allies, my own solution."
    
        hide silas
    
        # Scene ends, player must now seek alternative paths.
    
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
