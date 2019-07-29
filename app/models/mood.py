def moodCalculator(mood, genre):
    if mood == 'happy' and genre == 'pop':
        recommendation = 'Best Day Of My Life by American Authors'
        return(recommendation)
    elif mood == 'happy' and genre == 'rnb':
        recommendation = 'I Want You by Marian Hill'
        return(recommendation) 
    elif mood == 'happy' and genre == 'rap':
        recommendation = 'Flashing lights by Kanye West'
        return(recommendation)
    elif mood == 'happy' and genre == 'country':
        recommendation = 'Red Solo Cup by Toby Kieth'
        return(recommendation)  
    elif mood == 'happy' and genre == 'rock':
        recommendation = 'Walking on sunshine by katrina and the waves'
        return(recommendation)
        
    if mood == 'sad' and genre == 'pop':
        recommendation = 'How Do You Sleep? by Sam Smith'
        return(recommendation)    
    elif mood == 'sad' and genre == 'rnb':
        recommendation = 'Do You by Ne-Yo'
        return(recommendation) 
    elif mood == 'sad' and genre == 'rap':
        recommendation = 'Stan by Eminem'
        return(recommendation)
    elif mood == 'sad' and genre == 'country':
        recommendation = 'Need you now by Lady Antebellum'
        return(recommendation)
    elif mood == 'sad' and genre == 'rock':
        recommendation = 'it ends tonight by all american rejects'
        return(recommendation)
    
    if mood == 'mad' and genre == 'pop':
        recommendation = 'Complicated by Avril Lavigne'
        return(recommendation) 
    elif mood == 'mad' and genre == 'rnb':
        recommendation = 'Mad by Ne-Yo'
        return(recommendation) 
    elif mood == 'mad' and genre == 'rap':
        recommendation = 'Kill You Criminal by Eminem'
        return(recommendation)
    elif mood == 'mad' and genre == 'country':
        recommendation = 'Kerosene by Miranda Lambert'
        return(recommendation)      
    elif mood == 'mad' and genre == 'rock':
        recommendation = 'I Hate Everything About You by Three Days Grace'
        return(recommendation)      
            

