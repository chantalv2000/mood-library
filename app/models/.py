import random
def moodCalculator(mood, genre):
    if mood == 'happy' and genre == 'pop':
        recommendation = ["https://open.spotify.com/embed/track/5Hroj5K7vLpIG4FNCRIjbP",'https://open.spotify.com/embed/track/3QmolSZqjjLksTUvZJ6pPS','https://open.spotify.com/embed/track/5b88tNINg4Q4nrRbrCXUmg','https://open.spotify.com/embed/track/2dpaYNEQHiRxtZbfNsse99']
        return (random.choice(recommendation))
    elif mood == 'happy' and genre == 'r&b':
        recommendation = ["https://open.spotify.com/embed/track/5m77d1ztVTdZN9FevK9TE1",'https://open.spotify.com/embed/track/52FpkyImUt9LDI9mCWDryr','https://open.spotify.com/embed/track/3RU8VkqNLhv2mtwrVmnmrF','https://open.spotify.com/embed/track/6m59VvDUi0UQsB2eZ9wVbH','https://open.spotify.com/embed/track/6afg6nOJq4YLdLBY3RcUr6']
        return (random.choice(recommendation)) 
    elif mood == 'happy' and genre == 'rap':
        recommendation = ['https://open.spotify.com/embed/track/31I3Rt1bPa2LrE74DdNizO','https://open.spotify.com/embed/track/1WIZiOuNO3woKfdlSK2gNn','https://open.spotify.com/embed/track/6GnhWMhgJb7uyiiPEiEkDA','https://open.spotify.com/embed/track/7HytU9V8vMCUayply0lYBq','https://open.spotify.com/embed/track/2At3wa1XCMnEendDMO9qcM']
        return (random.choice(recommendation))
    elif mood == 'happy' and genre == 'country':
        recommendation = ['https://open.spotify.com/embed/track/4YKAOXyqkKZ5gOZR0AmVMN','https://open.spotify.com/embed/track/4u6eRWSXvzVZtRP6m48Psx','https://open.spotify.com/embed/track/2BgunkkepMPFpArQj1Dx5s', 'https://open.spotify.com/embed/track/2U2Z1IXnmJIvlknWizFykZ', 'https://open.spotify.com/embed/track/5HGibWoxnkYSkl6mHmAlOE']
        return (random.choice(recommendation))  
    elif mood == 'happy' and genre == 'rock':
        recommendation = ['https://open.spotify.com/embed/track/05wIrZSwuaVWhcv5FfqeH0','https://open.spotify.com/embed/track/0wzRcekWyVCSyPtlPOeJau','https://open.spotify.com/embed/track/1j8z4TTjJ1YOdoFEDwJTQa', 'https://open.spotify.com/embed/track/7IznnRqG5qJihAFZFPOq5l', 'https://open.spotify.com/embed/track/2t6hKG0Zr3tfxBVQRfa9Zs']
        return (random.choice(recommendation))
        
    if mood == 'sad' and genre == 'pop':
        recommendation = ['https://open.spotify.com/embed/track/6b2RcmUt1g9N9mQ3CbjX2Y' , 'https://open.spotify.com/embed/track/0STK94RxUulYqWzwFlyAb5', 'https://open.spotify.com/embed/track/6L6ra9mTlyQPmh7zGw58y1' , 'https://open.spotify.com/embed/track/2M9ro2krNb7nr7HSprkEgo', 'https://open.spotify.com/embed/track/43zdsphuZLzwA9k4DJhU0I' ]
        return(random.choice(recommendation))    
    elif mood == 'sad' and genre == 'r&b':
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

    if mood == 'mad' and genre == 'pop':
        recommendation = ['https://open.spotify.com/embed/track/5xEM5hIgJ1jjgcEBfpkt2F', 'https://open.spotify.com/embed/track/2lbbPNyawVMyyOlTMu4tn2', 'https://open.spotify.com/embed/track/7bprRkhvOXWmWpqOrEWbXu', 'https://open.spotify.com/embed/track/5HbCnVLXRyZVxnreOPgJCK', 'https://open.spotify.com/embed/track/5ecZWU5uQOiCVSnPxBZNmT', 'https://open.spotify.com/embed/track/6WAhLCL1XchQzYjl15rnFp']
        return(random.choice(recommendation))
    elif mood == 'mad' and genre == 'r&b':
        recommendation = ['https://open.spotify.com/embed/track/6Hn9Uc1mMNfqChXU3txNke', 'https://open.spotify.com/embed/track/5pUzxJo6UqY57Xl5AvU7tQ', 'https://open.spotify.com/embed/track/0YGQ3hZcRLC5YX7o0hdmHg', 'https://open.spotify.com/embed/track/5Zu4UO0QlderRYNPFkbJeO', 'https://open.spotify.com/embed/track/5fucng5fXRhyItyV9x7UPf']
        return(random.choice(recommendation)) 
    elif mood == 'mad' and genre == 'rap':
        recommendation = 'https://open.spotify.com/embed/track/5eGEc27nnhtmcOh6RC890a' 
        return(random.choice(recommendation))
    elif mood == 'mad' and genre == 'country':
        recommendation = ['https://open.spotify.com/embed/track/2yhhcHTfvLC0HzSajGYL0h', 'https://open.spotify.com/embed/track/1CyanrHZ0R07Yp8Nwq92F6', 'https://open.spotify.com/embed/track/7quBChnqXvS81TuiKr1EMW',] 
        return(random.choice(recommendation))      
    elif mood == 'mad' and genre == 'rock':
        recommendation = ['https://open.spotify.com/embed/track/0M955bMOoilikPXwKLYpoi', 'https://open.spotify.com/embed/track/0rmGAIH9LNJewFw7nKzZnc', 'https://open.spotify.com/embed/track/0v1XpBHnsbkCn7iJ9Ucr1l','https://open.spotify.com/embed/track/1aWGyuU1gNPAarCFwh6jec','https://open.spotify.com/embed/track/0oerlffJSzhRVvtDfLcp3N']
        return(random.choice(recommendation))
    # elif mood == 'mad' and genre == 'classical':
    #     recommendation = ['https://open.spotify.com/embed/track/2YarjDYjBJuH63dUIh9OWv', 'https://open.spotify.com/embed/track/1LrLejjPKSb5cAf9D7P85q', 'https://open.spotify.com/embed/track/4RnwnOki6FOcVT7zxBtbWj', 'https://open.spotify.com/embed/track/0ho24dNWwAS3Myat3N2V0C']
    #     return(random.choice(recommendation)) 
    
    if mood == 'stressed' and genre == 'pop':
        recommendation = ['https://open.spotify.com/embed/track/3CRDbSIZ4r5MsZ0YwxuEkn', 'https://open.spotify.com/embed/track/62bOmKYxYg7dhrC6gH9vFn', 'https://open.spotify.com/embed/track/3RgR3cFZ6xh7MlB9DURK6e','https://open.spotify.com/embed/track/5xTtaWoae3wi06K5WfVUUH', 'https://open.spotify.com/embed/track/7vS3Y0IKjde7Xg85LWIEdP']
        return(random.choice(recommendation))
    elif mood == 'stressed' and genre == 'r&b':
        recommendation = ['https://open.spotify.com/embed/track/6EFAyx72zPx5mnSuyLW1U2', '', 'https://open.spotify.com/embed/track/1m8WpLYXEiNVZchsWEcCSy', 'https://open.spotify.com/embed/track/2FyWsAo1BTiHrxCUI2w8yI']
        return(random.choice(recommendation))  
    elif mood == 'stressed' and genre == 'rap':
        recommendation = ['https://open.spotify.com/embed/track/5hZ0tNZfusgngcfrW3XtFD', 'https://open.spotify.com/embed/track/4YH7AZpdCXEAGOsSAZYPOq','https://open.spotify.com/embed/track/00t7QTffOR3SA3L1BvSQVq', 'https://open.spotify.com/embed/track/740gNyGWKk98gy8nJLhHrv']
        return(random.choice(recommendation))    
    elif mood == 'stressed' and genre == 'country':
        recommendation = ['https://open.spotify.com/embed/track/71geaRAZ2M5w08T3kl5Xvs', 'https://open.spotify.com/embed/track/3i5QyEUyXa9Y7lIklr5sWk','https://open.spotify.com/embed/track/1PoGWZbJPGmViVi7CYbDUK', 'https://open.spotify.com/embed/track/3S4ruu2F7dMeRY7FV0ayTb']
        return(random.choice(recommendation))
    elif mood == 'stressed' and genre == 'rock':
        recommendation = ['https://open.spotify.com/embed/track/4Bxl1qty34HSOKZrRjyj0s', 'https://open.spotify.com/embed/track/3asFGFY3uLjMDmML1p0tYm', 'https://open.spotify.com/embed/track/2DLWz8SAA2XlrN2mEo4fac', 'https://open.spotify.com/embed/track/3mcG2NI5G5vhrQtRda1YnA', 'https://open.spotify.com/embed/track/79meQHFglEqxQ3YRAO1QrW']
        return(random.choice(recommendation))
    # elif mood == 'stressed' and genre == 'Classical':
    #     recommendation = ''
    #     return(recommendation)
    

    if mood == 'in love' and genre == 'pop':
        recommendation = ['https://open.spotify.com/embed/track/6LsAAHotRLMOHfCsSfYCsz','https://open.spotify.com/embed/track/3HVWdVOQ0ZA45FuZGSfvns', 'https://open.spotify.com/embed/track/7kSLdGdXLey7pzLsWpdg1h', 'https://open.spotify.com/embed/track/2RttW7RAu5nOAfq6YFvApB', 'https://open.spotify.com/embed/track/7COXchtUOMd6uIT6HvmRaI']
        return(random.choice(recommendation))      
    elif mood == 'in love' and genre == 'r&b':
        recommendation = ['https://open.spotify.com/embed/track/3LmvfNUQtglbTrydsdIqFU', 'https://open.spotify.com/embed/track/0JEqGkvUiMTQmFY6sgL9kg', 'https://open.spotify.com/embed/track/3ibKnFDaa3GhpPGlOUj7ff', 'https://open.spotify.com/embed/track/7Lf7oSEVdzZqTA0kEDSlS5', 'https://open.spotify.com/embed/track/0PG9fbaaHFHfre2gUVo7AN']
        return(random.choice(recommendation))  
    elif mood == 'in love' and genre == 'rap':
        recommendation = ['https://open.spotify.com/embed/track/6PGoSes0D9eUDeeAafB2As', 'https://open.spotify.com/embed/track/2lpygKqzPFtItQ4ss3cgfb', 'https://open.spotify.com/embed/track/46CA1H0T1r7u5lDUtVveAh', 'https://open.spotify.com/embed/track/43PuMrRfbyyuz4QpZ3oAwN', 'https://open.spotify.com/embed/track/5mCPDVBb16L4XQwDdbRUpz']
        return(random.choice(recommendation))    
    elif mood == 'in love' and genre == 'country':
        recommendation = ['https://open.spotify.com/embed/track/5F5lmpwXkxAJtvZqEguTRo','https://open.spotify.com/embed/track/2SpEHTbUuebeLkgs9QB7Ue','https://open.spotify.com/embed/track/3GCL1PydwsLodcpv0Ll1ch', 'https://open.spotify.com/embed/track/0b9djfiuDIMw1zKH6gV74g','https://open.spotify.com/embed/track/2rxQMGVafnNaRaXlRMWPde']
        return(random.choice(recommendation))
    elif mood == 'in love' and genre == 'rock':
        recommendation = ['https://open.spotify.com/embed/track/5lDriBxJd22IhOH9zTcFrV', 'https://open.spotify.com/embed/track/7oK9VyNzrYvRFo7nQEYkWN', 'https://open.spotify.com/embed/track/5OQsiBsky2k2kDKy2bX2eT', 'https://open.spotify.com/embed/track/4UzVcXufOhGUwF56HT7b8M','https://open.spotify.com/embed/track/4JXfNOePhdgMOI7KZ1L25U']
        return(random.choice(recommendation))
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
    elif genre == 'r&b':
         return('Fill out the ENTIRE form!')
