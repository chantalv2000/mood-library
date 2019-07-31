import random
def moodCalculator(mood, genre):
    if mood == 'happy' and genre == 'pop':
        recommendation = ["https://open.spotify.com/embed/track/5Hroj5K7vLpIG4FNCRIjbP",'https://open.spotify.com/embed/track/3QmolSZqjjLksTUvZJ6pPS','https://open.spotify.com/embed/track/5b88tNINg4Q4nrRbrCXUmg','https://open.spotify.com/embed/track/2dpaYNEQHiRxtZbfNsse99']
        return (random.choice(recommendation))
    elif mood == 'happy' and genre == 'rnb':
        recommendation = ["https://open.spotify.com/embed/track/5m77d1ztVTdZN9FevK9TE1",'https://open.spotify.com/embed/track/52FpkyImUt9LDI9mCWDryr','https://open.spotify.com/embed/track/3RU8VkqNLhv2mtwrVmnmrF','https://open.spotify.com/embed/track/6m59VvDUi0UQsB2eZ9wVbH','https://open.spotify.com/embed/track/6afg6nOJq4YLdLBY3RcUr6']
        return (random.choice(recommendation)) 
    elif mood == 'happy' and genre == 'rap':
        recommendation = ['https://open.spotify.com/embed/track/31I3Rt1bPa2LrE74DdNizO','https://open.spotify.com/embed/track/1WIZiOuNO3woKfdlSK2gNn','https://open.spotify.com/embed/track/6GnhWMhgJb7uyiiPEiEkDA','https://open.spotify.com/embed/track/7HytU9V8vMCUayply0lYBq','https://open.spotify.com/embed/track/2At3wa1XCMnEendDMO9qcM']
        return (random.choice(recommendation))
    elif mood == 'happy' and genre == 'country':
        recommendation = ['https://open.spotify.com/embed/track/4YKAOXyqkKZ5gOZR0AmVMN','https://open.spotify.com/embed/track/4u6eRWSXvzVZtRP6m48Psx','https://open.spotify.com//embed/track/5pvIz4hL9j5ei4q5Bk2WJW', 'https://open.spotify.com/embed/track/2U2Z1IXnmJIvlknWizFykZ', 'https://open.spotify.com/embed/track/5HGibWoxnkYSkl6mHmAlOE']
        return (random.choice(recommendation))  
    elif mood == 'happy' and genre == 'rock':
        recommendation = ['https://open.spotify.com/embed/track/05wIrZSwuaVWhcv5FfqeH0','https://open.spotify.com/embed/track/0wzRcekWyVCSyPtlPOeJau','https://open.spotify.com/embed/track/1j8z4TTjJ1YOdoFEDwJTQa', 'https://open.spotify.com/embed/track/7IznnRqG5qJihAFZFPOq5l', 'https://open.spotify.com/embed/track/2t6hKG0Zr3tfxBVQRfa9Zs']
        return (random.choice(recommendation))
    # elif mood == 'happy' and genre == 'classical':
    #     recommendation = ''
    #     return(recommendation)
        
    if mood == 'sad' and genre == 'pop':
        recommendation = ['https://open.spotify.com/embed/track/6b2RcmUt1g9N9mQ3CbjX2Y' , 'https://open.spotify.com/embed/track/0STK94RxUulYqWzwFlyAb5', 'https://open.spotify.com/embed/track/6L6ra9mTlyQPmh7zGw58y1' , 'https://open.spotify.com/embed/track/2M9ro2krNb7nr7HSprkEgo', 'https://open.spotify.com/embed/track/43zdsphuZLzwA9k4DJhU0I' ]
        return(random.choice(recommendation))    
    elif mood == 'sad' and genre == 'rnb':
        recommendation = ['https://open.spotify.com/embed/track/0JKjqJLo145b1mqA6MnhIl', 'https://open.spotify.com/embed/track/6N3qHjcwly8ZuhE4bPYJAX', 'https://open.spotify.com/embed/track/6Nle9hKrkL1wQpwNfEkxjh','https://open.spotify.com/embed/track/41zXlQxzTi6cGAjpOXyLYH', 'https://open.spotify.com/embed/track/7DKS0rX27cCEPsK0R6tFWS' ]
        return(random.choice(recommendation))
    elif mood == 'sad' and genre == 'rap':
        recommendation = ['https://open.spotify.com/embed/track/3UmaczJpikHgJFyBTAJVoz', 'https://open.spotify.com/embed/track/75ZvA4QfFiZvzhj2xkaWAh', 'https://open.spotify.com/embed/track/4AEzAEnbm9uRgbmTdeI63K', 'https://open.spotify.com/embed/track/6M0IsaUX4GNyto4niSegfI', 'https://open.spotify.com/embed/track/0HDdyhtep8nLbCbcjFNlcz']
        return(random.choice(recommendation))
    elif mood == 'sad' and genre == 'country':
        recommendation = ['https://open.spotify.com/embed/track/11EX5yhxr9Ihl3IN1asrfK', 'https://open.spotify.com/embed/track/7A5CReD6yWe0rrkJym34QI', 'https://open.spotify.com/embed/track/3pkzJjJXfdDjhpXx639MIH', 'https://open.spotify.com/embed/track/6wycnu8FWXsj68ig7BEot9', 'https://open.spotify.com/embed/track/1M2l9ReoabUnvl6Y8jLUe7']
        return(random.choice(recommendation))
    elif mood == 'sad' and genre == 'rock':
        recommendation = ['https://open.spotify.com/embed/track/1FMHNVeJ9s1x1l1WlaRs2I', 'https://open.spotify.com/embed/track/6vrUTGn5p8IrfTZ0J6sIVM', 'https://open.spotify.com/embed/track/3ZffCQKLFLUvYM59XKLbVm']
        return(random.choice(recommendation))
    # elif mood == 'sad' and genre == 'classical':
    #     recommendation = ''
    #     return(random.choice(recommendation))
    
    if mood == 'mad' and genre == 'pop':
        recommendation = 'https://open.spotify.com/embed/track/5xEM5hIgJ1jjgcEBfpkt2F'
        return(random.choice(recommendation))
    elif mood == 'mad' and genre == 'rnb':
        recommendation = 'https://open.spotify.com/embed/track/6Hn9Uc1mMNfqChXU3txNke'
        return(random.choice(recommendation)) 
    elif mood == 'mad' and genre == 'rap':
        recommendation = 'https://open.spotify.com/embed/track/5eGEc27nnhtmcOh6RC890a' 
        return(recommendation)
    elif mood == 'mad' and genre == 'country':
        recommendation = 'https://open.spotify.com/embed/track/2yhhcHTfvLC0HzSajGYL0h'
        return(recommendation)      
    elif mood == 'mad' and genre == 'rock':
        recommendation = 'https://open.spotify.com/embed/track/0M955bMOoilikPXwKLYpoi'
        return(recommendation)
    # elif mood == 'mad' and genre == 'classical':
    #     recommendation = ''
    #     return(recommendation)  
    
    # if mood == 'stressed' and genre == 'pop':
    #     recommendation = 'stressed out artist by twenty one pilots'
    #     return(recommendation)      
    # elif mood == 'stressed' and genre == 'rnb':
    #     recommendation = ''
    #     return(recommendation)  
    # elif mood == 'stressed' and genre == 'rap':
    #     recommendation = ''
    #     return(recommendation)    
    # elif mood == 'stressed' and genre == 'country':
    #     recommendation = ''
    #     return(recommendation)
    # elif mood == 'stressed' and genre == 'rock':
    #     recommendation = ''
    #     return(recommendation)
    # elif mood == 'stressed' and genre == 'Classical':
    #     recommendation = ''
    #     return(recommendation)
    

    # if mood == 'in love' and genre == 'pop':
    #     recommendation = ''
    #     return(recommendation)      
    # elif mood == 'in love' and genre == 'rnb':
    #     recommendation = ''
    #     return(recommendation)  
    # elif mood == 'in love' and genre == 'rap':
    #     recommendation = ''
    #     return(recommendation)    
    # elif mood == 'in love' and genre == 'country':
    #     recommendation = ''
    #     return(recommendation)
    # elif mood == 'in love' and genre == 'rock':
    #     recommendation = ''
    #     return(recommendation)
    # elif mood == 'in love' and genre == 'Classical':
    #     recommendation = ''
    #     return(recommendation)
    
    

    elif mood == 'in love':
        return('Fill out the ENTIRE form!')
    elif mood =="stressed":
         return('Fill out the ENTIRE form!')
    elif mood == 'happy': 
         return('Fill out the ENTIRE form!')
    elif mood == 'mad':
         return('Fill out the ENTIRE form!')
    elif mood == 'sad':
         return('Fill out the ENTIRE form!')
    elif genre == 'classical':
         return('Fill out the ENTIRE form!')
    elif genre == 'rock':
         return('Fill out the ENTIRE form!')
    elif genre == 'pop':
         return('Fill out the ENTIRE form!')
    elif genre == 'rap':
         return('Fill out the ENTIRE form!')
    elif genre == 'rnb':
         return('Fill out the ENTIRE form!')
